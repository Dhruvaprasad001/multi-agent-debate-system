"""
Central configuration for the debate system.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
	"""Application settings loaded from environment variables."""

	# API Keys
	OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
	TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")

	# Model Configuration
	MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4")
	MODEL_TEMPERATURE: float = float(os.getenv("MODEL_TEMPERATURE", "0.7"))

	# Debate Configuration
	MAX_DEBATE_ROUNDS: int = int(os.getenv("MAX_DEBATE_ROUNDS", "3"))
	MIN_RESEARCH_SOURCES: int = 5

	# Memory Configuration
	MEMORY_DB_PATH: str = "data/memory/debate_memory.db"

	# Logging
	LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()


