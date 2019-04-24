#Grupo 61 / Joao Trindade - 80805 / Joao Simao - 81654
import string, re, collections, sys, unicodedata
from itertools import islice, izip, combinations

def remove_accents(input_str):
	encoding = "utf-8"
	unicode_string = input_str.decode(encoding)
	nfkd_form = unicodedata.normalize('NFKD',unicode_string)
   	return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def grams(inputFile):
	unwantedChars = '[^a-z | \s | -]'
	
	file = open(inputFile + '.final','r')
	nopunct = re.sub(unwantedChars,'',remove_accents(file.read().lower()))
	file.close()

	if "cobrem"  in inputFile:
		lema = ["cobrir", "cobrar"]
	else:
		lema = ["ver", "vestir"]
	#write to output:
	unigramsFile = open(inputFile + 'Unigramas.txt','a')
	unigramsCount = collections.Counter(nopunct.split())
	for item in sorted(unigramsCount.items()):
		unigramsFile.write(item[0] + '\t' + str(item[1] + len(unigramsCount.items())) + '\n')
	unigramsFile.close()

	print '________________\nUnigrams calculated!\nOutput file:' + unigramsFile.name + '\n________________\n'

	unigramItems = unigramsCount.items()
	bigramsaux = {}
	for uni1 in unigramItems:
		for l in lema:
			key = uni1[0]+" "+l
			bigramsaux[key] = 1
			key = l+" "+uni1[0]
			bigramsaux[key] = 1

	words = re.findall("\w+", nopunct)
	
	bigramsCount = collections.Counter(izip(words, islice(words, 1, None)))

	bigramsFile = open(inputFile + 'Bigramas.txt','a')
	
	for item in sorted(bigramsCount.items()):
		if item[0][0] in lema or item[0][1] in lema:
			bigramsaux[item[0][0] + " "+ item[0][1]]= item[1]+1

	output = ""
	for key in bigramsaux.keys():
		output+= key + "\t" + str(bigramsaux[key]) + "\n"
	bigramsFile.write(output)
	bigramsFile.close()

	print '________________\nBigrams calculated!\nOutput file:' + bigramsFile.name + '\n________________\n'

grams(sys.argv[1])