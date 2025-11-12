"""
Optimist Agent: Argues the positive side.
"""
from langgraph.prebuilt import create_react_agent
from src.agents.base_agent import create_llm
from src.prompts.optimist_prompt import OPTIMIST_PROMPT


def create_optimist_agent():
	"""Create and return optimist agent."""
	llm = create_llm()
	return create_react_agent(
		model=llm,
		tools=[],
		prompt=OPTIMIST_PROMPT,
		name="optimist_agent",
	)


