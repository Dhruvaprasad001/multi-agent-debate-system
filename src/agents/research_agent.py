"""
Research Agent: Gathers factual information about debate topics.
"""
from langgraph.prebuilt import create_react_agent
from src.agents.base_agent import create_llm
from src.tools.web_search import create_web_search_tool
from src.prompts.research_prompt import RESEARCH_PROMPT


def create_research_agent():
	"""Create and return research agent."""
	llm = create_llm()
	tools = [create_web_search_tool()]

	return create_react_agent(
		model=llm,
		tools=tools,
		prompt=RESEARCH_PROMPT,
		name="research_agent",
	)


