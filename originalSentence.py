import re

def findOriginal(sentence, diccSentence,  s=0, v=1, result=[]):
    if (v>len(sentence)): ## BASE-CASE
        if (s<v-1): ## IN CASE THE PROCESS WAS NOT A THOROUGH SUCCESS
            return None
        return result
    ## CHECK FOR MATCH IN THE CONTINUES SENTENCE FROM S-V (EXCLUDING V)
    match = re.compile(r'\b'+sentence[s:v]+r'\b').search(diccSentence)
    if (bool(match)):
        ## FOUND WORD IN DICTONARY
        result.append(match.group())
        s = v ## RESET PROCESS OF SEARCH
    return findOriginal(sentence, diccSentence, s, v+1, result)

def findOriginalSentence(sentence, dicc):
    diccSentence=""
    ## FOR EASE IN COMPUTATION COMPOSE STRING OF AVAILABLE WORDS
    for word in dicc:
        diccSentence+=word+" "
    return findOriginal(sentence, diccSentence)

print(\
findOriginalSentence('bedbathandbeyond', ['bed', 'bath', 'bedbath', 'and', 'beyond'])\
)
