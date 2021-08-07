from discord.ext import commands
import logging


class M9Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('m9bot')

    def log_usage(self, ctx : commands.context):
        self.logger.info()