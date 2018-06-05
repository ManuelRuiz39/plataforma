# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer



def platica(formulario):
    bot = ChatBot("Yocasta")
    bot_input = bot.get_response(formulario)
    print(bot_input)

    return str (bot_input)
