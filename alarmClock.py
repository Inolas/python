# https://jugad2.blogspot.in/2013/11/a-simple-alarm-clock-in-python-command.html
# https://stackoverflow.com/a/29590673/8343049

import sys
import string
import subprocess
from time import sleep

sa = sys.argv
lsa = len(sys.argv)

f = open('text.txt')
message = f.read()
#message = raw_input("Enter the message :\t")

if lsa != 2:
    print "Usage: [ python ] alarm_clock.py duration_in_seconds"
    print "Example: [ python ] alarm_clock.py 10"
    print "Use a value of 0 seconds for testing the alarm immediately."
    print "Beeps a few times after the duration is over."
    print "Press Ctrl-C to terminate the alarm clock early."
    sys.exit(1)
try:
    seconds = int(sa[1])
except ValueError:
    print "Invalid numeric value (%s) for seconds" % sa[1]
    print "Should be an integer >= 0"
    sys.exit(1)

if seconds < 0:
    print "Invalid value for seconds, should be >= 0"
    sys.exit(1)

if seconds == 1:
    unit_word = " minute"
else:
    unit_word = " seconds"

try:
    if seconds > 0:
        print "Sleeping for " + str(seconds) + unit_word
        sleep(seconds)
    print "\n\t\tWake up\n\n"
#    subprocess.call(['speech-dispatcher'])        #start speech dispatcher
    subprocess.call(['spd-say', '"Wake up dumass "'])

	
#    for i in range(5):
#	print "\007"
#       print chr(7),
#        sleep(1)

except KeyboardInterrupt:
    print "Interrupted by user"
    sys.exit(1)
