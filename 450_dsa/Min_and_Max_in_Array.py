"""
https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1

"""




class Solution:
    def get_min_max(self, arr):
        max_num = float('-inf')  # or arr[0] if you know the array is not empty
        min_num = float('inf')
        
        for i in range(len(arr)):
            if arr[i] > max_num:
                max_num = arr[i]
            if arr[i] < min_num:
                min_num = arr[i]
            print(f"Current min: {min_num}, max: {max_num}")
                
        return min_num, max_num
