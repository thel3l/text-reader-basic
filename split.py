import os

readfile = open("2.ogg", "rW")
for line in readfile:
	Type = line.split("OggS")
	#x = Type[-1]
	part = line.partition("OggS")[2]
	#if part == "OggS*":
	print(part)