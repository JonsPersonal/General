import tokens as Token
import discord
import chatController as chat

async def bullyRelpy(message):
    response = chat.bullyThemText(f"{message.author}",f"{message.content}", Token.getChatgptToken())
    try:
        await message.reply(response)
        print(f"message responsed in {message.channel}")
    except Exception as e :
        print(e)


def run():
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

        await bullyRelpy(message)
        
    client.run(Token.getBotToken())

def main():
    run()
 

if (__name__ == '__main__'):
    main()
