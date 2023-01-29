class Solution:
    def sortSentence(self, s: str) -> str:
        count=2
        for i in s:                   #find the number of words in s
            if i ==" ":
                count+=1
        res=[""]*count               #create a list with length of count
        k=0
        for j in range (len(s)-1):
            if s[j] ==" ":
                res[int(s[j-1])] = s[k:j-1]       #assign the words in s to the list res using the number by the end of each words as index in res
                k=j+1
        res[int(s[-1])] = s[k:len(s)-1]
        return (" ".join(res[1:]))
       

