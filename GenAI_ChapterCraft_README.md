# GenAI ChapterCraft: Automatic Video Chapter Generator

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kirbah/genai-chaptercraft/blob/main/GenAI_ChapterCraft.ipynb)

GenAI ChapterCraft is a free, open-source tool that automatically generates chapters for your videos using the power of AI.  It leverages state-of-the-art speech recognition (Whisper) and large language models (LLMs) like Gemini and models available via the Hugging Face Inference API to create accurate and SEO-friendly chapter titles with timestamps.  This tool saves you valuable time and effort, improves video discoverability, and enhances the viewer experience.

## Overview

This project provides a single, self-contained Google Colab notebook (`GenAI_ChapterCraft.ipynb`) that handles the entire process:

1.  **Video Input:**  Provide a video URL (e.g., YouTube, Vimeo).  For YouTube videos, the tool can try to retrieve an existing transcript for speed.
2.  **Audio Extraction (if needed):** If no YouTube transcript is found, the notebook downloads the audio.
3.  **Transcription:**  The audio is transcribed to text using the highly accurate Whisper model from OpenAI.
4.  **SRT Conversion:** The transcript is converted to the standard SRT (SubRip) subtitle format.
5.  **Chapter Generation:**  An LLM (Gemini or a Hugging Face model) analyzes the SRT transcript and intelligently generates chapters with appropriate titles and timestamps.

## Key Features

*   **Automatic Chapter Creation:**  Generate video chapters quickly and easily.
*   **High-Quality Transcription:** Uses OpenAI's Whisper for accurate audio-to-text conversion.
*   **Multiple LLM Options:** Choose between Google's Gemini API or models from the Hugging Face Inference API.
*   **SRT Output:**  Provides the transcript in the widely-used SRT format.
*   **GPU Acceleration:**  Automatically utilizes a GPU if available in Colab for faster processing.
*   **Easy to Use:**  Simply run the Colab notebook, providing your video URL and API keys (if required).
*   **Free and Open Source:**  No cost to use, and the code is available for modification and contribution.

## Getting Started

The easiest way to use GenAI ChapterCraft is to open the notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kirbah/genai-chaptercraft/blob/main/GenAI_ChapterCraft.ipynb)

Click the "Open in Colab" badge above.  This will launch the notebook in your Colab environment.

**Steps within Colab:**

1.  **Set Secrets:**  In the Colab sidebar (left side), click the "key" icon to access the Secrets manager.  You *may* need to set the following, depending on your chosen video source and LLM:
    *   `SUPADATA_TOKEN`:  *Only* required if retrieving existing YouTube transcripts. Obtain a token from [Supadata](https://supadata.ai/).
    *   `HF_TOKEN`:  *Only* required if using a Hugging Face model for chapter generation.  Get a token from [Hugging Face](https://huggingface.co/settings/tokens).
    *   `GEMINI_API_KEY`: *Only* required if using the Gemini API for chapter generation. Create an API key at [Google AI Studio](https://aistudio.google.com/apikey).

2.  **Enter Video URL:**  Locate the code cell containing `video_url = ...` and replace the example URL with the URL of your video.

3.  **Adjust `num_chapters` (Optional):**  Modify the `num_chapters` variable if you want a specific number of chapters (minimum 3).

4.  **Run the Notebook:** Go to "Runtime" -> "Run all" (or press Ctrl + F9).

5. **Review Output**: Examine the generated chapters and SRT transcript.

## Requirements (within Colab)

The Colab notebook will automatically install the necessary libraries (`yt_dlp`, `transformers`, `huggingface_hub`, `supadata`, `safetensors`).  A GPU runtime is highly recommended for faster processing, especially with larger videos.

## Limitations

*   **YouTube Transcript Availability:** For YouTube videos, the tool relies on the *existence* of a pre-generated transcript for optimal speed.  If no transcript is available, downloading and transcribing the audio will take significantly longer.  Direct YouTube video download is sometimes unreliable due to issues with the underlying `yt-dlp` library.
*   **LLM Variability:** The quality of generated chapters depends on the LLM used.  You may need to experiment with different models or adjust the prompt for optimal results.
*   **Video Length:** Very long videos may require significant processing time, even with a GPU.

## Contributing

Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details.
```
