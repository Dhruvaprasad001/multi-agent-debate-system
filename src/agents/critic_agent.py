"""
Critic Agent: Argues the negative side.
"""
from langgraph.prebuilt import create_react_agent
from src.agents.base_agent import create_llm
from src.prompts.critic_prompt import CRITIC_PROMPT


def create_critic_agent():
	"""Create and return critic agent."""
	llm = create_llm()
	return create_react_agent(
		model=llm,
		tools=[],
		prompt=CRITIC_PROMPT,
		name="critic_agent",
	)


