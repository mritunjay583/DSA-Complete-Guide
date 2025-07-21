""" 
https://www.geeksforgeeks.org/dsa/kth-smallest-largest-element-in-unsorted-array-expected-linear-time/
"""

class Solution:
    
    def kthSmallest_v1(self, arr,k):
        """ 
        Algorithm is a partial insertion sort used to build a list of the k smallest elements in sorted order.
        """
        temp_list = []
        
        for i in range(len(arr)):
            j = 0
            print(temp_list)
            while j < len(temp_list):
                if arr[i]>temp_list[j]:
                    j = j + 1
                else:
                    break
            
            if j == 0 and len(temp_list) < k :
                temp_list.insert(0,arr[i])
                continue
            
            if j == len(temp_list) and len(temp_list) < k:
                temp_list.append(arr[i])
                continue
            
            if j==len(temp_list) and len(temp_list)==k:
                continue
                
            if len(temp_list) < k:
                temp_list.append(-1)
            
            a = len(temp_list) - 1
            while a>j:
                temp_list[a] = temp_list[a-1]
                a = a - 1
                
            temp_list[j] = arr[i]
            
        return temp_list[k-1]
    
def main():
    input = [7, 10, 4, 20, 15]
    k = 4
    sol = Solution()
    res = sol.kthSmallest_v1(arr=input,k=k)
    print(res)
    
if __name__=='__main__':
    main()