# if it doesn't work follow the instructions, in the file intructions

import discord
from discord.ext import tasks
from mcstatus import MinecraftServer


# here u add the ip of ur server, here is an example
server = MinecraftServer.lookup("wastelands.cc")

client = discord.Client()

# here u put the id of the channels u wana the bot to print the info, (they are only numbers)
servers = [id, id]

# this is a loop that runs each 10 minutes
@tasks.loop(minutes=10)
async def test():

    for val in servers:
        
        channel = client.get_channel(val)
        try:
            status = server.status()
            query = server.query()
            players = query.players.names
            # this will show in the console the number of players
            print("The server has the following players online: {0}".format(", ".join(query.players.names)))

            # the discord msg
            await channel.send("The server is on :thumbsup: :grinning:")
            await channel.send("It has {0} players. All the players online are: {1}".format(status.players.online, ", ".join(players)))

        except:
            # the discord msg
            await channel.send("the server is not on :disappointed_relieved:")
    

@client.event
async def on_ready():
    test.start()


#here u will add ur discord bot private token
client.run("TOKEN")




