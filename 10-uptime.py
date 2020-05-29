import os
import re
import sys
import bar

uptime = os.popen('uptime -p').read()

print "System is up \x1b[34m{}\x1b[0m".format(uptime[3:-1])

who = os.popen('echo " 15:13:23 up 10 days,  1:33,  2 users,  load average: 1.01, 0.95, 0.98\nUSER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT\nmathias  pts/0    10.0.1.4         15:12    1.00s  0.09s  0.00s w\nmathias  pts/1    tmux(2498).%0    02Apr20 14:10m  2days  0.00s /bin/bash ./start"').read()

who = who.split('\n')[2:-1]
users = [0, 0]
for line in who:
    line = line.split()
    if line[2].startswith('tmux'):
        users[1] += 1
    else:
        users[0] += 1

print "{} users and {} terminals logged in".format(*users)

loads = os.popen("uptime").read()
loads = loads.split()[-3:]
loads[0] = loads[0][:-1]
loads[1] = loads[1][:-1]
sys.stdout.write("CPU: ")
for load in loads:
    load = float(load)
    color = '\x1b[32m'
    if load > 1:
        color = '\x1b[31m'
    else:
        if load > 0.5:
            color = '\x1b[33m'
    sys.stdout.write('{}{} '.format(color, load))
sys.stdout.write('\x1b[0m\n')

free = os.popen("free").read()
memory = free.split('\n')[1].split()
swap = free.split('\n')[2].split()
print "Memory: {:.1f}GB out of {:.1f}GB".format(
    float(memory[2])/(1024*1024), float(memory[1])/(1024*1024))
print bar.bar(memory[2], memory[1], ['\x1b[93m=', '-'])

print "Swap:   {:.1f}GB out of {:.1f}GB".format(
    float(swap[2])/(1024*1024), float(swap[1])/(1024*1024))
print bar.bar(swap[2], swap[1], ['\x1b[93m=', '-'])

ip = os.popen('ip addr').read()
ip = ip.split('\n')[:-1]

links = []
at = -1

for line in ip:
	line = line.split()

	if ':' in line[0]:
		if 'UP' in line[2]:
			links.append([line[1][:-1]])

	if 'link' in line[0]:
		links[-1].append([line[1]])

	if 'inet' in line[0]:
		links[-1][-1].append(line[1].split('/'))

# print links

for eth in links:
	if eth[0] == 'lo': continue

	# sys.stdout.write("{}: ".format(eth[0]))
	for mac in eth[1:]:
		print mac
	# for ip in range(2, len(eth)):
	# 	print " {} /{}".format(eth[ip][0], eth[ip][1])
