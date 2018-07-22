

# -*- coding: utf-8 -*-
"""
Created on Sat May 26 14:21:20 2018

@author: nafis
"""


from audio_record import audio_record as ar
from speech_synthesizer import speech_synthesizer as ss
from audio_recognizer import audio_recognizer as AU
from profiler import profiler as pr

from os import path
import threading


AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "new_file.wav")


def listen():
	m = ar.Audio_record()
	m.record()
	m.writeFile()
	m.readFile()



def reply():
	text = AU.Audio_recognizer(AUDIO_FILE).text()
	print("FROM main ------------> ", text)
	g.reply(text)
#	g.reply("hi")

	return text


if __name__ == "__main__":

	g = ss.speech_syn("Gizmo", "Hi");
	
	data = "";
	while 1:
		listen()

		data = reply()
	#	data = "yes"
		if data == "yes":
			questions_list = pr.Profiler().fetch_questions()
			while 1:
				print(questions_list)
				labelled_str = pr.Profiler().pro_labelling(questions_list[0])
				g.say(labelled_str);
				listen()
				text = AU.Audio_recognizer(AUDIO_FILE).text()
				print(text)



		if data == "bye":
			break;

#    help(AU)

	


#
