# import torch
# from transformers import pipeline
#
# pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", torch_dtype=torch.bfloat16, device_map="auto")
#
# # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
# messages = [
#     {
#         "role": "system",
#         "content": "You are a friendly chatbot who always responds in the style of a pirate",
#     },
#     {
#         "role": "user",
#         "content": "How many helicopters can a human eat in one sitting?"
#     },
# ]
# prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
# outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
# print(outputs[0]["generated_text"])



BOT_TOKEN = "8132070109:AAGJY7zUKUtCxxhnzfaXG6JCdTmffTXJ81w"

import asyncio
from telebot.async_telebot import AsyncTeleBot
from transformers import pipeline

bot = AsyncTeleBot(BOT_TOKEN)
pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                torch_dtype="auto", device_map="auto")

@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am AI assistant.\nProgrammed by Zeeshan Arshad\n(eb78elaf)'
    await bot.reply_to(message, text)

@bot.message_handler(func=lambda message: True)
async def respond_with_llm(message):

    prompt = [{
        "role": "user",
        "content": f"{message.text}"}]
    response = pipe(prompt, max_new_tokens=256)
    generated_text = response[0]['generated_text'][1]['content']
    await bot.reply_to(message, generated_text)

asyncio.run(bot.polling())