import re
import os.path as osp
import os
par = os.pardir
cur = os.curdir
pat = osp.dirname(__file__)
class Dic(dict):
	def __missing__(self, key):
		return 0

def simpAlg(sol, wordArr):
	word = " " * len(sol)
	letters = "abcdefghijklmnopqrstuvwxyz"
	used = ""
	realLet = ""
	fakeLet = ""
	while word != sol:
		percent = {}
		wordM = "^" + word + "$"
		wordM = wordM.replace(" ", "[a-z]")
		wordR = re.compile(wordM)
		modArr = [x for x in arr if wordR.search(x)]
		for n, l in enumerate(letters):
			percent[n] = (len([x for x in modArr if x.find(l) != -1]) / len(modArr) * 100)
		percentOrd = sorted(percent, key=percent.get, reverse=True)
		final = letters[percentOrd[0]]
		letters = letters.replace(final, "")
		used += final
		rWord = re.compile("^" + word.replace(" ", ('[' + letters + ']')) + "$")
		wordArr = [i for i in arr if rWord.search(i)]
		wordArr.sort()
		if sol.find(final) != -1:
			realLet += final
			wordL = list(word)
			for i, l in enumerate(sol):
				if l == final:
					wordL[i] = l
			word = "".join(wordL)
		else:
			fakeLet += final

	print(sol, (len(used) - len(realLet)), (len(realLet) / len(used) * 100))
	#print("\nSolution: {}\nWord Found: {}\nLetters Used: {}\nLetters in Word: {}\nLetters not in Word: {}\nLetters not Used: {}\nWrong Guesses: {}\nPrecent Correct Guesses: {:.2f}%".format(sol, word, used, realLet, fakeLet, letters, (len(used) - len(realLet)), (len(realLet) / len(used) * 100)))
	return (len(realLet) / len(used) * 100)

def getWord(sol, wordArr):
	word = " " * len(sol)
	letters = "abcdefghijklmnopqrstuvwxyz"
	used = ""
	realLet = ""
	fakeLet = ""
	while word != sol:
		lDict = {}
		for l in letters:
			lDict[l] = Dic()
			for w in wordArr:
				if w.find(l) != -1:
					tup = tuple(x for x, i in enumerate(w) if i == l)
					lDict[l][tup] += 1
			#print(l, lDict[l])
		sortData = sorted({l : len(v) for l,v in lDict.items()}.items(), key=lambda x: x[1], reverse=True)
		#print(sortData)
		final = ""
		maxValue = sortData[0][1]
		finDict = {}
		for i, j in sortData:
			if j == maxValue:
				#print(i, lDict[i])
				finDict[i] = sum(k for l, k in lDict[i].items())
		#print(finDict)
		final = ((sorted({l : v for l,v in finDict.items()}.items(), key=lambda x: x[1], reverse=True)))[0][0]
		#print(final)
		letters = letters.replace(final, "")
		used += final
		rWord = re.compile("^" + word.replace(" ", ('[' + letters + ']')) + "$")
		wordArr = [i for i in arr if rWord.search(i)]
		wordArr.sort()
		if sol.find(final) != -1:
			realLet += final
			wordL = list(word)
			for i, l in enumerate(sol):
				if l == final:
					wordL[i] = l
			word = "".join(wordL)
		else:
			fakeLet += final

	print(sol, (len(used) - len(realLet)), (len(realLet) / len(used) * 100))
	return (len(realLet) / len(used) * 100)

print("Hangman Solver Test: ")
with  open(osp.join(pat, par, "resources", "wordsEn.txt")) as tFile:
	arr = set([i.strip("\n") for i in tFile.readlines()])
#tFile = open("\\Users\\Noah\\Documents\\Python Scripts\\Text Files\\wordsEn.txt", "r")
#nFile = open("\\Users\\Noah\\Documents\\Python Scripts\\Text Files\\testWords.txt", "r")
with  open(osp.join(pat, par, "resources", "tesTWords.txt")) as nFile:
	wordList = set([i.strip("\n") for i in nFile.readlines()])
sol = "reline"
word = " " * len(sol)
wordArr = [i for i in arr if len(i) == len(word)]
avg = 0
for w in wordList:
	wordArr = [i for i in arr if len(i) == len(w)]
	avg += getWord(w, wordArr)

print("Final:", (avg / len(wordList)))
#print()
#simpAlg(sol, wordArr)
#getWord(sol, word, wordArr)
#print(sol, word, letters, used, realLet, (len(realLet) / len(used) * 100), (len(used) - len(realLet)))
