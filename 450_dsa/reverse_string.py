
"""
### Reverse a String
https://www.geeksforgeeks.org/problems/reverse-a-string/1


-  strings are immutable, which means you can't change their characters in-place.
"""


class Solution:
    def reverseString_v1(self, input_str: str) -> str:
        """
        Reverses the input string using a temporary variable and returns the result.

        Parameters:
        input_str (str): The string to be reversed.

        Returns:
        str: The reversed string.
        """

        # Convert the string to a list since strings are immutable
        char_list = list(input_str)

        # Get the length of the list
        length = len(char_list)

        # Swap characters using a temporary variable
        for i in range(length // 2):
            temp = char_list[i]
            char_list[i] = char_list[length - 1 - i]
            char_list[length - 1 - i] = temp

        # Join the list back to a string and return
        return "".join(char_list)
    
    
    def reverseString_v2(self, input_str: str) -> str:
        #more pythonic way
        return input_str[::-1]
    
    
    def reverseString_v3(self,input_str: str) -> str:
        def reverse_list_recursively(chars: list[str], start_index: int, end_index: int) -> None:
            """
            Recursively reverses the list of characters in-place.

            Parameters:
            chars (list[str]): List of characters to reverse.
            start_index (int): Starting index of the range to reverse.
            end_index (int): Ending index of the range to reverse.
            """
            if start_index >= end_index:
                return

            # Swap characters at start_index and end_index using a temporary variable
            temp = chars[start_index]
            chars[start_index] = chars[end_index]
            chars[end_index] = temp

            # Recursively reverse the remaining sublist
            reverse_list_recursively(chars, start_index + 1, end_index - 1)
            
            
        """
            Reverses the given string using recursion.

            Parameters:
            input_str (str): The input string to be reversed.

            Returns:
            str: The reversed string.
        """
        # Convert string to a list since strings are immutable
        char_list = list(input_str)

        # Reverse the list using the recursive helper function
        reverse_list_recursively(char_list, 0, len(char_list) - 1)

        # Join the characters back into a string
        return "".join(char_list)


def main():
    sol = Solution()
    test_cases = [
        "hello",
        "world",
        "racecar",
        "a",
        "",
        "123456789",
        "Python3.11"
    ]

    print("Testing reverseString_v1 (loop with temp variable):")
    for test in test_cases:
        print(f"Input: '{test}' → Output: '{sol.reverseString_v1(test)}'")

    print("\nTesting reverseString_v2 (slicing):")
    for test in test_cases:
        print(f"Input: '{test}' → Output: '{sol.reverseString_v2(test)}'")

    print("\nTesting reverseString_v3 (recursion):")
    for test in test_cases:
        print(f"Input: '{test}' → Output: '{sol.reverseString_v3(test)}'")


if __name__ == "__main__":
    main()
