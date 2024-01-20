from openai import OpenAI



def bullyThemText(user, message,token):
    
    content = "in less than 2000 characters roast the following user in the style of an extremely aggressive gamer who reallly hates everyone that isn't them:\" "+user+" \" for sending the message:\""+message
    client = OpenAI(
    # This is the default and can be omitted
    api_key=token
    )
    response = client.chat.completions.create(
    messages=[
            {
                "role": "user",
                "content": content,
            }
        ], model="gpt-4",
        )
    print("response from gpt in controller")
    print(response.choices[0].message.content)
    return response.choices[0].message.content
