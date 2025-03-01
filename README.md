# GenAI ChapterCraft Project

This project provides tools for generating chapters from YouTube videos using Generative AI.

## Overview

The main components of this project are:

- `GenAI_ChapterCraft.ipynb`: A Jupyter Notebook containing a playground with various features and experimentation related to chapter generation. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kirbah/genai-chaptercraft/blob/main/GenAI_ChapterCraft.ipynb)
- `GenAI_ChapterCraft_YouTube.ipynb`: A Jupyter Notebook focused on generating chapters specifically from YouTube videos. [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kirbah/genai-chaptercraft/blob/main/GenAI_ChapterCraft_YouTube.ipynb)
- `src/youtube_chapters.py`: A Python script to generate chapters for a given YouTube video.

## Running `youtube_chapters.py`

This script generates chapters for a YouTube video using the Gemini API.

### Prerequisites

1.  **Install Dependencies:** Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

    This will install the following packages:

    - `youtube-transcript-api`
    - `google-generativeai`

2.  **Set Environment Variable:** You need to set the `GEMINI_API_KEY` environment variable with your Gemini API key. You can obtain an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

    - **Windows (Command Prompt):**

      ```bash
      set GEMINI_API_KEY=your_gemini_api_key
      ```

    - **Windows (PowerShell):**

      ```powershell
      $env:GEMINI_API_KEY = "your_gemini_api_key"
      ```

    - **Linux/macOS:**
      ```bash
      export GEMINI_API_KEY=your_gemini_api_key
      ```
      (Replace `your_gemini_api_key` with your actual Gemini API key.)

### Usage

Once you have installed the dependencies and set the environment variable, you can run the script:

```bash
python src/youtube_chapters.py
```

The script will fetch the transcript of the YouTube video specified in the `video_url` variable within the script, generate chapters using the Gemini API, and print the generated chapters to the console. You may change `video_url` variable to generate chapters for another video.
