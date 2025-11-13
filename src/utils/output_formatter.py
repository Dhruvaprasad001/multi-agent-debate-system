"""
Format debate outputs for display.
"""
from src.graph.state import DebateState


def format_debate_summary(state: DebateState) -> str:
	"""Format final debate state into readable summary."""
	
	optimist_args = state.get('optimist_arguments', [])
	critic_args = state.get('critic_arguments', [])
	rounds_completed = len(optimist_args)
	
	# Build debate history
	history = ""
	for i in range(rounds_completed):
		history += f"\n{'─' * 60}\n"
		history += f"Round {i + 1}:\n"
		history += f"{'─' * 60}\n"
		
		if i < len(optimist_args):
			history += f"\n✅ OPTIMIST:\n{optimist_args[i]}\n"
		
		if i < len(critic_args):
			history += f"\n❌ CRITIC:\n{critic_args[i]}\n"
	
	summary = f"""
{'=' * 60}
                 📊 DEBATE SUMMARY 📊
{'=' * 60}

📌 Topic: {state['topic']}
🔄 Total Rounds Completed: {rounds_completed}

{history}

{'=' * 60}
              ⚖️  FINAL CONSENSUS ⚖️
{'=' * 60}

{state.get('consensus', 'No consensus reached.')}

{'=' * 60}
"""
	return summary


