# Install required libraries
import os
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import re

# Specify the YouTube video URL and the desired number of chapters
video_url = "https://www.youtube.com/watch?v=A9WY_HZUK8Q"


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


prompt = (
    "Based on the following transcript, generate a chapter list following these precise instructions:\n"
    "1. Identify **distinct and major topic shifts** in the transcript. Each significant topic change marks the start of a new chapter.  Focus on clear transitions in the subject matter discussed.\n"
    "2. For each chapter, determine the starting timestamp in MM:SS format **at the exact point where the topic clearly transitions to a new subject**.\n"
    "3. Format each chapter as a single line: '<timestamp> <chapter title>' (e.g., '00:00 Introduction'). Chapter titles should be concise (under 10 words) and accurately represent the chapter's primary topic.\n"
    "4. After generating the initial chapter list, **critically self-review** it for topic coherence. Ensure each chapter break corresponds to a genuine, significant topic change. Eliminate any chapter boundaries that are weak, ambiguous, or do not represent a clear shift in the discussion. The goal is to create chapters that represent meaningful thematic sections of the video.\n"
    "5. The final output should ONLY be the self-reviewed chapter list, with each chapter on a new line and in the specified '<timestamp> <chapter title>' format. Do not include any introductory or concluding sentences, explanations, or commentary.\n"
    "\n"
    "Example of the desired output format:\n"
    "00:00 Introduction to the Topic\n"
    "01:45 Deep Dive into Subject A\n"
    "05:20 Exploring Subject B\n"
    "08:30 Conclusion and Summary\n"
    "\n"
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
    "temperature": 0.0,
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
print("Generated using free 'GenAI ChapterCraft' tool.\n")
