'''
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''

#mycode
def fruits_into_baskets(fruits):
  result=0
  for i in range(len(fruit)-2):
      b_f=[fruit[i]]
      b_s=[]
      count=1
      for j in range(i+1,len(fruit)):
          if len(b_s)==0:
              count+=1
              b_s.append(fruit[j])
          elif fruit[j] == b_f[0]:
              count+=1
          elif fruit[j] == b_s[0]:
              count+=1
          else:
              break
          result=max(count,result)
  return result


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()



'''
Time Complexity 
The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input array. 
The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N)which is asymptotically equivalent to O(N).
Space Complexity 
The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.
Similar Problems 
Problem 1: Longest Substring with at most 2 distinct characters
Given a string, find the length of the longest substring in it with at most two distinct characters.
Solution: This problem is exactly similar to our parent problem.
'''
