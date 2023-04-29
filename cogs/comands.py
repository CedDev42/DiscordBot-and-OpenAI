import discord
from discord.ext import commands
import settings
import openai

class BotCommandes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def chat(self, ctx, *, message):
        openai.api_key = settings.OPENAI_TOKEN
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
        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')
        
    @commands.command()
    async def userinfos(self, ctx, member: discord.Member):
        embed = discord.Embed(title="User infos", description="Here are the user infos", color=discord.Color.blue())
        embed.add_field(name="Name", value=member.name, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Status", value=member.status, inline=False)
        embed.add_field(name="Top role", value=member.top_role, inline=False)
        embed.add_field(name="Joined at", value=member.joined_at, inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}")
        embed.timestamp = ctx.message.created_at
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        
        await ctx.author.send(embed=embed)
    
    @commands.command()
    async def setusergroup(self, ctx, member: discord.Member, group: discord.Role):
        try:
            await member.add_roles(group)
            await ctx.send(f'User {member.name} has been added to {group.name}')
        except Exception as e:
            await ctx.send(f'Error: {e}')
    
    @commands.command()        
    async def removeusergroup(self, ctx, member: discord.Member, group: discord.Role):
        try:
            await member.remove_roles(group)
            await ctx.send(f'User {member.name} has been removed from {group.name}')
        except Exception as e:
            await ctx.send(f'Error: {e}')
            
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f'User {member.name} has been kicked')
        except Exception as e:
            await ctx.send(f'Error: {e}')
        
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f'User {member.name} has been banned')
        except Exception as e:
            await ctx.send(f'Error: {e}')
    
    @commands.command()
    async def unban(self, ctx, *, member):
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')
            
            for ban_entry in banned_users:
                user = ban_entry.user
                
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'User {user.name}#{user.discriminator} has been unbanned')
                    return
        except Exception as e:
            await ctx.send(f'Error: {e}')
    
    @commands.command()
    async def clear(self, ctx, amount=5):
        try:
            await ctx.channel.purge(limit=amount)
        except Exception as e:
            await ctx.send(f'Error: {e}')
    
    async def on_command_error(self, ctx, error):
        await ctx.send(f'Error: {error}')
    
    async def setup(bot):
        await bot.add_cog(BotCommandes(bot))