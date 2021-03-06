#!/usr/bin/env python
# you know what i hate? when i'm coding: utf8

import sys
import types
import errno
import os
import datetime
from re import match

cli_rst = "\033[0m"         # reset colours
cli_red = "\033[38;5;124m"  # red
cli_grn = "\033[38;5;034m"  # green
cli_blu = "\033[38;5;039m"  # blue
cli_yel = "\033[38;5;214m"  # yellow
cli_gry = "\033[38;5;240m"  # gray
# brighter colours for XL messages
cli_rxl = "\033[38;5;196m"  # bright red
cli_gxl = "\033[38;5;046m"  # bright green
cli_bxl = "\033[38;5;045m"  # bright blue
cli_yxl = "\033[38;5;220m"  # bright yellow

# for class dumps
cli_classdump_key = "\033[38;5;097m"
cli_classdump_val = "\033[38;5;103m"


def _print_message(message, colour=cli_blu, full_colour=False, stdout=False, eol="\n", prefix='+', die=False):
	if full_colour:
		output = '%s[%s] %s%s%s' % (colour, prefix, message, cli_rst, eol)
	else:
		output = '%s[%s]%s %s%s' % (colour, prefix, cli_rst, message, eol)
	if stdout:
		stdout(output)
	else:
		stderr(output)
	if die:
		sys.exit(die) if type(die) is int else sys.exit(1)

def stderr(message):
	sys.stderr.write(message)
	sys.stderr.flush()

def stdout(message):
	sys.stdout.write(message)
	sys.stdout.flush()

def error(message, prefix='!', eol="\n", die=False):
	_print_message(message, colour=cli_red, prefix=prefix, die=die, eol=eol)

def error_XL(message, prefix='!', eol="\n", die=False):
	_print_message(message, colour=cli_rxl, prefix=prefix, die=die, eol=eol, full_colour=True)

def good(message, prefix='$', eol="\n"):
	_print_message(message, colour=cli_grn, prefix=prefix, eol=eol)

def good_XL(message, prefix='$', eol="\n"):
	_print_message(message, colour=cli_gxl, prefix=prefix, eol=eol, full_colour=True)

def warn(message, prefix='!', eol="\n"):
	_print_message(message, colour=cli_yel, prefix=prefix, eol=eol)

def warn_XL(message, prefix='!', eol="\n"):
	_print_message(message, colour=cli_yxl, prefix=prefix, eol=eol, full_colour=True)

def debuggo(message, prefix='+', eol="\n"):
	_print_message(message, colour=cli_blu, prefix=prefix, eol=eol)

def debuggo_XL(message, prefix='+', eol="\n"):
	_print_message(message, colour=cli_bxl, prefix=prefix, eol=eol, full_colour=True)


# gives you the time like [17/12/15 16:08]
def logtime(colour=False):
	format_string = "[%d/%m/%y %T]" if colour==False else (cli_gry+"[%d/%m/%y %T]"+cli_rst)
	return datetime.datetime.now().strftime(format_string)


# if it's a list we put all the values together with a ": ", like if you had:
#   ["./program.py", "inputfile", "permission denied"],
# it would come out like:
#   ./program.py: inputfile: permission denied
def _array_join(message):
	if not isinstance(message, types.StringTypes):
		try:
			message = ': '.join(str(message))   # stackoverflow/questions/7221404/
		except TypeError:
			pass
	# if it's just a string, then return it as it was
	return str(message)

def posix_error(e):
	# returns stuff like "EACCES: Permission denied"
	# http://stackoverflow.com/questions/7841573/
	return '%s: %s' % (errno.errorcode[e], os.strerror(e))

def my_pain(message, e=1):
	# just a normal error function really, with an added exit value thing,
	# and this one supports error arrays (see _array_join)
	error(_array_join(message))
	sys.exit(e)

# ------------------------------------------------------------------------------

# format the dir() function & remove all the weird __things__ __like__ __this__
def dir_XL(obj_thing):

	# we're making a nice formatted thing, so we need to know
	# the length of the longest member, to get everything
	# nicely aligned
	longest = 0 #for now
	dir_things = []

	for i in dir(obj_thing):
		if not match('^_', i):
			dir_things.append(i)
			longest = len(i) if (len(i) > longest) else longest

	# assume an 80 char wide term
	# TODO: use get_tty_size() to make nice cols
	width = 80
	rows  = 24

	# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit
	if longest < 37:
		for i in range(0, len(dir_things), 2):
			try:
	# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit
				print format("| %-36s | %-36s |" % (dir_things[i], 
							                          dir_things[i+1]))
					# this is the laziest shit
			except IndexError:
				#ARE YOU FUCKING READY FOR THIS
				pass
					# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit
	# this is the laziest shit

	else:
		for i in dir_things:
			print format("| %-80s |" % i)

			# omfg am i serious right now



# ------------------------------------------------------------------------------

def get_tty_size():
	# http://stackoverflow.com/questions/566746/
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])


def classdump(classs):
	# format and print the output of dir(some_class)
	from pprint import pprint
	from inspect import getmembers
	from re import match
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
		# get rid of keys like __whatever__,
		# and vals like <stupid thing at 0xf38fae3e>
		if not match('__$', i):# or match('^<.*>$', i):
			sys.stderr.write(
				format("%s[class] %20s:%s %s%s%s\n" % (
					cli_classdump_key, i, cli_rst,
					cli_classdump_val, format_string[i], cli_rst
				))
			)
			sys.stderr.flush()


def test():
	debuggo_XL('Testing formatting functions:')
	stderr     ('stderr')
	stdout     ('stdout')
	error      ('error')
	error_XL   ('error_XL')
	good       ('good')
	good_XL    ('good_XL')
	warn       ('warn')
	warn_XL    ('warn_XL')
	debuggo    ('debuggo')
	debuggo_XL ('debuggo_XL')


if __name__ == "__main__":
	print "\033[38;2;255;029;0m _"
	print "\033[38;2;255;059;0m| |"
	print "\033[38;2;255;088;0m| |        _|__|_  ,"
	print "\033[38;2;255;118;0m|/ \_|   |  |  |  / \_"
	print "\033[38;2;255;148;0m \_/  \_/|_/|_/|_/ \/\033[38;2;255;168;0m.py"
	print "\033[0m"
	test()