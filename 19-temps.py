import os
import misc

# temps = os.popen("sensors -u").read()
temps = "\ncoretemp-isa-0000\nAdapter: ISA adapter\nPackage id 0:\n  temp1_input: 37.000\n  temp1_max: 80.000\n  temp1_crit: 85.000\n  temp1_crit_alarm: 0.000\nCore 0:\n  temp2_input: 35.000\n  temp2_max: 80.000\n  temp2_crit: 85.000\n  temp2_crit_alarm: 0.000\nCore 1:\n  temp3_input: 31.000\n  temp3_max: 80.000\n  temp3_crit: 85.000\n  temp3_crit_alarm: 0.000\n\nnouveau-pci-0100\nAdapter: PCI adapter\nGPU core:\n  in0_input: 0.980\n  in0_min: 0.830\n  in0_max: 1.000\ntemp1:\n  temp1_input: 47.000\n  temp1_max: 95.000\n  temp1_max_hyst: 3.000\n  temp1_crit: 105.000\n  temp1_crit_hyst: 5.000\n  temp1_emergency: 135.000\n  temp1_emergency_hyst: 5.000"
temps = temps.split('\n')
lastline = False
out = ""

for line in temps:
    # print(repr(lastline), repr(line))
    if lastline == '':
        out += line+'\n'
    lastline = line

    if 'temp' in line and 'input' in line:
        line = line.split()
        out += " {} {}{:.1f}\x1b[0m\n".format(
            line[0],
            '\x1b[91m' if float(line[1])>80 else '\x1b[93m' if float(line[1])>65 else '\x1b[92m',
            float(line[1])
            )

print(out)