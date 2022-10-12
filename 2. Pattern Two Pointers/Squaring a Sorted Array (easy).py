'''
Problem Statement 
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
'''

#answer
def make_squares(arr):
  newarr=[arr[0]*arr[0]]

  for i in range(1,len(arr)):
    ele=arr[i]*arr[i]
    if ele > newarr[len(newarr)-1]:
        newarr.append(ele)
    elif ele < newarr[0]:
        newarr.insert(0,ele)
    else:
        j=len(newarr)-1
        while j>=0:
            if ele>newarr[j]:
                j-=1
            elif ele<=newarr[j]:
                newarr.insert(j,ele)
                j=-1
  return newarr


def main():

  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()


'''
Time complexity 
The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.
Space complexity 
The space complexity of the above algorithm will also be O(N); this space will be used for the output array.
'''
