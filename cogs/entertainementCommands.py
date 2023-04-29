import discord
from discord.ext import commands

class Entertainement(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_command('help')
        
    @commands.command()
    async def bhour(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=0J2QdDbelmY')
    
    @commands.command()
    async def bday(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=I7rCNiiNPxA')
       
    @commands.command()
    async def starwars(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=U9t-slLl30E')
    
    
    async def setup(bot):
        await bot.add_cog(Entertainement(bot))