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
    "Based on the following transcript, generate a chapter list following these instructions:\n"
    "1. Identify key topic shifts and assign each a starting timestamp in MM:SS format.\n"
    "2. Format each chapter as '<timestamp> <chapter title>' (e.g., '00:00 Introduction').\n"
    "3. Then, review the chapter list and if any chapter boundary seems misaligned (i.e., if two adjacent chapters do not clearly reflect a topic change), adjust or remove that boundary.\n"
    "Only output the final, self-reviewed chapter list without any extra commentary.\n\n"
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
    "temperature": 0.5,
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
