#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        
        #code here
        sort_words={}
        for i in words:
            sorted_word="".join(sorted(i))
            if sorted_word not in sort_words:
                sort_words[sorted_word]=[i]
            else:
                sort_words[sorted_word].append(i)
            
        ans=[]
        for grp in sort_words.values():
            ans.append(grp)
        return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends