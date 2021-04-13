"""
Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

    Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp' 

    Note: All inputs will be in lower-case. 

Example :

Input : cat dog god tca
Output : [[1, 4], [2, 3]]

"""

def anagrams(A):
        resDict = OrderedDict()
        res = []
        for i in range(len(A)):
            sortedWord = "".join(sorted(A[i]))
            if sortedWord in resDict:
                resDict[sortedWord].append(i+1)
            else:
                resDict[sortedWord] = [i+1]
        for eachob in resDict:
            res.append(resDict[eachob])
        return res