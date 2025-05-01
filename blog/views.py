from django.shortcuts import render
from django.http import HttpResponse

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot(
    "AIchatbox",
    read_only=False,
    logic_adapters=[{"import_path": "chatterbot.logic.BestMatch"}],
)
# Note: This list is short but in real life it may have a lot of data. And it will take more time.
list_to_train = [
    "Hi",
    "Hello",
    "How are you?",
    "I am fine, thank you.",
    "What is your name?",
    "My name is AIchatbox.",
    "What can you do?",
    "I can chat with you.",
    "Tell me a joke.",
    "Why did the chicken cross the road? To get to the other side.",
    "What is your favorite color?",
    "I like all colors.",
]
chatterBotCorpusTrainer = ChatterBotCorpusTrainer(bot).train(
    "chatterbot.corpus.english"
)
# list_trainer = ListTrainer(bot)
# list_trainer.train(list_to_train)


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def specific(request):
    return HttpResponse("specific URL")


def getResponse(request):
    userMessage = request.GET.get("userMessage")
    # bot.get_response(userMessage) will return a response object, so we need to get the text from it
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)
