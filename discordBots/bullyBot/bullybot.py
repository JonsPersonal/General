import tokens as Token
import discord
import chatController as chat
import random

async def bullyRelpy(message):

    tester = random.randint(0,10)
    print(f"responds if 1 rolled a: {tester}")
    if(tester == 1):
        response = chat.bullyThemText(f"{message.author}",f"{message.content}", Token.getChatgptToken())
        try:
            await message.reply(response)
            print(f"message responsed in {message.channel}")
        except Exception as e :
           print(e)

async def adviceRelpy(message):
    input = message.content.split()[1:]
    response = chat.adviseThem(f"{message.author}",input, Token.getChatgptToken())
    try:
        await message.reply(response)
        print(f"message responsed in {message.channel}")
    except Exception as e :
           print(e)

async def drawRelpy(message):
    response = chat.drawThem(f"{message.author}",f"{message.content}", Token.getChatgptToken())


async def decode(message,inputstr):
    if(inputstr == "advice"):
        ##await adviceRelpy(message)
        print("worked")
    if(inputstr == "draw"):
        ##await drawRelpy(message)
        print("draw worked")
        
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
        if(f"{message.channel}" == 'cancerous-content'):
            await bullyRelpy(message)
        inputstr = message.content
        if(inputstr[0]=="!"):
            command = inputstr[1:].split()[0]
            await decode(message,command)
    client.run(Token.getBotToken())

def main():
    run()
 

if (__name__ == '__main__'):
    main()
