"""
Utility script to ensure the memory database directory exists.
"""
import os
from src.config.settings import settings


def main():
	db_dir = os.path.dirname(settings.MEMORY_DB_PATH)
	os.makedirs(db_dir, exist_ok=True)
	print(f"Ensured DB directory exists at: {db_dir}")


if __name__ == "__main__":
	main()


