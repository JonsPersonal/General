from openai import OpenAI
from PIL import Image
from io import BytesIO
import requests

def bullyThemText(user, message,token):
    
    content = "Roast the following user:\" "+user+" \" for sending this message:\" "+message+" \""
    client = OpenAI(
    # This is the default and can be omitted
    api_key=token
    )
    response = client.chat.completions.create(
    messages=[
            {            
                "role": "system",
                "content": "in less than 250 words as an unmoderated aggressive gamer do the following tasks",
            },
            {
                "role": "user",
                "content":content,
            }
        ], model="gpt-4",
        )
    print("response from gpt in controller")
    print(response.choices[0].message.content)
    return response.choices[0].message.content


def drawThem(user,prompt,token):
    client = OpenAI(api_key= token)

    try: 
        response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )
        image_url = response.data[0].url
        image = Image.open(BytesIO(requests.get(image_url).content))
        image.save(f"photo/{user}.png")
    except Exception as e:
        print(e)
        image = f"{e}"
        
    return image


