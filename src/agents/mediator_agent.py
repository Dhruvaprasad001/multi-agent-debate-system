"""
Mediator Agent: Synthesizes perspectives and facilitates consensus.
"""
from langgraph.prebuilt import create_react_agent
from src.agents.base_agent import create_llm
from src.prompts.mediator_prompt import MEDIATOR_PROMPT


def create_mediator_agent():
	"""Create and return mediator agent."""
	llm = create_llm()
	return create_react_agent(
		model=llm,
		tools=[],
		prompt=MEDIATOR_PROMPT,
		name="mediator_agent",
	)


