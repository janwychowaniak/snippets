#!/usr/bin/python




# <copy-paste'able:>
# === PROG PRC =========================================================
import sys
class ProgressPrc:
	def __init__(self, _max_steps):
		self.max_steps = _max_steps
		self.bumpcount = 0
		self.full = False

	def bump(self):
		if self.bumpcount < self.max_steps:
			self.bumpcount += 1
			if self.bumpcount == self.max_steps:
				self.full = True
		else:
			raise Exception ("ProgressPrc: bumpcount over max_steps")

	def complete(self):
		self.bumpcount = self.max_steps

	def display(self):
		i = int(float(self.bumpcount)/float(self.max_steps)*100)
		sys.stderr.write("\r%d%%" %i)
		sys.stderr.flush()
		
	def pyk(self):
		self.bump()
		self.display()
		if self.full: print
# ======================================================================





if __name__ == '__main__':
	import time
	rangee = 200
	pp = ProgressPrc(rangee)
	for i in range(rangee):
		time.sleep(0.03	)
		pp.pyk()

