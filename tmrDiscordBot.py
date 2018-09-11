from discord.ext.commands import Bot
from discord.ext import commands
import datetime, asyncio, discord

TOKEN = "NDg4Nzc4MzU1NDUwMzE0NzUz.DnhJ-w.GxjOCnyQvJhILyYouLc_ebq5Jo8"

bot = commands.Bot(command_prefix = '.',
                   case_insensitive = True)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	print(discord.utils.oauth_url(bot.user.id))


@bot.event
async def on_member_join(member):
	WelcomeChannel = bot.get_channel(469488895449366530)
	await welcomeChannel.send_message("Welcome to Terminal Manager Remote. " + member.mention)

@commands.has_permissions(administrator=True)
@bot.command()
async def prune(ctx, pruneCount):
    messages = []
    number = int(pruneCount) + 1
    async for index in ctx.history(limit = number):
        messages.append(index)
    await ctx.message.channel.delete_messages(messages)
    await ctx.send('Pruned {} messages'.format(number), delete_after = 5)


@bot.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, user:discord.Member, *, reason:str = None):
    if reason is None:
        reason = "The ban hammer has spoken!"
        try:
            await user.kick(reason = reason)
            await ctx.send('Kicked user {} with ID {}'.format(user, user.id))
        except:
            await ctx.send('Could not kick user {} with ID {}'.format(user, user.id))

@bot.command()
async def ban(ctx, user:discord.Member):
    try:
        user = user.id
    except:
        pass
    await ctx.message.guild.ban(discord.Object(id=int(user)))
    await ctx.send('Banned user with ID: {}'.format(user))

@bot.command(hidden = True)
@commands.has_permissions(administrator=True)
async def setname(ctx, *, name):
	try:
		await bot.edit_profile(username=name)
		await ctx.send('Changed username to `{}`'.format(name))
	except:
		await ctx.send("Failed to change username")



@bot.command(hidden = True)
@commands.has_permissions(administrator = True)
async def LogOut(ctx):
    try:
        await ctx.send('Logging out bot!')
        await bot.close()
    except :
        pass

@bot.command()
@commands.has_permissions(administrator=True)
async def setgame(ctx, *, gameName):
    game = discord.Game(gameName)
    await bot.change_presence(status=discord.Status.idle, activity=game)
    await ctx.send('Changed game to `{}`'.format(gameName))


@bot.command(hidden=True)
@commands.has_permissions(administrator=True)
async def announce(ctx, *, announcement):
	now = datetime.datetime.now().isoformat(' ', 'seconds')
	channel = discord.utils.get(ctx.message.guild.channels, name = 'announcements')
	await channel.send("@everyone " + now +":\n"+announcement)

@bot.command(hidden = True)
@commands.has_permissions(administrator = True)
async def announce_notag(ctx, *, announcement):
    now = datetime.datetime.now().isoformat(' ','seconds')
    channel = discord.utils.get(ctx.message.guild.channels, name = 'announcements')
    await channel.send(str(now + ":\n"+announcement))

bot.run(str(TOKEN))
