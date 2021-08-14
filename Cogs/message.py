import io
from typing import List

import discord
import requests
from datetime import datetime, timezone
from PIL import Image, ImageColor, ImageDraw, ImageFont

from Utils.location import src
from Utils.database import db
from discord.ext import commands
from . import m9cog


def setup(bot):
    bot.add_cog(quote(bot))


class quote(m9cog.M9Cog):

    def __init__(self, bot):
        super().__init__(bot)
        self.db = db(db_name='quote.db', sql_query='quote_db.sql')

    @commands.command(name='viewquote')
    async def viewquote(self, ctx, quote_id: int):
        qte = self.select_quote(quote_id)[0]
        if not qte:
            ctx.send('quote does not exist')
            return
        else:
            qte_target = ctx.guild.get_member(qte[1])
            await self.send_image(ctx, self.generate_image(qte_target, qte[3], datetime.fromtimestamp(qte[4])))

    # async def quote_test(self, ctx):
    #     self.generate_image()
    #     pass

    def insert_db(self, msg_id: int, msg_author_id: int, quote_creator_id: int, msg_content: str,
                  quote_timestamp: datetime):
        # add local utc offset
        # https://stackoverflow.com/a/13287083/13168925
        ctx_msg_time = quote_timestamp.replace(tzinfo=timezone.utc).astimezone(tz=None)
        ins = 'INSERT INTO Quotes (Message_id, Message_author_id, Quote_creator_id, Message_content, Quote_time) VALUES(?, ?, ?, ?, ?)'
        self.db.curs.execute(ins, (msg_id, msg_author_id, quote_creator_id, msg_content, ctx_msg_time.timestamp()))
        self.db.commit()

    def select_quote(self, message_id: int) -> List[tuple]:
        """returns msg_id int,
        msg_author_id int,
        quote_creator_id int,
        msg_content str,
        quote_epoch float"""
        ins = 'SELECT * from Quotes WHERE Message_id = (?);'
        self.db.curs.execute(ins, (message_id,))
        return self.db.curs.fetchall()

    @commands.command(name='quote')
    async def quote(self, ctx):

        if ctx.message.reference is None:
            await ctx.send('no reference')
        else:
            quote_msg = await ctx.fetch_message(ctx.message.reference.message_id)
            self.insert_db(quote_msg.id, quote_msg.author.id, ctx.author.id, quote_msg.content, ctx.message.created_at)
        pass

    @commands.is_owner()
    @commands.command(name='validquote')
    async def vaildquote(self, ctx):
        # i think it's impossible, maybe delete?
        pass

    def generate_image(self, quote_target: discord.member, message: str, timestamp: datetime) -> Image:

        # profile picture
        img = Image.open(requests.get(quote_target.avatar_url, stream=True).raw)
        # make image transparent
        img = img.convert('RGBA')
        img = img.resize((96, 96), Image.ANTIALIAS)

        # https://stackoverflow.com/a/22336005/13168925
        # make profile picture circle
        bigsize = (img.size[0] * 3, img.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(img.size, Image.ANTIALIAS)

        # image background, todo add white theme
        bg_img = Image.new('RGB', (608, 160), color=(54, 57, 63))
        bg_img.paste(img, box=(20, int(80 - (img.size[1] / 2))), mask=mask)

        # text
        font_draw = ImageDraw.Draw(bg_img)

        # font
        ascii_font = ImageFont.truetype(str(src / 'Main.otf'), 38)
        time_font = ImageFont.truetype(str(src / 'Main.otf'), 30)

        # name
        font_draw.text((138, 24), quote_target.display_name, font=ascii_font, fill='#cfffe5')
        # message
        font_draw.text((138, 80), message, font=ascii_font)
        # timestamp
        font_draw.text((312, 35), timestamp.strftime("%Y/%m/%d"), font=time_font, fill='#9B9B9B')

        return bg_img

    async def send_image(self, ctx, image: Image):
        # https://stackoverflow.com/questions/63209888/send-pillow-image-on-discord-without-saving-the-image
        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))
