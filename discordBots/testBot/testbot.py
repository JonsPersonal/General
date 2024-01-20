import discord
import 

async def sendPhoto(message):
    try:
        await message.channel.send("sending photos now")
  
        for i in range(10,470):
            photo = discord.File(f"C:/general/discordBots/testBot/photos/GregUk {i}.png")
            await message.channel.send(file = photo)

        print(f"sent photos to {message.channel}")
    except Exception as e :
        print(e)





async def decodeCommand(message,command:str):

    if(command == "sendPhotos"):
        await sendPhoto(message)
    if(command == "bullyTim"):
        await bullyTim(message)

def run(TOKEN):



    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"i'm alive {client.user}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        print(f"{message.author} sent: '{message.content}' in {message.channel}")
        inputstr = message.content
        if(inputstr[0]=="!"):
            await decodeCommand(message,inputstr[1:])
        else:
            return
        
    client.run(TOKEN)



def bullyTim():
