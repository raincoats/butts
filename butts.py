#!/usr/bin/env python
# you know what i hate? when i'm coding: utf8

import sys
import types
import errno
import os

# reset colours
cli_rst = "\033[0m"

cli_red = "\033[38;5;124m"
cli_grn = "\033[38;5;034m"
cli_blu = "\033[38;5;039m"

# brighter colours for XL messages
cli_rxl = "\033[38;5;196m"
cli_gxl = "\033[38;5;046m"
cli_bxl = "\033[38;5;045m"

# for class dumps
cli_classdump_key = "\033[38;5;097m"
cli_classdump_val = "\033[38;5;103m"



def stderr(message):
	sys.stderr.write(message+"\n")
	sys.stderr.flush()

def stdout(message):
	sys.stdout.write(message+"\n")
	sys.stdout.flush()

def error(message):
	message = array_to_string(message)
	sys.stderr.write(cli_red+'[!] '+cli_rst+message+"\n")
	sys.stderr.flush()

def error_XL(message):
	message = array_to_string(message)
	sys.stderr.write(cli_rxl+'[!] '+message+cli_rst+"\n")
	sys.stderr.flush()

def good(message):
	sys.stdout.write(cli_grn+'[$] '+cli_rst+message+"\n")
	sys.stdout.flush()

def good_XL(message):
	sys.stdout.write(cli_gxl+'[$] '+message+cli_rst+"\n")
	sys.stdout.flush()

def debuggo(message):
	message = array_to_string(message)
	sys.stderr.write(cli_blu+'[+] '+cli_rst+message+"\n")
	sys.stderr.flush()

def debuggo_XL(message):
	# extra blue for extra important messages
	sys.stderr.write(cli_bxl+'[+] '+message+cli_rst+"\n")
	sys.stderr.flush()

def array_to_string(message):
	# if it's a list we put all the values together with a ": ", like if you had:
	#   ["./program.py", "inputfile", "permission denied"],
	# it would come out like:
	#   ./program.py: inputfile: permission denied
	if not isinstance(message, types.StringTypes):
		message = ': '.join(message)   # http://stackoverflow.com/questions/7221404/
	# if it's just a string, then return it as it was
	return message

def posix_error(e):
	# returns stuff like "EACCES: Permission denied"
	# http://stackoverflow.com/questions/7841573/
	return '%s: %s' % (errno.errorcode[e], os.strerror(e))

def my_pain(message, e=1):
	# just a normal error function really, with an added exit value thing,
	# and this one supports error arrays (see array_to_string)
	error(array_to_string(message))
	sys.exit(e)




def classdump(classs):
	# format and print the output of dir(some_class)
	from pprint import pprint
	from inspect import getmembers
	classbits = getmembers(classs)
	#pprint(getmembers(classs))
	format_string = {}
	key = ''
	val = ''

	for i in range(0, len(classbits)):
		# get the key
		key = str(classbits[i][0])

		for o in range(1, len(classbits[i])):
			# get the key's values
			val = str(classbits[i][o])

		format_string[key] = val
	
	for i in format_string:
		sys.stderr.write(
			format("%s[class] %20s:%s %s%s%s\n" % (
				cli_classdump_key, i, cli_rst,
				cli_classdump_val, format_string[i], cli_rst
			))
		)
		sys.stderr.flush()





# http://stackoverflow.com/questions/5226958/
def which(file):
	for path in os.environ["PATH"].split(os.pathsep):
		if os.path.exists(os.path.join(path, file)):
			return os.path.join(path, file)
	return False


if __name__ == "__main__":
	debuggo_XL('Testing formatting functions:')
	stderr     ('stderr')
	stdout     ('stdout')
	error      ('error')
	error_XL   ('error_XL')
	good       ('good')
	good_XL    ('good_XL')
	debuggo    ('debuggo')
	debuggo_XL ('debuggo_XL')
