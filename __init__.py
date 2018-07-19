from opsdroid.matchers import match_regex
import logging
import random

from .chatbot import Chatbot

chatbot = Chatbot()

# restart exploration
# chatbot.history = []
# chatbot.goal = []

def setup(opsdroid):
    logging.debug("Loaded ODExploration skill")


@match_regex(r'(.*)')
async def searchOD(opsdroid, config, message):
    request = message.regex.group(1)
    # print(request)
    text = chatbot.search(request)
    print(text)
    await message.respond(text)
