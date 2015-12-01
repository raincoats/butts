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

# put in a number between 0 and 255, recieve the colour code.
def ps1_colour(colour):
    ansi = "\033[38;5;"+str(colour)+"m"
    return "\001"+ansi+"\002"

# normal ansi reset, used to remove the colour effect
def ps1_reset():
    return "\001"+"\033[0m"+"\002"


def create(prompt_phrase, colours = [198, 73, 30, 96] ):
    ps1 = ""
    ps1 += ps1_colour(colours[0])
    ps1 += "["
    ps1 += ps1_colour(colours[1])
    ps1 += prompt_phrase
    ps1 += ps1_colour(colours[0])
    ps1 += "]"
    ps1 += ps1_colour(colours[2])
    ps1 += '--'
    ps1 += ps1_colour(colours[3])
    ps1 += '> '
    ps1 += ps1_reset()
    return ps1


if __name__ == "__main__":
	from butts import debuggo,stdout
	debuggo("this is what your ps1 could look like:")
	stdout("\n"+create()+"\n")
	debuggo("to use, put this in your ~/.pythonrc or whatever:")
	stdout("")
	stdout("import sys")
	stdout("import butts.ps1")
	stdout("sys.ps1 = butts.ps1.create()\n")

