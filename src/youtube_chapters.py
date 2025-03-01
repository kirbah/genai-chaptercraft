# Install required libraries
import os
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import re

# Specify the YouTube video URL and the desired number of chapters
video_url = "https://www.youtube.com/watch?v=A9WY_HZUK8Q"
num_chapters = 0  # More than 3 chapters should be created. Either specified number of chapters generated or LLM will try to decide the best number of chapters


def extract_video_id(url):
    """Extracts the YouTube video ID from the provided URL."""
    match = re.search(r"(?:v=|youtu\.be/)([^&?]+)", url)
    if match:
        return match.group(1)
    raise ValueError("Invalid YouTube URL provided.")


# Retrieve video ID and transcript
video_id = extract_video_id(video_url)
transcript_segments = YouTubeTranscriptApi.get_transcript(video_id)
# Combine transcript text segments into a single string
transcript_text = "\n".join([segment["text"]
                            for segment in transcript_segments])

# Prepare the prompt for Gemini chapter generation
if num_chapters:
    chapter_generation_line = f"2. Generate exactly {num_chapters} distinct, non-overlapping chapters that cover different aspects of the video.\n"
else:
    chapter_generation_line = "2. Generate distinct, non-overlapping chapters that cover different aspects of the video.\n"

prompt = (
    "Based on the following transcript, please perform the following steps internally and then output a single final chapter list:\n"
    "1. Analyze the transcript and identify its key segments with approximate starting timestamps in MM:SS format.\n"
    f"{chapter_generation_line}"
    "3. The very first chapter must start at 00:00. All subsequent chapters should use the timestamp corresponding to when the segment begins, and the timestamps must be in ascending order with a minimum gap of 10 seconds between chapters.\n"
    "4. Format each chapter on its own line using the format '<timestamp> <chapter title>'. For example, '00:00 Introduction'.\n"
    "5. Do not include any additional commentary, explanations, chain-of-thought, or intermediate reasoning—only the final chapter list.\n"
    "6. Ensure that only one chapter list is generated and that there are no duplicate chapters or timestamps.\n\n"
    "Example:\n"
    "00:00 Introduction\n"
    "01:24 Key Concepts Overview\n"
    "08:56 Comparative Insights\n"
    "09:31 Conclusion and Next Steps\n\n"
    "### Transcript:\n"
    f"{transcript_text}\n\n"
    "Chapters:"
)


# Configure the Gemini API key from the environment variable
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError(
        "The GEMINI_API_KEY environment variable is not set. Please set it and try again.")

genai.configure(api_key=gemini_api_key)

# Set up the Gemini API generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 500,
    "response_mime_type": "text/plain",
}

# Create the Gemini generative model instance
model = genai.GenerativeModel(
    model_name="gemini-2.0-pro-exp-02-05",
    generation_config=generation_config,
)

# Start a chat session and send the prompt
chat_session = model.start_chat(history=[])
gemini_response = chat_session.send_message(prompt)

# Output the generated chapters
print("Generated Chapters:\n")
print(gemini_response.text)
