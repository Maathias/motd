import os
import misc

df = os.popen("df --output=source,fstype,size,used,avail,pcent,target").read()
df = df.split('\n')
df.pop(0)

for drv in df:
    if any(x in drv for x in ['drvfs', 'ext4']):
        drv = drv.split()
        print("\x1b[36m{}\x1b[0m mounted on {} {:.1f}GB of {:.1f}GB".format(
            drv[0],
            drv[6],
            misc.gig(drv[4]),
            misc.gig(drv[2])
        ))
        print(misc.bar(drv[3], drv[2], ['\x1b[94m=', '-']))

print()