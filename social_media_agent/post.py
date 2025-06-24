# ------------------------------------------------------
# Step 0: Import packages and modules
# ------------------------------------------------------
import asyncio
import os
from youtube_transcript_api._api import YouTubeTranscriptApi 
from agents import Agent, Runner, WebSearchTool, function_tool, ItemHelpers
from openai import OpenAI
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import List, Optional


# ------------------------------------------------------
# Step 1: Get OpenAI API key
# ------------------------------------------------------

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)


# ------------------------------------------------------
# Step 2: Define tools for agents
# ------------------------------------------------------
@function_tool
def generate_content(video_transcipt: str, social_media_platform: str):
    print(f"Generating social media content for {social_media_platform}...")

    # Iniatialize the OpenAI client
    client = OpenAI(api_key=openai_api_key)

    # Generate content
    response = client.responses.create(
        model="gpt-4o",
        input=[{
            "role": "user",
            "content": f"Here is a new video transcript:\n{video_transcipt}\n\n"
                        f"Generate a social mdia post on my {social_media_platform}"
        }],
        max_output_tokens=2500 #increase tokens for longer blocks
    )
    return response.output_text

# ------------------------------------------------------
# Step 3: Define agents (content writer agent)
# ------------------------------------------------------

@dataclass
class Post:
    platform: str
    content: str



content_writer_agent = Agent(
    name = "Content Writer",
    instructions="""You are a content writer for a social media platform.
                    You will be given a video transcript and a social media platform. You
                    will generate a social media post based on the video transcript and the
                    social media platform.
                    You may search the web for up-to-date information on the topic and fill in
                    some useful details if needed.""",
    model="gpt-4o-mini",
    tools = [generate_content, 
             WebSearchTool(),
             ],

    output_type=List[Post]
    )


# ------------------------------------------------------
# Step 4: Define helper functions
# ------------------------------------------------------

# Fetch the transcript of a YouTube video using the video ID
def get_transcript(video_id: str, languages: Optional[list] = None) -> str:
    """
    Retrieves the transcript for a YouTube video.

    Args:
        video_id (str): The YouTube video ID.
        languages (list, optional): List of language codes to try, in order of preference.
                                   Defaults to ["en"] if None.

    Returns:
        str: The concatenated transcript text.

    Raises:
        Exception: If transcript retrieval fails, with details about the failure.
    """
    if languages is None:
        languages = ["en"]

    try:
        # Use the Youtube transcript API
        fetched_transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)

        # More efficient way to concatenate all text snippets
        transcript_text = " ".join(item['text'] for item in fetched_transcript)

        return transcript_text

    except Exception as e:
        # Handle specific YouTube transcript API exceptions
        from youtube_transcript_api._errors import (
            CouldNotRetrieveTranscript, 
            VideoUnavailable,
            InvalidVideoId, 
            NoTranscriptFound,
            TranscriptsDisabled
        )

        if isinstance(e, NoTranscriptFound):
            error_msg = f"No transcript found for video {video_id} in languages: {languages}"
        elif isinstance(e, VideoUnavailable):
            error_msg = f"Video {video_id} is unavailable"
        elif isinstance(e, InvalidVideoId):
            error_msg = f"Invalid video ID: {video_id}"
        elif isinstance(e, TranscriptsDisabled):
            error_msg = f"Transcripts are disabled for video {video_id}"
        elif isinstance(e, CouldNotRetrieveTranscript):
            error_msg = f"Could not retrieve transcript: {str(e)}"
        else:
            error_msg = f"An unexpected error occurred: {str(e)}"

        print(f"Error: {error_msg}")
        raise Exception(error_msg) from e

# --------------------------------------------------------------
# Step 5: Run the agent
# --------------------------------------------------------------
async def main():
    video_id = "OZ5OZZZ2cvk"
    transcript = get_transcript(video_id)

    msg = f"Generate a LinkedIn post and an Instagram caption based on this video transcript: {transcript}"

    # Package input for the agent
    # Use a string input if that's what the agent expects
    input_items = msg

    # Run content writer agent
    result = await Runner.run(content_writer_agent, input_items)
    output = ItemHelpers.text_message_outputs(result.new_items)
    print("Generated Post:\n", output)

if __name__ == "__main__":
    asyncio.run(main())
