"""
https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1

"""


""" 
🧠 Time and Space Complexity:
Time Complexity: O(n)
Space Complexity: O(log n) due to recursive stack depth in case of a balanced split (binary tree recursion).


Number of Comparisons:
The total number of comparisons: Different for even and odd n, see below: 
        
If n is odd:    3*(n-1)/2  
If n is even:   1 + 3*(n-2)/2 = 3n/2-2, 1 comparison for initializing min and max, 
            and 3(n-2)/2 comparisons for rest of the elements

"""
def get_min_max_recursive(array, start, end):
    """
    Recursively finds the minimum and maximum values in the array between indices start and end.

    Args:
    - array (List[int]): The input array of integers.
    - start (int): Starting index of the segment.
    - end (int): Ending index of the segment.

    Returns:
    - Tuple[int, int]: A tuple containing (minimum value, maximum value).
    """
    
    # Base Case 1: Empty range
    if start > end:
        return float('inf'), float('-inf')
    
    # Base Case 2: Only one element in the range
    if start == end:
        return array[start], array[end]
    
    # Base Case 3: Only two elements — directly compare
    if end - start == 1:
        if array[start] > array[end]:
            return array[end], array[start]
        else:
            return array[start], array[end]
    
    # Recursive Case: Divide the array into two halves
    mid = start + (end - start) // 2
    
    # Recurse on the left half
    left_min, left_max = get_min_max_recursive(array, start, mid)
    
    # Recurse on the right half
    right_min, right_max = get_min_max_recursive(array, mid + 1, end)
    
    # Combine the results from both halves
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)
    
    return overall_min, overall_max


class Solution:
    def get_min_max_v1(self, arr):
        max_num = float('-inf')  # or arr[0] if you know the array is not empty
        min_num = float('inf')
        
        for i in range(len(arr)):
            if arr[i] > max_num:
                max_num = arr[i]
            if arr[i] < min_num:
                min_num = arr[i]
            print(f"Current min: {min_num}, max: {max_num}")
                
        return min_num, max_num
    
    def get_min_max_v2(self,arr):
        """
            Returns the minimum and maximum values in the array.

            Args:
            - array (List[int]): The input array of integers.

            Returns:
            - Tuple[int, int]: A tuple containing (minimum value, maximum value).
        """
        return get_min_max_recursive(arr, 0, len(arr) - 1)
    
    def get_min_max_v3(self, arr):
        """
            Time Complexity: O(n)
            Auxiliary Space: O(1) as no extra space was needed.
            
            Number of Comparisons:
            The total number of comparisons: Different for even and odd n, see below: 

            If n is odd:    3*(n-1)/2  
            If n is even:   1 + 3*(n-2)/2 = 3n/2-2, 1 comparison for initializing min and max, 
                      and 3(n-2)/2 comparisons for rest of the elements
        """
        i = 0
        overall_min = float('inf')
        overall_max = float('-inf')
        if len(arr)%2==0:
            if arr[0]>=arr[1]:
                overall_min = arr[1]
                overall_max = arr[0]
            else:
                overall_min = arr[0]
                overall_max = arr[1]
            i = 2
        else:
            i = 1
            overall_min = arr[0]
            overall_max = arr[0]
            
            
        while(i<len(arr)-1):
            if arr[i] > arr[i+1]:
                overall_max = max(overall_max,arr[i])
                overall_min = min(overall_min,arr[i+1])
            else:
                overall_max = max(overall_max,arr[i+1])
                overall_min = min(overall_min,arr[i])
            i += 2
        
        return overall_min,overall_max



def main():
    sol = Solution()
    
    test_cases = [
        ([3, 1, 4, 1, 5, 9, 2], (1, 9)),
        ([1], (1, 1)),
        ([5, 5, 5, 5], (5, 5)),
        ([-10, -20, 0, 10, 20], (-20, 20)),
        ([], (float('inf'), float('-inf'))),  # Edge case: empty list
    ]

    for idx, (arr, expected) in enumerate(test_cases):
        print(f"\nTest case {idx + 1}: {arr}")
        result = sol.get_min_max_v1(arr)
        print(f"Result: {result}, Expected: {expected}")
        assert result == expected, f"Test case {idx + 1} failed"

    print("\nAll test cases passed!")


if __name__ == "__main__":
    main()