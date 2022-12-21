import openai
from discord.ext import commands
import settings

#Le token d'openAI
openai.api_key = settings.OPENAI_TOKEN

#La classe qui nous permet de répondre à la commande !chat
#Elle récupère le texte, l'envois a l'api openAI, la traite et retourn la réponse dans le même canel que la commande
#Vous pouvez changer de canal ou mettre en dm en modifiant (await ctx.send(response.choices[0].text))
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

#On définit le setup pour le launch dand le bot
async def setup(bot):
    await bot.add_cog(ChatCog(bot))