# Multi-Agent Debate System

A LangChain + LangGraph application where specialized AI agents (Research, Optimist, Critic, Mediator) debate a topic over multiple rounds and synthesize a consensus.

## Quickstart
1) Create a virtual environment and install dependencies:
```
pip install -r requirements.txt
```
2) Copy `.env.example` to `.env` and set your API keys.
3) Run:
```
python scripts/run_debate.py --topic "Should AI be regulated by government?" --rounds 3
```

## Structure
See `docs/architecture.md` for a deep dive into folders, state, and graph orchestration.


