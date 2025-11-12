"""
Base agent utilities and common functionality.
"""
from langchain_openai import ChatOpenAI
from src.config.settings import settings


def create_llm():
	"""Create and return configured LLM instance."""
	return ChatOpenAI(
		model=settings.MODEL_NAME,
		temperature=settings.MODEL_TEMPERATURE,
		api_key=settings.OPENAI_API_KEY,
	)


