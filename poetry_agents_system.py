# poetry_agents_system.py

# pip install openai-agents
# pip install python-dotenv

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, function_tool
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables
load_dotenv()

# Get API Key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Setup OpenAI client
external_client = AsyncOpenAI(
    api_key=openai_api_key,
    base_url="https://api.openai.com/v1"
)

# Model configuration
model = OpenAIChatCompletionsModel(
    model="gpt-4o-mini",  # lightweight & cost-effective model
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# ---------- TOOLS ----------

@function_tool
def generate_poem(custom_poem: str = None):
    """
    Generate a poem. If a custom poem is provided, return it; otherwise, create a default poem.
    """
    if custom_poem:
        return custom_poem.strip()
    return (
        "The night was cold, the moon hung high,\n"
        "I whispered dreams into the sky.\n"
        "My thoughts were drenched in silent rain,\n"
        "Each heartbeat echoed with my pain.\n\n"
        "A shadow danced along the wall,\n"
        "Recalling times I can't recall.\n"
        "My soul adrift in endless sea,\n"
        "Longing for what used to be."
    )

@function_tool
def lyric_analysis(poem: str):
    """
    Analyze a poem as lyric poetry.
    """
    return (
        "🎵 **Lyric Analysis:**\n"
        "This is lyric poetry expressing deep personal emotions like sorrow and longing. "
        "Imagery like 'silent rain' and 'shadows' gives it a melancholic tone."
    )

@function_tool
def narrative_analysis(poem: str):
    """
    Analyze a poem for narrative elements.
    """
    return (
        "📖 **Narrative Analysis:**\n"
        "There are subtle story elements: a character reflecting on lost time, hinting at a past event. "
        "However, it lacks a full plot structure, so it's not primarily narrative poetry."
    )

@function_tool
def dramatic_analysis(poem: str):
    """
    Analyze a poem for dramatic qualities.
    """
    return (
        "🎭 **Dramatic Analysis:**\n"
        "The poem could be performed as a dramatic monologue. It has an introspective speaker, "
        "emotive tone, and theatrical potential suitable for stage delivery."
    )

# ---------- MAIN AGENT ----------

async def main():
    poetry_agent = Agent(
        name="Poetry Agent",
        instructions="Generate poems and provide lyric, narrative, and dramatic analyses.",
        tools=[generate_poem, lyric_analysis, narrative_analysis, dramatic_analysis]
    )

    # Replace with your own poem if you want
    response = await Runner.run(
        poetry_agent,
        input="Generate a poem and analyze it in lyric, narrative, and dramatic terms.",
        run_config=config
    )

    print("\n--- Poetry Agent Response ---")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
