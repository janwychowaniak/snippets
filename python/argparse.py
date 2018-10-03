#!/usr/bin/python




import argparse



# przyklad 1

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Generate server stats from its log file.')
	parser.add_argument('srvlogfile')
	parser.add_argument('-p', action='store_true', help='Show prolog (head) of the stats only')
	parser.add_argument('-c', action='store_true', help='Show clippgen_reqs counts only')
	parser.add_argument('-i', action='store_true', help='Show source IP addrs only')
	parser.add_argument('-a', action='store_true', help='Show everything')
	args = parser.parse_args()

	disp_head = args.p
	disp_counts = args.c
	disp_ips = args.i
	disp_all = args.a
	srvlogfile = args.srvlogfile


	if disp_head:
		print 'disp_head'
	elif disp_counts:
		print 'disp_counts'
	elif disp_ips:
		print 'disp_ips'
	else:
		print 'else'
	

# przyklad 2

if __name__ == '__main__':
    aparser = argparse.ArgumentParser(description='price tracker')
    aparser.add_argument('-l', help='a whole link to parse initial info from')
    aparser.add_argument('-c', help='the check-in date')
    aparser.add_argument('-o', help='the offer ID')

    args = aparser.parse_args()

    input_url = args.l
    input_checkInDate = args.c
    input_offerID = args.o


# more here: http://docs.python.org/2/library/argparse.html
