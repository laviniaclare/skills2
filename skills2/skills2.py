string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
    pass

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
    pass

"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    pass

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    pass

"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    output=[]
    for word in words:
    	if not word in output:
    		output.append(word)
    return output


print "Testing Q1 'find_duplicates':"
print find_duplicates(['hi','hi','hi'])
print find_duplicates(['how','are','you','how','are'])
print find_duplicates(['cool','beans'])
"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    print "Do word_length later, plz"
word_length('gah')

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def english_2_pirate(string):
	e2pdict={
		"sir":"matey", 
		"hotel":"fleabag inn", 
		"student":"swabbie", 
		"boy":"matey", 
		"madam":"proud beauty", 
		'professor':'foul blaggart',
		'restaurant':'galley',
		'your':'yer',
		'excuse': 'arr',
		'students':'swabbies',
		'are':'be',
		'lawyer': 'foul blaggart',
		'the':'th',
		'restroom':'head',
		'my':'my',
		'hello':'avast',
		'is':'be',
		'man':'matey'
		}
	string=string.lower()
	word_list=string.split()                             #convert input string to list
	word_index=0										 #set index for later use	
	for word in word_list:
		if word in e2pdict:
			pirate_translation=e2pdict[word]
			word_list.remove(word)                        
			word_list.insert(word_index, pirate_translation)    #replace word with pirate translation
		word_index+=1

	output=' '.join(word_list)

	return output

print "Testing english_2_pirate translator"
print english_2_pirate("man, this professor needs to get off my back")











