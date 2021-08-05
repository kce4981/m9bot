from types import SimpleNamespace
import json

with open('config.json', mode='r', encoding='utf-8') as fp:
    config = json.load(fp, object_hook=lambda d: SimpleNamespace(**d))
