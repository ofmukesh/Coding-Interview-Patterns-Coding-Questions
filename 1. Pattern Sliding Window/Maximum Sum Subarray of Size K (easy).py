'''
Problem Statement #
Given an array of positive numbers and a positive number âkâ, find the maximum sum of any contiguous subarray of size âkâ.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

#mycode
def max_sub_array_of_size_k(k, arr):
  ans=-1
  for i in range(len(arr)-k+1):
    ans=max(ans(arr[i:i+k]),ans)
  return ans

def main():
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
  print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))

main()
