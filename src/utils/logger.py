"""
Logging configuration.
"""
import logging
from src.config.settings import settings


def setup_logger(name: str):
	"""Configure and return logger."""
	logger = logging.getLogger(name)
	logger.setLevel(settings.LOG_LEVEL)

	# Avoid duplicate handlers during repeated imports/tests
	if not logger.handlers:
		handler = logging.StreamHandler()
		formatter = logging.Formatter(
			"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
		)
		handler.setFormatter(formatter)
		logger.addHandler(handler)

	return logger


