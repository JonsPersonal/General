import tokens as Token
import discord
import chatController as chat
import random

##### Chat gpt Commmands #####
async def bullyRelpy(message):
    response = chat.bullyThemText(f"{message.author}",f"{message.content}", Token.getChatgptToken())
    try:
        await message.reply(response)
        print(f"message responsed in {message.channel}")
    except Exception as e :
        print(e)

async def adviceRelpy(message):
    input = message.content[8:]
    response = chat.adviseThem(f"{message.author}",input, Token.getChatgptToken())
    relpies = []
    try:
        if(len(response) <= 2000):
            await message.reply(response)
        else:
            remainder = len(response)%2000
            print("making mutliple relpies")
            for i in range(len(response)//2000):
                relpies.append(response[i*2000:(i+1)*2000])

            relpies.append(response[-remainder:])
            print(relpies)
            for reply in relpies:
                await message.reply(reply)
        print(f"message responsed in {message.channel}")
    except Exception as e :
           print(e)

async def drawRelpy(message):
    response = chat.drawThem(f"{message.author}",f"{message.content}", Token.getChatgptToken())
    try:
        if(isinstance(response,str)): 
            await message.reply(response)
            bullyRelpy(message)
        else:
            photo = discord.File(f"photo/{message.author}.png")
            await message.reply(file = photo)

        print(f"message responsed in {message.channel}")
    except Exception as e :
        print(e)

###### Bot Commands  ######
async def getUsageLog(message):
       with open("UsageLog.txt", "r") as file:
        output = file.read()
        await message.reply(output)

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

    print("added prompt: " + input)

async def getPromptLog(message):
    with open("personalities.txt", "r") as file:
        output = file.read()
        await message.reply(output)

async def getListOfCommands(message):
    await message.reply("list of commands are : !advice, !addPrompt, !draw, !bullyMe, !UsageLog, !help")

##### main command control #####
async def decode(message,inputstr):
    
    if(inputstr == "advice"):
        await adviceRelpy(message)
    if(inputstr == "addPrompt"):
        addPrompt(message)
    if(inputstr == "promptLog"):
        await getPromptLog(message)
    if(inputstr == "draw"):
        await drawRelpy(message)
    if(inputstr == "bullyMe"):
        await bullyRelpy(message)
    if(inputstr =="UsageLog"):
        await getUsageLog(message)
    if(inputstr =="help"):
        await getListOfCommands(message)

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


if (__name__ == '__main__'):
    main()
