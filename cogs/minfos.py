import discord
from discord.ext import commands

class UserInfos(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfos(self, ctx, *, member: discord.Member):
        # Check if the member exists
        try:
            # Create the embed
            embed = discord.Embed(color=discord.Color.blue())
            embed.set_author(name=member.name, icon_url=member.avatar)
            embed.add_field(name='Status', value=member.status, inline=True)
            embed.add_field(name='Roles', value=', '.join([role.name for role in member.roles]), inline=True)
            # Send the embed to the user
            await ctx.author.send(embed=embed)
        except Exception as e:
            # Send an error message if the member does not exist
            await ctx.send(f'Error: {e}')

async def setup(bot):
    await bot.add_cog(UserInfos(bot))