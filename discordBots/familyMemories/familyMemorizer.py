#this bot saves sent images to the store them in the jellyfin server
import discord
import tokens as Token
import uuid
def saveHist():
    return

def main():
    print("booting up the bully bot!")
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
         
        if (message.attachments ):

            print(f'yes photo')
            imageName = f"{message.author}."+str(uuid.uuid4()) + '.jpg'
            await message.attachments[0].save(imageName)
        print(f"{message.author} sent: '{message.content}' in {message.channel}")

        inputstr = message.content
        if inputstr == '':
            return
        if(inputstr[0]=="!"):
            if inputstr=="!saveHist":
                saveHist()
        else:
            return


    client.run(Token.getBotToken())


if (__name__ == '__main__'):
    main()
