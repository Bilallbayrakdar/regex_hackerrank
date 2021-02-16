import re
import sys

# file = open("input.html","r")
# st = file.read()

st = sys.stdin.read()

m_id = r'<div class="question-summary" id="question-summary-([0-9]+)">'
m_about = r'<div class="summary">\s*<h3><a href="[\w/-]*"\s*class="[\w/-]*">(.*)</a></h3>' 
m_time = r'<div class="[a-z-\s]*">\s*<div class="user-action-time">\s*asked <span title="[0-9-:Z\s"a-z=]*>*(.*)</span>'

ids = re.findall(m_id,st)
# print(ids)
abouts = re.findall(m_about,st)
# print(abouts)
times = re.findall(m_time,st)
# print(times)

data = []

for x,y,z in zip(ids,abouts,times):
    data.append([x,y,z])


for ele in data:
    for e in range(len(ele)):
        if e != len(ele)-1:
            print(ele[e], end=";")
        else:
            print(ele[e])

# 80417;Can I safely enclose battery-powered electronics in an antistatic bag to protect it from static electricity?;11 hours ago
# 80412;How to overwrite flash memory on STM32L series;12 hours ago
# 80407;about power supply of opertional amplifier;12 hours ago
# 80405;5V Regulator Power Dissipation;13 hours ago
# 80404;How to stop two DC motors simultaneously using limit switches;13 hours ago
# 80396;Logic Level Translator caveats;13 hours ago
# 80393;Microcontroller Newbe here. LED color pattern controller for arcade machine [on hold];14 hours ago
# 80385;how to scale dynamic range voltage to 1-5 volt;15 hours ago
# 80383;Is it the frequency that determines the current in a LC Tank Parallel Circuit?;15 hours ago
# 80378;Replacing resistors with equivalent resistor;15 hours ago
# 80371;Saturation current in inductor - Definition?;16 hours ago
# 80370;Is it possible for batteries to give a false reading of being charged with a multimeter?;16 hours ago
# 80366;Arduino - accessing extra analog pins on 32-pin SMT package;16 hours ago
# 80365;Capacitor Inrush Current;16 hours ago
# 80360;Designing ADC driver circuit using LTC6406;17 hours ago

# 80417;Can I safely enclose battery-powered electronics in an antistatic bag to protect it from static electricity?;11 hours ago
# 80412;How to overwrite flash memory on STM32L series;12 hours ago
# 80407;about power supply of opertional amplifier;12 hours ago
# 80405;5V Regulator Power Dissipation;13 hours ago
# 80404;How to stop two DC motors simultaneously using limit switches;13 hours ago
# 80396;Logic Level Translator caveats;13 hours ago
# 80393;Microcontroller Newbe here. LED color pattern controller for arcade machine [on hold];14 hours ago
# 80385;how to scale dynamic range voltage to 1-5 volt;15 hours ago
# 80383;Is it the frequency that determines the current in a LC Tank Parallel Circuit?;15 hours ago
# 80378;Replacing resistors with equivalent resistor;15 hours ago
# 80371;Saturation current in inductor - Definition?;16 hours ago
# 80370;Is it possible for batteries to give a false reading of being charged with a multimeter?;16 hours ago
# 80366;Arduino - accessing extra analog pins on 32-pin SMT package;16 hours ago
# 80365;Capacitor Inrush Current;17 hours ago