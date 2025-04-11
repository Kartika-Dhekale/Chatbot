import nltk
import random
import string
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Sample patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name\??",
        ["I'm a chatbot created with NLTK.", "You can call me ChatNLTK."]
    ],
    [
        r"how are you\??",
        ["I'm just a bunch of code, but I'm running smoothly!", "I'm great, thanks!"]
    ],
    [
        r"(.*)(help|support)(.*)",
        ["I'm here to help! Tell me more.", "What do you need assistance with?"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Take care!"]
    ],
    [
        r"(.*)",
        ["Tell me more about that.", "Why do you say that?", "Interesting... go on."]
    ]
]

# Chat class using NLTK's built-in reflections
chatbot = Chat(pairs, reflections)

# Simple chatbot runner
def start_chat():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ['bye', 'exit', 'quit']:
            print("Chatbot: Goodbye! 👋")
            break
        print("Chatbot:", chatbot.respond(user_input))

if __name__ == "__main__":
    start_chat()
