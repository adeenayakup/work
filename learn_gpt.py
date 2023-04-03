import openai
import os
from IPython.display import display, Markdown

openai.api_key = "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"

system_intel = "You are GPT-4, answer my questions as if you were an expert in the field."
prompt = "5岁女孩生日会玩什么"

# Function that calls the GPT-4 API
def ask_GPT4(system_intel, prompt): 
    result = openai.ChatCompletion.create(model="gpt-4",
                                 messages=[{"role": "system", "content": system_intel},
                                           {"role": "user", "content": prompt}])
    print(Markdown(result['choices'][0]['message']['content']))

# Call the function above
ask_GPT4(system_intel, prompt)