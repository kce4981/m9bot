import discord
from discord.ext import commands
from . import m9cog


def setup(bot):
    bot.add_cog(quote(bot))


class quote(m9cog.M9Cog):

    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name='quote')
    async def quote(self, ctx):
        # https://discordpy.readthedocs.io/en/stable/api.html#discord.TextChannel.fetch_message
        # ctx.send(generated_image)
        self.generate_image()
        pass

    @commands.command(name='addquote')
    async def addquote(self, ctx):
        pass

    @commands.command(name='validquote')
    async def vaildquote(self, ctx):
        # valid if the quote is real or not
        # should return valid, deleted or not existed
        # https://discordpy.readthedocs.io/en/stable/api.html#deletedreferencedmessage
        pass

    def generate_image(self):
        # PIL ?
        pass
