from openai import OpenAI
from PIL import Image
from io import BytesIO
import requests
import random
import re

def logUse(user: str, type: str):
    # Initialize count outside of the loop
    count = 0
    
    with open("UsageLog.txt", "r") as file:
        lines = file.readlines()

        # Iterate over the lines to find the user
        for line in lines:
            if re.search(pattern=user, string=line):
                break  # Break the loop if the user is found
            count += 1

    with open("UsageLog.txt", "r") as file:
        lines = file.readlines()

        # If the user is found, update the corresponding line
        if count < len(lines):
            newLine = lines[count]

            pattern = r'\d+'
            integers = re.findall(pattern, newLine)
            bullied = int(integers[0])
            advised = int(integers[1])
            drew = int(integers[2])

            if type == "bullied":
                bullied += 1
            elif type == "advised":
                advised += 1
            elif type == "drew":
                drew += 1

            newLine = f"{user} bullied: {bullied}, advised: {advised}, drew: {drew}\n"
            print("Updated usage log with: " + newLine)
            lines[count] = newLine

        else:
            # If the user is not found, add a new line
            if type == "bullied":
                newLine = f"{user} bullied: 1, advised: 0, drew: 0\n"
            elif type == "advised":
                newLine = f"{user} bullied: 0, advised: 1, drew: 0\n"
            elif type == "drew":
                newLine = f"{user} bullied: 0, advised: 0, drew: 1\n"

            print("Added to usage log: " + newLine)
            lines.append(newLine)

    # Write the modified lines back to the file
    with open("UsageLog.txt", "w") as file:
        file.writelines(lines)

def getPersonality() -> str:
    with open("personalities.txt", "r") as file:
        lines = file.readlines()
        amountOfPrompts = int(lines[0])
        selector = random.randint(1,amountOfPrompts)
    
        print(f"selector rolled : {selector} personality: " + lines[selector])
        return lines[selector]
        
def bullyThemText(user, message,token):
    logUse(user,"bullied")
    content = "Roast the following user:\" "+user+" \" for sending this message:\" "+message+" \""
    client = OpenAI(
    # This is the default and can be omitted
    api_key=token
    )
    response = client.chat.completions.create(
    messages=[
            {            
                "role": "system",
                "content": f"in less than 250 words your name is bullyBot and your personality is {getPersonality()} do the following ",
            },
            {
                "role": "user",
                "content":content,
            }
        ], model="gpt-4",
        )
    print("response of bul gpt in controller")
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def drawThem(user,prompt,token):
    client = OpenAI(api_key= token)
    print("drawing...")
    try: 
        response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        logUse(user,"drew")
        image_url = response.data[0].url
        image = Image.open(BytesIO(requests.get(image_url).content))
        image.save(f"photo/{user}.png")
    except Exception as e:
        print(e)
        image = f"{e}"
        
    return image

def adviseThem(user, message,token):
    logUse(user,"advised")
    client = OpenAI(
    # This is the default and can be omitted
    api_key=token
    )
    response = client.chat.completions.create(
    messages=[
            {            
                "role": "system",
                "content": f"assist {user}",
            },
            {
                "role": "user",
                "content":message,
            }
        ], model="gpt-4",
        )
    print("response of advice from gpt in controller")
    print(response.choices[0].message.content)
    return response.choices[0].message.content