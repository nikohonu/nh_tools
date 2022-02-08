from json import dump
from json import load
from pathlib import Path


def open_json(path: Path, default={}):
    if path.exists():
        with path.open() as f:
            return load(f)
    else:
        return default


def save_json(path: Path, data):
    with path.open('w') as f:
        dump(data, f, indent=4)
