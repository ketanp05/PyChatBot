"""
PyChatBot: A simple chatbot using Python's NLTK library.

This script leverages the nltk.chat module to create a responsive chatbot that engages users
with hardcoded responses based on regular expressions matching. The chatbot uses reflections to
handle simple conversational transformations, enhancing the interaction experience.
"""

from nltk.chat.util import Chat, reflections

# Pairing patterns with responses
pairs = [
    [r"my name is (.*)", ["Hello %1, how are you today?"]],
    [r"what is your name\?", ["My name is PyChatBot and I'm a chatbot."]],
    [r"how are you\?", ["I'm doing good\nHow about you?"]],
    [r"sorry (.*)", ["It's alright!", "It's OK, never mind."]],
    [r"hi|hey|hello", ["Hello", "Hey there!"]],
    [r"(.*) age\?", ["I'm a computer program, I don't have an age."]],
    [r"what (.*) want\?", ["Make me an offer I can't refuse."]],
    [r"(.*) created\?", ["I was created by Ketan using Python's NLTK library."]],
    [r"(.*) (location|city)\?", ["I'm based in Pune, Maharashtra."]],
    [r"how is the weather in (.*)\?", ["The weather in %1 is pleasant."]],
    [r"i work in (.*)\?", ["%1 sounds like a great place to work!"]],
    [r"quit", ["Bye, take care. See you soon!", "It was nice talking to you. See you soon!"]],
]

def chatty():
    print("Hi, I'm Chatty and I chat a lot ;)\nPlease type in lowercase English to start a conversation. Type 'quit' to leave.")
    chat = Chat(pairs, reflections)
    chat.converse()

def main():
    chatty()

if __name__ == "__main__":
    main()
