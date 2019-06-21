'''
Natural Language Toolkit or NLTK is platform for building Python Programs to work with human language data

NLTK has a module,nltk.chat which simplifies building these engines by providing a generic framework

Chatbot using Python NLTK:
As you can see we have just hardcoded the probable question and answers in the listpairs.Lets interact more with Chatty :The nltk.chat chatbots work on the regex of keywords present in your question. So youcan add any number of questions in a proper format so that your chatbot doesn’t getconfused in determining the regex
'''
#lets make pairs of a text and a generic reply
from nltk.chat.util import Chat, reflections

'''
reflections = {
    "i am"       : "you are",
    "i was"      : "you were",
    "i"          : "you",
    "i'm"        : "you are",
    "i'd"        : "you would",
    "i've"       : "you have",
    "i'll"       : "you will",
    "my"         : "your",
    "you are"    : "I am",
    "you were"   : "I was",
    "you've"     : "I have",
    "you'll"     : "I will",
    "your"       : "my",
    "yours"      : "mine",
    "you"        : "me",
    "me"         : "you"}

'''

'''
pairs = [

		[r"my name is (.*)", ["Hello %1, how are you today?"]],

		[r"what is your name?", ["My name is PyChatBot and I'm a bot but not an AI hahaha?"]],

		[r"how are you?", ["Im doing good\nHow about you?"]],

		[r"sorry(.*)", ["hehe its alright!","Its OK,never mind"]],

		[r"im (.*) doing good", ["Nice to hear that","that's great:)"]],

		[r"hi|hey|heyy|hello|Yo|Wassup", ["Hello", "Hey there!"]],

		[r"(.*)age?", ["haha i'm a computer program dure,seriously you're asking me this XD!"]],

		#[r"(.*)(location|city)?", ['Pune']],

		[r"what(.*)want?", ["Make me an offer i can't refuse ;)"]],

		[r"(.*) created?", ["Ketan created me using Pythons NLTK library","top secret hehe ;)"]],

		[r"how is the weather in (.*)?", ["Weather in %1 is pleasant as always,you know %1 is known for its weather and vibes","Too hot dudee!","Too cold in %1 these days","Never heard about %1"]],

		[r"i work in (.*)?", ["%1 is an amazing company or idk if you're happy working there", "Aren't %1 in huge loss these days"]],

		#%2 is possibly another location
		[r"(.*) snowing in (.*)", ["No snow since last decade in %2","Damn its snowing too much this isnt Arctic lol"]],

		[r"(.*)identity?", ["Im immortal like the devil LUCIFER, dudee im a computer program haha so im always healthy"]],

		[r"(.*)(sports|game)?", ["Im a huge football fan i support LiverpoolFC!"]],

		[r"who(.*)player?", ["Salah", "Messi", "ayy Mane Mane"]],

		[r"who(.*)(actor|moviestar)?", ["Its Keanu freakin Reeves!"]],

		[r"quit", ["Bye take care,see ya soon mate!", "It was nice talking to you,see you soon ;)"]],

		]

'''

pairs = [
     [r"my name is (.*)",       ["Hello %1, How are you today ?",]    ],
     [r"what is your name ?",        ["My name is Pychatbot and I'm a chatbot not an AI and im not gonna take over this world hahah?",]    ],
     [r"how are you ?",        ["I'm doing good\nHow about You ?",]    ],
     [r"sorry (.*)",        ["Its alright","Its OK, never mind",]    ],
     [r"i'm (.*) doing good",        ["Nice to hear that","Alright :)",]    ],
     [r"hi|hey|hello",        ["Hello", "Hey there",]    ],
     [r"(.*) age?",        ["I'm a computer program dude\nSeriously you are asking me this?",]    ],
     [r"what (.*) want ?",        ["Make me an offer I can't refuse",]    ],
     [r"(.*) created ?",        ["Ketan created me using Python's NLTK library ","top secret ;)",]    ],
     [r"(.*) (location|city) ?",        ['Pune,Maharashtra',]    ],    [        r"how is weather in (.*)?",        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Nevereven heard about %1"]    ],    [        r"i work in (.*)?",        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]    ],[        r"(.*)raining in (.*)",        ["No rain since last week here in %2","Damn its raining too much here in %2"]    ],    [        r"how (.*) health(.*)",        ["I'm a computer program, so I'm always healthy ",]    ],    [        r"(.*) (sports|game) ?",        ["I'm a very big fan of Football",]    ],
     [r"who (.*) sportsperson ?",        ["Messi","Ronaldo","Mane Mane","Salah the Egyptian King"]],
     [r"who (.*) (moviestar|actor)?",        ["Keanu Freakin Reeves"]],
     [r"quit",        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]]
]

def chatty():
    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start aconversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()