from openai import OpenAI



def bullyThemText(user, message,token):
    print(f" {user} {message} {token}")
    content = "tease the following user:\""+user+"\" for sending the message:\""+message
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
        ], model="gpt-3.5-turbo",
        )
    print("response from gpt in controller")
    print(response.choices[0].message.content)
    return response.choices[0].message.content
