"""
Input validation functions.
"""


def validate_topic(topic: str) -> bool:
	"""Validate debate topic input."""
	if not topic or len(topic.strip()) < 10:
		return False
	return True


def validate_max_rounds(rounds: int) -> bool:
	"""Validate max rounds parameter."""
	return 1 <= rounds <= 10


