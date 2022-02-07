from pathlib import Path
from os import getenv
from nh_tool.file import open_file


def get_path_from_env(var: str, default: Path):
    path = getenv(var)
    if path:
        path = Path(path)
    else:
        path = default
    return path


def get_path_from_user_dirs(var: str, default: Path):
    data = open_file(get_config() / 'user-dirs.dirs')
    user_dirs = {}
    for line in [line for line in data.split('\n') if not line.startswith('#') and line]:
        key, value = line.split('=')
        value = value.replace('$HOME', str(get_home())).replace('"', '')
        user_dirs[key] = Path(value)
    return user_dirs[var] if var in user_dirs else default


def get_home():
    return Path.home()


def get_config():
    return get_path_from_env('XDG_CONFIG_HOME', get_home() / '.config')


def get_music_dir():
    return get_path_from_user_dirs('XDG_MUSIC_DIR', get_home() / 'Music')

def get_archive_dir():
    return get_home() / 'archive'
