"""
Memory checkpointer configuration.
"""
from langgraph.checkpoint.sqlite import SqliteSaver
from src.config.settings import settings
import os
import sqlite3


def create_checkpointer():
	"""Create and return configured checkpointer."""
	# Ensure directory exists
	os.makedirs(os.path.dirname(settings.MEMORY_DB_PATH), exist_ok=True)
	# Create connection and pass to SqliteSaver
	conn = sqlite3.connect(settings.MEMORY_DB_PATH, check_same_thread=False)
	return SqliteSaver(conn)


