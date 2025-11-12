"""
Edge routing logic for the debate graph.
"""
from src.graph.state import DebateState


def should_continue_debate(state: DebateState) -> str:
	"""Determine if debate should continue or conclude."""
	if state["is_complete"] or state["debate_round"] >= state["max_rounds"]:
		return "end"
	return "continue"


