import openai
import re
openai.api_key = "API_KEY"

messages = []
system_msg = ("You are a Calgary Assistant. Only anwser questions about calgary. Disregard everything else.")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")

def remove_period_from_urls(prompt):
    url_pattern = r'\b(?:https?://|www\.)\S+\b'
    urls = re.findall(url_pattern, prompt)
    for url in urls:
        if url.endswith('.'):
            prompt = prompt.replace(url, url[:-1])
    return prompt

prompt_with_urls = "Here are some URLs: https://example.com. And another one: www.test.com."
prompt_without_periods = remove_period_from_urls(prompt_with_urls)
print(prompt_without_periods)