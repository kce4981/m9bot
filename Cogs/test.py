from discord.ext import commands
import requests
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

    @commands.command(name='peko')
    async def peko(self, ctx, arg):
        self.log_usage(ctx)
        message = await ctx.channel.fetch_message(arg)
        await ctx.send('yeet', reference=message, mention_author=False)

    @commands.command(name='del_test')
    async def del_test(self, ctx, arg):
        self.log_usage(ctx)
        message = await ctx.channel.fetch_message(arg)
        await ctx.send(message.reference)


def setup(bot):
    bot.add_cog(peko(bot))
