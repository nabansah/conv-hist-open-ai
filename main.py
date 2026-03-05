import os
from openai import OpenAI
# from dotenv import load_dotenv
import openai

# load your key from environment instead of hardcoding it
# load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Hello, World!")

conversation = []

def chat_with_ai(user_message):
    conversation.append(
                {"role": "user", "content": user_message}            
            )    

    response =  client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."}
            ] + conversation
    )  

    ai_answer = response.choices[0].message.content

    conversation.append(
                {"role": "assistant", "content": ai_answer}            
            )
    
    return ai_answer


print(chat_with_ai("what are the symptoms of heart attack"))   
print("-----")
print(chat_with_ai("what are the suggested mediacations"))   
print("-----")
print(chat_with_ai("please summarize what we just talked"))  
print("-----")




