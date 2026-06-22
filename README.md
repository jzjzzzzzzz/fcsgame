# FCSGame

Console-based Python farming, crafting, and survival game prototype. The game stores player and farm state in text files under `data/`.

## Project Structure

- `generate_map.py`: main game script with world generation, character state, inventory, farming, exploration, save/load, and interaction loops.
- `data/player_data.txt`: saved player state.
- `data/farm_data.txt`: saved farm state.
- `requirements.txt`: currently documents that no third-party packages are required.

## Setup

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Run

```bash
.venv/bin/python generate_map.py
```

Follow the terminal prompts to play.

## Notes

- This is an interactive terminal game, so automated tests are not configured yet.
- Save files in `data/` are currently tracked as sample/default state.
- Future cleanup should split the large `generate_map.py` file into modules before adding more features.
