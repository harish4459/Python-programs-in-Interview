Longest Common Prefix Matching | Set-6


class Solution(object):
   def longestCommonPrefix(self, strs):
      """
      :type strs: List[str]
      :rtype: str
      """
      if len(strs) == 0:
         return ""
      current = strs[0]
      for i in range(1,len(strs)):
         temp = ""
         if len(current) == 0:
            break
         for j in range(len(strs[i])):
            if j<len(current) and current[j] == strs[i][j]:
               temp+=current[j]
            else:
               break
         current = temp
      return current
input_list = ["school","schedule","scotland"]
ob1 = Solution()
print(ob1.longestCommonPrefix(input_list))
Input
["school","schedule","scotland"]




def longestCommonPrefix( a):
      
    size = len(a)
  
    # if size is 0, return empty string 
    if (size == 0):
        return ""
  
    if (size == 1):
        return a[0]
  
    # sort the array of strings 
    a.sort()
      
    # find the minimum length from 
    # first and last string 
    end = min(len(a[0]), len(a[size - 1]))
  
    # find the common prefix between 
    # the first and last string 
    i = 0
    while (i < end and 
           a[0][i] == a[size - 1][i]):
        i += 1
  
    pre = a[0][0: i]
    return pre
  
# Driver Code
if __name__ == "__main__":
  
    input = ["geeksforgeeks", "geeks", 
                     "geek", "geezer"]
    print("The longest Common Prefix is :" ,
                 longestCommonPrefix(input))
  
