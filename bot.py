import telebot
import openai
openai.api_key = "ur gpt token" 
Token = "ur tg token"
bot = telebot.TeleBot(Token)
@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "Hello")
@bot.message_handler(content_types=["text"])
def chat(message):
    try:
        user_input = message.text
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=150
    )
        gpt_response = response.choices[0].message['content'].strip()
        bot.send_message(message.chat.id, gpt_response)
    except openai.error.RateLimitError:
        bot.send_message(message.chat.id, "Превышена квота использования API. Пожалуйста, повторите попытку позже.")
    except openai.error.OpenAIError as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")
bot.polling(none_stop=True)