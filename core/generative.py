import openai


from config import SECRET_KEY

openai.api_key = "SECRET_KEY"


def chat(prompt: str) -> str:
    messages = [
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
    )

    response_message = response["choices"][0]["message"]

    print(response_message)
