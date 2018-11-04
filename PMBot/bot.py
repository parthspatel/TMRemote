import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import server, text

bot = commands.Bot(command_prefix='.', case_insensitive=True)
serverObj = None
serverInvites = ["RJcZbv"]

sentMessage = []

@bot.event
async def on_ready():
    global serverObj
    serverObj = server.Server(text.TOKEN)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    embed = discord.Embed(title="About Us", colour=discord.Colour(0xb5d109), url="https://beta.tmremote.io", description=\
	"We are TMRemote, a remote bot management service for Terminal enabling our customers to manage bots over a simplified web service.\
	\n\nSome of the services that we offer are:\n - monitoring\n - ban detection (similar to gm detect by Blight Trainer)\n - remote logout\
	\n\nWe are in the process of implementing all the features of terminal so that you can fully manage all your bots from TMRemote.\n\
	\nWith this most recent patch 11/1/2018 Terminal was being detected by MapleStory.  With TMRemote you can crash all of the bots from any \
	internet browser and not have to worry about the integrity of your bots.\n\nPlease check us out at https://beta.tmremote.io/ for a \
	more user-friendly bot management solution and peace of mind.\nYou can also join our discord: https://discord.gg/N5Tpgtt")
    embed.set_author(name="TMRemote", url="https://beta.tmremote.io", icon_url="https://beta.tmremote.io/assets/img/logo-no-text.png")
    print("Joining all inputted server invites...")
    for invite in serverInvites:
        try:
            serverObj.join_server(invite, None)
        except Exception as E:
            print(E)
    print("Joined all servers...")
    print("Starting iterations...")
    for guild in bot.guilds:
        for member in guild.members:
            if member.id in sentMessage:
                print(f"Already PM'd {member.name}")
                continue
            try:
                await member.send(embed=embed)
                print(f"Sent message to {member.name}")
                sentMessage.append(member.id)
            except Exception as E:
                if 'cannot send messages to this user' in str(E).lower():
                    print(f"Cannot PM {member.name}, {E}")
            await asyncio.sleep(5)
    print("Finished iterations...")

@bot.command()
async def logOut(ctx):
    if not ctx.message.author.id == 321354072865112074:
        return
    with open('sentMessage.txt', 'w+') as file:
        file.seek(0)
        file.truncate()
        for userID in sentMessage:
            file.write(f'{userID}\n')
    await bot.logout()

with open('sentMessage.txt', 'r+') as file:
    content = file.readlines()
for line in content:
    sentMessage.append(int(line))

bot.run(text.TOKEN, bot = False)

