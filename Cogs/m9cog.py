from discord.ext import commands
import functools
import logging


class M9Cog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.logger = logging.getLogger('m9bot')

    def log_usage(self, ctx: commands.context):
        # replace with
        # https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=reload_extension#discord.ext.commands.Bot.before_invoke
        self.logger.info(f'{ctx.author} used command {ctx.command}, Raw -> {ctx.message.content}')
