## Usage Guide

1) Install dependencies:
```
pip install -r requirements.txt
```
2) Copy `env.example` to `.env` and set API keys.
3) Run a debate:
```
python scripts/run_debate.py --topic "Should AI be regulated by government?" --rounds 3
```

Tips:
- Tune model and rounds in `.env`.
- Check `data/` for persisted artifacts (DB and transcripts if added).


