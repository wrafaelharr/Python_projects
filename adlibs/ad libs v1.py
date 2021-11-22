import pyttsx3
from nltk.corpus import wordnet as wn

#make speaking engine
engine = pyttsx3.init()

#find list of words
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}

#ad those libs
if "cook" in nouns:
    #say text
    engine.say("cook is a noun")
    engine.runAndWait()