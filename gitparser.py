#TODO
import re
import sys

try:
	f = open(sys.argv[1])
except:
	print "oops"
	sys.exit()

def parse(sentence):
	while "(" in sentence:
		count = 0
		end = None
		for x in range(len(sentence)):
			if sentence[x] == "(":
				count += 1
			elif sentence[x] == ")":
				count -= 1
				if count == 0:
					end = x
					break
		
		focus = sentence[sentence.index("("):end+1]
		sentence = sentence.replace(focus, parse(focus[1:len(focus)-1])) 
	if "+" in sentence:
		index = sentence.find('+')
		left = sentence[0:index+1]
		right = sentence[index+1:len(sentence)] 

		newleft = parse(left[0:len(left)-1])
		newright = parse(right)

		sentence = sentence.replace(left, newleft)
		sentence = sentence.replace(right, newright)
		
		summed = int(newleft) + int(newright)
		
		sentence = str(summed)

	if "-" in sentence:
		index = sentence.find('-')
		left = sentence[0:index+1]
		right = sentence[index+1:len(sentence)] 

		newleft = parse(left[0:len(left)-1])
		newright = parse(right)

		sentence = sentence.replace(left, newleft)
		sentence = sentence.replace(right, newright)
		
		subbed = int(newleft) - int(newright)
		
		sentence = str(subbed)

	if "*" in sentence:
		index = sentence.find('*')
		left = sentence[0:index+1]
		right = sentence[index+1:len(sentence)] 

		newleft = parse(left[0:len(left)-1])
		newright = parse(right)
		
		sentence = sentence.replace(left,newleft)
		sentence = sentence.replace(right,newright)
		
		mult = int(newleft)*int(newright)

		sentence = str(mult)   

	if "/" in sentence:
		index = sentence.find('/')
		left = sentence[0:index+1]
		right = sentence[index+1:len(sentence)] 

		newleft = parse(left[0:len(left)-1])
		newright = parse(right)

		sentence = sentence.replace(left, newleft)
		sentence = sentence.replace(right, newright)
		
		quotient = int(newleft) / int(newright)
		
		sentence = str(quotient)

	if not r"[^0-9]+" in sentence: #this doesnt work the way you assumed, will always return True, but is just never reached until ops are out anyway
		return sentence

f = f.readlines()
for line in f:
	line = line.replace("\n","")
	print parse(line)
