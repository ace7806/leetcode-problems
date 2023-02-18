
word = 'Isvalid'
words = ['isvalid']
#U 
#we need to somehow check the word has camel case as well as if its words are in the dictionary
#isValid = true, Isvalid = false, IsValid = true, aAAAAAAA [a] = true
#M
# im thinking of taking advantage of the fact its supposed to be camel case and make a list of splitted words and then checking seperately if it meets the requirements
# put the words into a set for faster lookup times
# make functions for checking
#P
# IsValid = [Is, Valid], Isvalid = [Isvalid]
# set = [is, valid, right]
# check first word is in the set if not return false
# loop through the rest of word
# check if camel case and check if word is in set if not return false 
# return True
#I
def test():
    split =[]
    l=0
    for r in range(1,len(word)):
        if word[r].isupper():
            split.append(word[l:r])
            l=r

    split.append(word[l:r+1])
    lookup = set(words)
    print(split)
    def isInWords(s:str):
        return s.casefold() in lookup
    def isCamelCase(s:str):
        return s[0].isupper()

    if not isInWords(split[0]): return False
    for x in range(1,len(split)):
        curr = split[x]
        if not isCamelCase(curr) and not isInWords(curr):  return False
    return True
print(test())
#R