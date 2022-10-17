'''
Problem Statement 
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''

#mycode
def length_of_longest_substring(str, k):
  s=list(str)
  res=0
  for i in range(len(s)):
      c=0
      d_c=0
      for j in range(i,len(s)):
          if s[j]==s[i]:
              c+=1
          elif s[j]!=s[i] and d_c<k:
              d_c+=1
              c+=1
          else:
              break
      res=max(res,c)
  return res


def main():
  print(length_of_longest_substring("aabccbb", 2))
  print(length_of_longest_substring("abbcb", 1))
  print(length_of_longest_substring("abccde", 1))


main()



'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of letters in the input string.
Space Complexity 
As we are expecting only the lower case letters in the input string, we can conclude that the space complexity will be O(26), to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).
'''
