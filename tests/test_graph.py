"""
Test graph workflow execution.
"""
from src.graph.debate_graph import create_debate_graph


def test_graph_compilation():
	"""Test graph compiles without errors."""
	graph = create_debate_graph()
	assert graph is not None


