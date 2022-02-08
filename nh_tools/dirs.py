from os import getenv
from pathlib import Path


def get_path_from_env(var: str, default: Path):
    path = getenv(var)
    if path:
        path = Path(path)
    else:
        path = default
    return path


def get_home():
    return Path.home()


def get_config_path():
    return get_path_from_env('XDG_CONFIG_HOME', get_home() / '.config')


def get_data_path():
    return get_path_from_env('XDG_DATA_HOME', get_home() / '.local' / 'share')


def get_path_from_user_dirs(var: str, default: Path):
    data = (get_config_path() / 'user-dirs.dirs').read_text()
    user_dirs = {}
    for line in [line for line in data.split('\n') if not line.startswith('#') and line]:
        key, value = line.split('=')
        value = value.replace('$HOME', str('~'))
        user_dirs[key] = Path(value).expanduser()
    return user_dirs[var] if var in user_dirs else default


def get_music_path():
    return get_path_from_user_dirs('XDG_MUSIC_DIR', get_home() / 'Music')
