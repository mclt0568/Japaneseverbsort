#Copyright(c) 2019 mclt0568. MIT LISENCE applied.
#author: Mclt0568 aka Frankie
#Lets check out the file 'wordlist'

from os import system
system("clear")
magicverbs = [
	"おきます",
	"おります",
	"おちます",
	"かります",
	"できます",
	"たります",
	"あびます"
]
hiragana = ["あ","か","さ","た","な","は","ま","や","ら","は","い","き","し","ち","に","ひ","み","り","う","く","す","つ","ぬ","ふ","む","ゆ","る","え","け","せ","て","ね","へ","め","れ","お","こ","そ","と","の","ほ","も","よ","ろ","を","ぁ","ぃ","ぅ","ぇ","ぉ","っ","ん","ゃ","ゅ","ょ","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","ぢ","づ","で","ど","ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ","ゔ"]


def countpronounce(verb:str):
	verb = verb.replace("ゃ","")
	verb = verb.replace("ゅ","")
	verb = verb.replace("ょ","")
	return len(verb)

def excep(error:str,errstr:str):
	print("\nerror occured on '{}' \ndue to the following reason \n{}\n".format(errstr,error))
	exit()

def removemasu(verb:str):
	if len(verb) < 3:
		excep("verb in ます form not completedm, need to be atleast 3 characters",verb)
	elif verb[-2:] == "ます":
		return verb[0:-2]
	else:
		excep("'ます' cannot be found",verb)

def _checkirow(verb:str):
	if verb[-1] in ["い","き","し","ち","に","ひ","み","り"]:
		return True
	else: return False

def _checksimasu(verb:str):
	if (verb[-1] in ["し","き"]) and (len(verb) == 1):
		return True
	else: return False

def _checkendsi(verb:str):
	if verb[-1] == "し":
		return True
	else: return False
		
def sort(verb:str):
	global magicverbs,hiragana
	if verb[0:2] == "//":
		return "None" 
	for i in list(verb):
		if not (i in hiragana):
			excep("None Hiragana word found '{}'".format(i),verb)
	if verb in magicverbs:
		return 2
	_verb = removemasu(verb)
	if len(_verb) == 1:
		return 2
	elif (countpronounce(_verb) >= 3)and(_checkendsi(_verb)):
		return 3
	elif (_checkirow(_verb)):
		return 1
	else:
		return 2

def sortforfile(filename:str):
	try:
		with open(filename,"r",encoding="utf8") as a:
			data = a.read().split("\n")
			for i in data:
				_result = sort(i.strip())
				if not(_result == "None"):
					print("Verb '{}' is in catagory of group {}".format(i,str(_result)))
	except Exception as e:
		excep("SystemError.{}".format(e),"AtFile:{}".format(filename))

	

def showresult(verb:str,ctgry:int):
	print("Result:\nVerb: '{}'\nCatagory: {}".format(verb,str(ctgry)))
while True:
	vocab = input("\nInput verb in hiragana(あいう) and in ます form\nImport a wordlist by '#filename'\n>")
	if vocab[0] == "#":
		sortforfile(vocab[1:])
	else:
		result = sort(vocab)
		showresult(vocab,result)