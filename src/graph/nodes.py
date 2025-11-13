"""
Node functions for the debate graph.
"""
from typing import Dict
from src.graph.state import DebateState
from src.agents.research_agent import create_research_agent
from src.agents.optimist_agent import create_optimist_agent
from src.agents.critic_agent import create_critic_agent
from src.agents.mediator_agent import create_mediator_agent

# Create agents once at module level
research_agent = create_research_agent()
optimist_agent = create_optimist_agent()
critic_agent = create_critic_agent()
mediator_agent = create_mediator_agent()


def research_node(state: DebateState) -> DebateState:
	"""Research agent node - gathers facts about the topic."""
	topic = state["topic"]
	
	print("\n" + "=" * 60)
	print("🔍 RESEARCH AGENT")
	print("=" * 60)
	print(f"Researching: {topic}...")
	
	result = research_agent.invoke({
		"messages": [{"role": "user", "content": f"Research the topic: {topic}"}]
	})
	
	# Extract the research facts from the agent's response
	if result and "messages" in result and len(result["messages"]) > 0:
		research_content = result["messages"][-1].content
		state["research_facts"] = research_content
		state["messages"] = state.get("messages", []) + [
			{"role": "assistant", "name": "research_agent", "content": research_content}
		]
		print(f"\n{research_content}\n")
	
	return state


def optimist_node(state: DebateState) -> DebateState:
	"""Optimist agent node - argues the positive side."""
	topic = state["topic"]
	research = state.get("research_facts", "")
	context = f"Topic: {topic}\nResearch: {research}\nRound: {state['debate_round']}"
	
	print("\n" + "=" * 60)
	print(f"✅ OPTIMIST AGENT - Round {state['debate_round']}")
	print("=" * 60)
	print("Formulating positive arguments...")
	
	result = optimist_agent.invoke({
		"messages": [{"role": "user", "content": context}]
	})
	
	if result and "messages" in result and len(result["messages"]) > 0:
		argument = result["messages"][-1].content
		state["optimist_arguments"] = state.get("optimist_arguments", []) + [argument]
		state["messages"] = state.get("messages", []) + [
			{"role": "assistant", "name": "optimist_agent", "content": argument}
		]
		print(f"\n{argument}\n")
	
	return state


def critic_node(state: DebateState) -> DebateState:
	"""Critic agent node - argues the negative side."""
	topic = state["topic"]
	research = state.get("research_facts", "")
	optimist_args = state.get("optimist_arguments", [])
	context = f"Topic: {topic}\nResearch: {research}\nOptimist's arguments: {optimist_args[-1] if optimist_args else 'None'}\nRound: {state['debate_round']}"
	
	print("\n" + "=" * 60)
	print(f"❌ CRITIC AGENT - Round {state['debate_round']}")
	print("=" * 60)
	print("Formulating counter-arguments...")
	
	result = critic_agent.invoke({
		"messages": [{"role": "user", "content": context}]
	})
	
	if result and "messages" in result and len(result["messages"]) > 0:
		counter = result["messages"][-1].content
		state["critic_arguments"] = state.get("critic_arguments", []) + [counter]
		state["messages"] = state.get("messages", []) + [
			{"role": "assistant", "name": "critic_agent", "content": counter}
		]
		print(f"\n{counter}\n")
	
	return state


def mediator_node(state: DebateState) -> DebateState:
	"""Mediator agent node - synthesizes arguments and determines if debate should continue."""
	topic = state["topic"]
	optimist_args = state.get("optimist_arguments", [])
	critic_args = state.get("critic_arguments", [])
	context = f"Topic: {topic}\nRound: {state['debate_round']}/{state['max_rounds']}\nOptimist's arguments: {optimist_args}\nCritic's arguments: {critic_args}\n\nProvide a synthesis and decide if we need more debate rounds."
	
	print("\n" + "=" * 60)
	print(f"⚖️  MEDIATOR AGENT - Round {state['debate_round']}/{state['max_rounds']}")
	print("=" * 60)
	print("Synthesizing arguments...")
	
	result = mediator_agent.invoke({
		"messages": [{"role": "user", "content": context}]
	})
	
	if result and "messages" in result and len(result["messages"]) > 0:
		mediator_response = result["messages"][-1].content
		
		# Check if we should continue or end
		if state["debate_round"] >= state["max_rounds"]:
			state["consensus"] = mediator_response
			state["is_complete"] = True
		else:
			state["debate_round"] += 1
			state["is_complete"] = False
		
		state["messages"] = state.get("messages", []) + [
			{"role": "assistant", "name": "mediator_agent", "content": mediator_response}
		]
		print(f"\n{mediator_response}\n")
	
	return state


