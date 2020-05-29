import math

def bar(used, total, chars=['#', '-'], max=40):
	percent = int(used)/float(total)
	len = int(math.floor(percent*max))
	rest = max - len

	return " {:.1f}% {}[{}\x1b[0m{}\x1b[0m]".format(percent*100, 'a' if percent>=1 else (' ' if percent >=0.1 else '  '), chars[0]*len, chars[1]*rest)
