"""
Assemble the complete debate graph.
"""
from langgraph.graph import StateGraph, START, END
from src.graph.state import DebateState
from src.graph.nodes import research_node, optimist_node, critic_node, mediator_node
from src.graph.edges import should_continue_debate
from src.memory.checkpointer import create_checkpointer


def create_debate_graph():
	"""Build and return compiled debate graph."""
	workflow = StateGraph(DebateState)

	# Add nodes
	workflow.add_node("research", research_node)
	workflow.add_node("optimist", optimist_node)
	workflow.add_node("critic", critic_node)
	workflow.add_node("mediator", mediator_node)

	# Add edges
	workflow.add_edge(START, "research")
	workflow.add_edge("research", "optimist")
	workflow.add_edge("optimist", "critic")
	workflow.add_edge("critic", "mediator")

	# Conditional routing
	workflow.add_conditional_edges(
		"mediator",
		should_continue_debate,
		{
			"continue": "optimist",
			"end": END,
		},
	)

	# Compile with memory
	return workflow.compile(checkpointer=create_checkpointer())


