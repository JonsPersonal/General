import tokens as Token
import discord
import chatController as chat
import random

async def bullyRelpy(message):
    response = chat.bullyThemText(f"{message.author}",f"{message.content}", Token.getChatgptToken())
    try:
        await message.reply(response)
        print(f"message responsed in {message.channel}")
    except Exception as e :
        print(e)

async def adviceRelpy(message):
    input = message.content[1:]
    response = chat.adviseThem(f"{message.author}",input, Token.getChatgptToken())
    try:
        await message.reply(response)
        print(f"message responsed in {message.channel}")
    except Exception as e :
           print(e)

async def drawRelpy(message):
    response = chat.drawThem(f"{message.author}",f"{message.content}", Token.getChatgptToken())
    try:
        if(response == type.__str__): 
            await message.reply(response)
        else:
            photo = discord.File(f"photo/{message.author}.png")
            await message.reply(file = photo)

        print(f"message responsed in {message.channel}")
    except Exception as e :
        print(e)

def addPrompt(message):
    input = message.content[11:]
    
    with open("personalities.txt","r") as file:
        lines = file.readlines()
        amountOfPrompts = int(lines[0])
        amountOfPrompts = amountOfPrompts +1
        lines[0] = f"{amountOfPrompts}\n"
    
        with open("personalities.txt","w") as file:
            file.writelines(lines)
    with open("personalities.txt","a") as file:
        file.write(f"{input}\n")


def getPromptLog(message):
    
    with open("personalities.txt", "r") as file:
        output = file.read()
        message.reply(output)
        
## main command control 
async def decode(message,inputstr):
    
    if(inputstr == "advice"):
        await adviceRelpy(message)
    if(inputstr == "addPrompt"):
        addPrompt(message)
    if(inputstr == "promptLog"):
        getPromptLog(message)
    if(inputstr == "draw"):
        await drawRelpy(message)
    if(inputstr == "bullyMe"):
        await bullyRelpy(message)

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
            tester = random.randint(1,10)
            print(f"responds if 1 rolled a: {tester}")
            if(tester == 1):
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
