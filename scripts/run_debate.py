"""
Main script to run debates.
"""
import argparse
import sys
from src.graph.debate_graph import create_debate_graph
from src.utils.output_formatter import format_debate_summary
from src.utils.logger import setup_logger

# Set UTF-8 encoding for stdout (Windows compatibility)
if sys.platform == "win32":
	sys.stdout.reconfigure(encoding='utf-8')

logger = setup_logger(__name__)


def main():
	parser = argparse.ArgumentParser(description="Run multi-agent debate")
	parser.add_argument("--topic", required=True, help="Debate topic")
	parser.add_argument("--rounds", type=int, default=3, help="Max debate rounds")

	args = parser.parse_args()

	logger.info(f"Starting debate on: {args.topic}")

	# Create and run debate
	graph = create_debate_graph()
	initial_state = {
		"messages": [],
		"topic": args.topic,
		"research_facts": "",
		"optimist_arguments": [],
		"critic_arguments": [],
		"consensus": "",
		"debate_round": 1,
		"max_rounds": args.rounds,
		"is_complete": False,
	}

	config = {"configurable": {"thread_id": "debate-001"}}

	final_state = None
	for update in graph.stream(initial_state, config):
		final_state = update
		# Print node updates for debugging
		node_name = list(update.keys())[0] if update else "unknown"
		logger.info(f"Completed node: {node_name}")

	# Format and print results
	if final_state:
		result = list(final_state.values())[0]
		logger.info(f"Final state - Round: {result.get('debate_round')}, Is Complete: {result.get('is_complete')}")
		logger.info(f"Consensus length: {len(result.get('consensus', ''))}")
		print(format_debate_summary(result))


if __name__ == "__main__":
	main()


