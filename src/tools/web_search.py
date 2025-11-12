"""
Web search tool wrapper for research agent.
"""
from langchain_tavily import TavilySearch
from src.config.settings import settings


def create_web_search_tool():
	"""Create configured web search tool."""
	return TavilySearch(
		max_results=settings.MIN_RESEARCH_SOURCES,
		api_key=settings.TAVILY_API_KEY,
	)


