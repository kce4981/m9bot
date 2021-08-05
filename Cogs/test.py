from discord.ext import commands
from . import m9cog


class peko(m9cog.M9Cog):

    def __init__(self, bot):
        super().__init__(bot)

    @commands.command(name='foo')
    async def foobar(self, ctx: commands.context):
        self.logger.info(f'{ctx.author} used foo')
        await ctx.send('bar')

    @commands.command(name='bar')
    async def bar(self, ctx: commands.context):
        await ctx.send('foo')


def setup(bot):
    bot.add_cog(peko(bot))
