"""
Unit tests for individual agents.
"""
from src.agents.research_agent import create_research_agent
from src.agents.optimist_agent import create_optimist_agent
from src.agents.critic_agent import create_critic_agent
from src.agents.mediator_agent import create_mediator_agent


def test_research_agent_creation():
	"""Test research agent initialization."""
	agent = create_research_agent()
	assert agent is not None


def test_optimist_agent_creation():
	agent = create_optimist_agent()
	assert agent is not None


def test_critic_agent_creation():
	agent = create_critic_agent()
	assert agent is not None


def test_mediator_agent_creation():
	agent = create_mediator_agent()
	assert agent is not None


