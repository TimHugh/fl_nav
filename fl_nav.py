#!/usr/bin/env python

import sys
from collections import deque

from fl_sys import *

def findPath(start, end):
  sys_open = deque()
  sys_closed = []
  last_sys = {}

  sys_closed.append(start)
#  print "Adding", start.name, "to search queue"
#  print "Entering", start.name
  for system in start.systems:
#    print "Adding", system.name, "to search queue"
    sys_open.append(system)
    last_sys[system] = start
    sys_closed.append(system)

  while len(sys_open) > 0:
    system = sys_open.popleft()
#    print "Entering", system.name

    if system == end:
#      print "Found destination!"
      return returnPath(last_sys, system, start)
    for nxt_sys in system.systems:
      if (not nxt_sys in sys_open) and (not nxt_sys in sys_closed):
#        print "Adding", nxt_sys.name, "to search queue"
        sys_open.append(nxt_sys)
        last_sys[nxt_sys] = system
        sys_closed.append(nxt_sys)

def returnPath(sys_links, current, start):
#  print "Tracing back from", current.name
  if sys_links[current] == start:
#    print "Reached", start.name
#    print "Added",current.name,"to directions"
    return [current]
  path = returnPath(sys_links, sys_links[current], start)
  path.append(current)
#  print "Added", current.name, "to directions"
  return path

def quit(input):
  if input.lower() == "quit":
    sys.exit(0)

########
# MAIN #
########

print "FREELANCER NAVIGATOR"
while True:
  print "\nNEW TRIP"
  input = raw_input("CURRENT SYSTEM: ")
  quit(input)

  start_sys = None
  try:
    start_sys = Systems[input.lower()]
  except:
    print "INVALID SYSTEM"
    continue

  input = raw_input("DESTINATION SYSTEM: ")
  quit(input)

  end_sys = None
  try:
    end_sys = Systems[input.lower()]
  except:
    print "INVALID SYSTEM"
    continue

  if start_sys == end_sys:
    print "CAN'T PLOT TRIP TO SAME SYSTEM"
    continue

  path = findPath(start_sys, end_sys)

  if not path:
    print "CANNOT PLOT PATH. INFORMATION NOT AVAILABLE"
    continue

  print len(path), (["JUMP","JUMPS"][len(path)>1])
  print start_sys.name.upper(),
  for system in path:
    print "->",system.name.upper(),
  print ""
