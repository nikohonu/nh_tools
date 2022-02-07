from pathlib import Path
from json import dump, load


def open_file(path: Path):
    with open(path) as f:
        data = f.read()
    return data


def save_file(path: Path, data):
    with open(path, 'w') as f:
        f.write(data)


def open_json(path: Path):
    if path.exists():
        with open(path) as f:
            return load(f)
    else:
        return {}


def save_json(path: Path, data):
    with open(path, 'w') as f:
        dump(data, f, indent=4)
