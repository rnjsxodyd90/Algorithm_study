import unittest
from 344_Reversestring import 344_Reversestring
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse_string(self):
        # Test case 1: Normal string
        s = ["h", "e", "l", "l", "o"]
        expected = ["o", "l", "l", "e", "h"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

        # Test case 2: Palindrome
        s = ["r", "a", "c", "e", "c", "a", "r"]
        expected = ["r", "a", "c", "e", "c", "a", "r"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

        # Test case 3: Empty string
        s = []
        expected = []
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

        # Test case 4: Single character
        s = ["a"]
        expected = ["a"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

        # Test case 5: Two characters
        s = ["a", "b"]
        expected = ["b", "a"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

if __name__ == '__main__':
    unittest.main()