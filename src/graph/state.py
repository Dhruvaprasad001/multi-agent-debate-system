"""
Define the debate state schema.
"""
from typing import TypedDict, Annotated, List, Any
from langgraph.graph import add_messages


class DebateState(TypedDict):
	"""Shared state across all debate agents."""
	messages: Annotated[List[Any], add_messages]
	topic: str
	research_facts: str
	optimist_arguments: List[str]
	critic_arguments: List[str]
	consensus: str
	debate_round: int
	max_rounds: int
	is_complete: bool


