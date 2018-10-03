#!/usr/bin/python



# <copy-paste'able:>
# === TTY COLORS =======================================================
import sys
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
	if has_colours:
		seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
		sys.stdout.write(seq)
	else:
		sys.stdout.write(text)

def getcoltext(text, colour=WHITE):
	if has_colours:
		return "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
	else:
		return text
# ======================================================================


if __name__ == '__main__':
	printout("[debug]   ", GREEN)
	print("in green")
	printout("[warning] ", YELLOW)
	print("in yellow")
	printout("[error]   ", RED)
	print("in red")
	printout("[error]   ")
	print("in nocolor")
	
	print
	print 'normal text, ' + getcoltext("red text", RED) + ', normal text again'
