#!/usr/bin/python

import os
import sys


class Singleinstance:
    '''
    Singleinstance - make sure that only a single instance of an application is running.
    '''
                        
    def __init__(self, pidPath):
        '''
        pidPath - full path/filename where pid for running application is to be
                  stored.  Often this is ./var/<pgmname>.pid
        '''
        self.pidPath = pidPath

        if os.path.exists(self.pidPath):				# See if pidFile exists
            with open(self.pidPath, 'r') as f:		# Make sure it is not a "stale" pidFile
                pid = int(f.read().strip())
            try:								# Check list of running pids, if not running it is stale so overwrite
                os.kill(pid, 0)
                self.running = True
            except OSError:
                self.running = False
        else:
            self.running = False

        if not self.running:
            with open(self.pidPath, 'w') as fp:		# Write my pid into pidFile to keep multiple copies of program from running.
                fp.write(str(os.getpid()))

    def is_already_running(self):
        return self.running

    def __del__(self):
        if not self.running:
            os.unlink(self.pidPath)



if __name__ == "__main__":

    # do this at beginnig of your application
    lockfname = 'Singleinstance.pid' # '%s.pid' % os.path.basename(__file__)
    myapp = Singleinstance(lockfname)

    if myapp.is_already_running():
        sys.exit("Another instance of this program is already running")
    
    import time
    time.sleep(200)
    # not running, safe to continue...
    print "No another instance is running, can continue here"
