from openai import OpenAI



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
