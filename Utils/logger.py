import logging

logging.getLogger().setLevel(logging.INFO)

discord_logger = logging.getLogger('discord')
m9Bot_logger = logging.getLogger('m9bot')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('\033[0;33m[%(asctime)s %(levelname)s] %(name)s: %(message)s', datefmt='%H:%M:%S'))
discord_logger.addHandler(ch)
m9Bot_logger.addHandler(ch)

