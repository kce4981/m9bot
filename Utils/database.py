from types import SimpleNamespace
import pathlib
import json

# for file in pathlib.Path(__name__).:
#    pass

with open('config.json', mode='r', encoding='utf-8') as fp:
    config = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
with open('token.json', mode='r', encoding='utf-8') as fp:
    token = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
