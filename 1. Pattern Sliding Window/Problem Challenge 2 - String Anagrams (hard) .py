'''
Problem Challenge 2
String Anagrams (hard) 
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

#mycode
def find_string_anagrams(str, pattern):
  s=list(str)
  p=list(pattern)

  check=False
  ans=[]
  for i in range(len(s)):
      ans=[]
      temp=list(pattern)
      for j in range(i,len(p)+i):
          if s[j] in temp:
              ans.append(j)
              temp.remove(s[j])
              check=True
          else:
              check=False
              break
      if check:
          return ans
          break    
  return ans

def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()
