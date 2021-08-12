import logging
import copy

logging.getLogger().setLevel(logging.INFO)

# discord_logger = logging.getLogger('discord')
# ch_dc = logging.StreamHandler()
# ch_dc.setFormatter(logging.Formatter('\033[0;33m[\033[0;32mDiscord\033[0;33m %(asctime)s %(levelname)s] %(message)s', datefmt='%H:%M:%S'))
# discord_logger.addHandler(ch_dc)

m9Bot_logger = logging.getLogger('m9bot')
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('\033[0;33m[\033[0;32mM9bot\033[0;33m %(asctime)s %(levelname)s] %(message)s', datefmt='%H:%M:%S'))
m9Bot_logger.addHandler(ch)

