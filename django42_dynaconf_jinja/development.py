from pathlib import Path
import sys

import dynaconf
from dynaconf import LazySettings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
SETTINGS_DIR = Path(__file__).resolve().parent

config_files = [
    SETTINGS_DIR / 'base.py',
    SETTINGS_DIR / 'jinja_test.json',
    SETTINGS_DIR / 'dynaconf_jinja_example.yaml',
]
DYNACONF_settings = LazySettings(
    commentjson_enabled=True,
    environments=True,
    merge_enabled=True,
    settings_files=config_files,
)

print(dynaconf.inspect_settings(DYNACONF_settings))

DYNACONF_settings.populate_obj(sys.modules[__name__])

