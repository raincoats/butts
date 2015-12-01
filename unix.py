#!/usr/bin/env python
# loading, roading, toading and coding: utf8

"""
	these are just functions that act like unix commands

	1 december 2015
	@reptar_xl
	github.com/raincoats
"""

# returns the name of the computer it's running on
# http://stackoverflow.com/questions/4271740
def hostname():
	import platform
	return platform.node()	

# returns the full path of whatever program, provided it's in $PATH
# http://stackoverflow.com/questions/5226958/
def which(file):
	for path in os.environ["PATH"].split(os.pathsep):
		if os.path.exists(os.path.join(path, file)):
			return os.path.join(path, file)
	return False


# --------------------------------------------------------------------
# okay so this one isn't actually a unix command but it's handy
# http://stackoverflow.com/questions/566746/
def get_tty_size(cols=True, rows=True):
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
    if cols and not rows:
        return int(cr[1])    # like, if called as get_tty_size(rows=False)
    elif rows and not cols:
        return int(cr[0])    # get_tty_size(cols=False)
    else:
        # if both or neither
        return int(cr[1]), int(cr[0])
