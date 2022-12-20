import openai
from discord.ext import commands
import settings

openai.api_key = settings.OPENAI_TOKEN

class ChatCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def chat(self, ctx, *, message):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=message,
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    await ctx.send(response.choices[0].text)

async def setup(bot):
    await bot.add_cog(ChatCog(bot))