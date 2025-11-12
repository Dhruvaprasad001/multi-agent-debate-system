"""
Format debate outputs for display.
"""
from src.graph.state import DebateState


def format_debate_summary(state: DebateState) -> str:
	"""Format final debate state into readable summary."""
	summary = f"""
============================================================
                    DEBATE SUMMARY                        
============================================================

Topic: {state['topic']}
Total Rounds: {max(0, state['debate_round'] - 1)}

CONSENSUS:
{state['consensus']}
"""
	return summary


