#!/usr/bin/env python
# mum can you please pick me up from school? why not? but mum!! i'm coding: utf8

"""
	This is all thanks to scapy, specifically the file "config.py", where I 
	learned if \001 and \002 surround an ansi escape, it doesn't go all wierd
	when your typing wraps.

	(know what i mean? like try doing this without the \001 and \002 wraps, then
	trying to type big long commands in python, with a narrow terminal)

	1 december 2015
	@reptar_xl
	github.com/raincoats
"""


def ps1_colour(colour):
    ansi = "\033[38;5;"+str(colour)+"m"
    return "\001"+ansi+"\002"

def ps1_reset():
    return "\001"+"\033[0m"+"\002"

# this is just for the prompt but you can use it anywhere
def hostname():
	import platform
	return platform.node()	

def python_ps1():
    prompt = ""
    prompt += ps1_colour(198)
    prompt += "["
    prompt += ps1_colour(73)
    prompt += hostname()
    prompt += ps1_colour(198)
    prompt += "]"
    prompt += ps1_colour(30)
    prompt += '--'
    prompt += ps1_colour(96)
    prompt += '> '
    prompt += ps1_reset()
    return prompt


if __name__ == "__main__":
	from butts import debuggo,stdout
	debuggo("this is what your ps1 could look like:")
	stdout("\n"+python_ps1()+"\n")
	debuggo("to use, put this in your ~/.pythonrc or whatever:")
	stdout("")
	stdout("import sys")
	stdout("import butts.ps1")
	stdout("sys.ps1 = butts.ps1.python_ps1()")
	stdout("")
	debuggo("(that should hopefully work? idk)")

