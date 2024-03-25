# main.py
import random
random_number = random.randint(0,9)

#create a list of 20 prefixes
prefixes = ["anti","de","dis","en","fore","inter","mid","mis" "non","over","pre","re","semi ","sub ","trans ","un ","under ","up ","extra ","giga ",]

#create a list of 20 suffixes
suffixes = ["able","ible","al","ed","en","er","or","est","ful","ic","ing","ion","tion","ity ","ive ","less ","ly ","ment ", "ness ","ous ", "s ","y ",]

#create a list of 20 word roots
roots = ["auto","bio","chron","dyna","hypo","hydra","hyper", "opt","phobia","pseudo","tele ","ego ","act ","form ", "homo ","logy ","meter ","morph ","phil ",]

#create definitions for each word
listprefixesdef= ["opposed", "down", "citizen", "in","before", "amoung", "middle", "wrong ", "not ", "to much ","before ", "again ","half ","underneath ", "across ","not ", "below ","higher ","outside ","big "]
listsuffixesdef = ["easily handled", "able to be", "all", "again", "in", "faster", "add", "most ", "able", "of", "result", "action", "quality", "full of", "without", "having characteristics", "doing", "shape", "man", "study", "measure", "change", "love", "make something plural", "characterized by"]
listrootwordsdef = ["automatic", "life","a sense of time", "power", "little", "Greek for water", "much", "choice", "fear", "false", "sight", "myself", "move", "shape", "main", "study", "measure", "change", "love"]

#create statement
x = random.randint(0,len(listprefixesdef) - 1)
y = random.randint(0,len(listsuffixesdef) - 1)
z = random.randint(0,len(listrootwordsdef) - 1)

word = prefixes[x] + roots[z] + suffixes[y]
definition = listprefixesdef[x] + listrootwordsdef[z] + listsuffixesdef[y]
print(word)
print(definition)