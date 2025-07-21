"""
Merge Sort Algorithm
https://www.geeksforgeeks.org/merge-sort/

Merge sort is a divide-and-conquer algorithm. It works by:
1.  Dividing the unsorted list into n sublists, each containing one element (a list of one element is considered sorted).
2.  Repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.
"""
from typing import List

def sort_list(arr: list[int],start: int,end: int) -> list[int]:
    if start>end:
        return []
    
    if start==end:
        return [arr[start]]
    
    
    mid = start + (end-start)//2
    
    left = sort_list(arr,start,mid)
    right = sort_list(arr,mid+1,end)
    
    i = 0
    j = 0
    
    sorted_list: list[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i = i + 1
        else:
            sorted_list.append(right[j])
            j = j + 1
    
    while i < len(left):
        sorted_list.append(left[i])
        i = i + 1
        
    while j < len(right):
        sorted_list.append(right[j])
        j = j + 1
        
    return sorted_list

class Solution:
    def merge_sort(self, arr: List[int]) -> List[int]:
        """
        Sorts an array using the Merge Sort algorithm.
        This is a placeholder for you to implement the logic.

        A typical merge sort is recursive. You'll likely need a helper
        function for merging two sorted arrays.

        Args:
            arr: The list of integers to sort.

        Returns:
            A new list containing the sorted elements.
        """
        # --- Your Merge Sort logic goes here ---
        
        # Base case: If the array is empty or has one element, it's already sorted.
        if len(arr) <= 1:
            return arr

        # TODO:
        # 1. Find the middle of the array.
        # 2. Recursively sort the left half.
        # 3. Recursively sort the right half.
        # 4. Merge the two sorted halves.
        
        # You might want a helper function like:
        # def merge(left_half, right_half):
        #     ...
        
        return sort_list(arr=arr,start=0,end=len(arr)-1) # Replace this with your sorted array

def main():
    """
    Main function to run test cases for the merge_sort method.
    """
    sol = Solution()
    
    test_cases: list[dict] = [
        {"name": "General case", "input": [12, 11, 13, 5, 6, 7], "expected": [5, 6, 7, 11, 12, 13]},
        {"name": "Reverse sorted", "input": [5, 4, 3, 2, 1], "expected": [1, 2, 3, 4, 5]},
        {"name": "Already sorted", "input": [1, 2, 3, 4, 5], "expected": [1, 2, 3, 4, 5]},
        {"name": "Empty list", "input": [], "expected": []},
        {"name": "Single element", "input": [42], "expected": [42]},
        {"name": "With duplicates", "input": [3, 1, 4, 1, 5, 9, 2, 6], "expected": [1, 1, 2, 3, 4, 5, 6, 9]},
        {"name": "With negative numbers", "input": [-5, 8, -2, 0, 3], "expected": [-5, -2, 0, 3, 8]},
    ]

    for i, case in enumerate(test_cases):
        print(f"--- Test Case {i+1}: {case['name']} ---")
        input_arr = case["input"]
        expected_arr = case["expected"]
        
        print(f"Input:    {input_arr}")
        
        # Pass a copy of the input array to the function
        result = sol.merge_sort(list(input_arr))
        
        print(f"Your output: {result}")
        print(f"Expected:    {expected_arr}")

        if result is not None:
            try:
                assert result == expected_arr
                print("Status: PASS")
            except AssertionError:
                print("Status: FAIL")
        else:
            print("Status: PENDING (function not implemented)")
        
        print("-" * 25)

if __name__ == "__main__":
    main()
    


