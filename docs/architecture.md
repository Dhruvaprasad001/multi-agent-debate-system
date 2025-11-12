## Architecture Overview

- **Agents**: Research, Optimist, Critic, Mediator — each with a focused role.
- **Graph**: Orchestrates agent nodes with conditional routing via Mediator.
- **State**: Shared, typed state accessible to all agents.
- **Memory**: SQLite checkpointer for persistence across runs.
- **Tools**: Web search (Tavily) and custom tools (extensible).

See `src/graph/debate_graph.py` for the wiring and `src/graph/state.py` for the schema.


