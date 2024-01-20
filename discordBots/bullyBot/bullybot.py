import tokens as Token
import discord as discord
import chatController as chat

async def bullyRelpy(message):
    str: response = chat.bullyThemText(message.author,message.content)
    try:
        await message.channel.send(response)
        print(f"message responsed in {message.channel}")
    except Exception as e :
        print(e)


def run(str:token):
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
        
        print(f"{message.author} sent: '{message.content}' in {message.channel}")
        inputstr = message.content

        await bullyRelpy(message)
        
    client.run(token)

def main():
    run(Token.getBotToken())
 

if (__name__ == '__main__'):
    main()
