#Grupo 61 / Joao Trindade - 80805 / Joao Simao - 81654
import sys, unicodedata
from itertools import islice, izip

def remove_accents(input_str):
	encoding = "utf-8"
	unicode_string = input_str.decode(encoding)
	nfkd_form = unicodedata.normalize('NFKD',unicode_string)
   	return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def ANALisador(unigrams,bigrams,param,test):
	unigramfile = open(unigrams,'r')
	bigramfile = open(bigrams,'r')
	paramfile = open(param,'r')
	testfile = open(test,'r') 


	testphrases = map(lambda x:x.lower(),testfile.readlines())

	testphrases = [remove_accents(x.strip()) for x in testphrases] 
	
	unigramlist = [x.strip() for x in unigramfile.readlines()]
	bigramlist = [x.strip() for x in bigramfile.readlines()]

	for x in range(len(unigramlist)):
		unigramlist[x] = unigramlist[x].split("\t")

	for x in range(len(bigramlist)):
		bigramlist[x] = bigramlist[x].split("\t")

	paramData = []

	aux = paramfile.readlines()
	paramData.append(aux[0].replace("\n",""))
	paramData.append(aux[1].split(" ")[0])
	paramData.append(aux[1].split(" ")[1])

	if paramData[0] == "cobrem":
		resultfile = open(paramData[0] + "1Resultado.txt","w")
	else:
		resultfile = open(paramData[0] + "2Resultado.txt","w")

	auxcounter = 1
	for x in testphrases:
		xlist = []
		xlist.append(x)
		xbigrams = getBigrams(xlist)
	
		objbigrams = []
		for x in xbigrams:
			if paramData[0] in x:
				objbigrams.append(x)

		firstlema = []
		firstlema.append(objbigrams[0].split(" ")[0] +" "+paramData[1])
		firstlema.append(paramData[1] +" "+objbigrams[1].split(" ")[1])

		secondlema = []
		secondlema.append(objbigrams[0].split(" ")[0]+" "+paramData[2])
		secondlema.append(paramData[2] +" "+objbigrams[1].split(" ")[1])

		#counters for first lema:
		counterbigram1=0
		counterbigram2=0
		counterunigram1=0
		counterunigram2=0

		#counters for second lema:
		counterbigram3=0
		counterbigram4=0
		counterunigram3=0
		counterunigram4=0

		p1 = 0
		p2 = 0

		#count number of bigram appearences for both lema cases:
		for x in bigramlist:
			if firstlema[0] == x[0]:
				counterbigram1 = float(x[1])
			elif firstlema[1] == x[0]:
				counterbigram2 = float(x[1])
			if secondlema[0] == x[0]:
				counterbigram3 = float(x[1])
			elif secondlema[1] == x[0]:
				counterbigram4 = float(x[1])

		#count number of unigram appearences for both lema cases:
		for x in unigramlist:
			if firstlema[0].split(" ")[0] == x[0]:
				counterunigram1 = float(x[1])
			elif firstlema[1].split(" ")[0] == x[0]:
				counterunigram2 = float(x[1])
			
			if secondlema[0].split(" ")[0] == x[0]:
				counterunigram3 = float(x[1])
			elif secondlema[1].split(" ")[0] == x[0]:
				counterunigram4 = float(x[1])

		#chose the most probable lema:
		if counterunigram1!=0 and counterunigram2!=0:
			p1 = (counterbigram1/counterunigram1) * (counterbigram2/counterunigram2)
		if counterunigram3!=0 and counterunigram4!=0:
			p2 = (counterbigram3/counterunigram3) * (counterbigram4/counterunigram4)
		auxid = 0
		if p1 > p2:
			auxid=1
		
		else:
			auxid=2
		if (p1!=0 or p2!=0 ):
			resultfile.write("O lema mais provavel na frase numero " + str(auxcounter) + " e: " + paramData[auxid]
			 + ".\nProbabilidade do lema " + paramData[1] + ": " + str(p1)
			 + ".\nProbabilidade do lema " + paramData[2] + ": " + str(p2) + "\n\n")
		else:
			resultfile.write("Falta de informacao no corpora para decidir qual o lema mais provavel (Frase " + str(auxcounter) + ").\n")
		auxcounter+=1
	print "Success!\nOutput file: " + resultfile.name

def getBigrams(phrase):
	bigrams = [b for l in phrase for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
	for x in range(len(bigrams)):
		bigrams[x] = bigrams[x][0]+" " + bigrams[x][1]
	return bigrams

ANALisador(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])