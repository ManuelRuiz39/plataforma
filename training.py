# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer



def entrena():
     bot = ChatBot("Yocasta")
     bot.set_trainer(ChatterBotCorpusTrainer)
     bot.train("./plantilla/saludo.yml", "./plantilla/yocasta.yml","./plantilla/drp.yml","./plantilla/general.yml","./plantilla/nube.yml")



entrena()

