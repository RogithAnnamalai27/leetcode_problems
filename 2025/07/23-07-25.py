"""
    Problem for date 23rd July 2025:

    You are given a string s and two integers x and y. You can perform two types of operations any number of times.
    Remove substring "ab" and gain x points.
    For example, when removing "ab" from "cabxbae" it becomes "cxbae".
    Remove substring "ba" and gain y points.
    For example, when removing "ba" from "cabxbae" it becomes "cabxe".
    Return the maximum points you can gain after applying the above operations on s.
    
    Example 1:
    Input: s = "cdbcbbaaabab", x = 4, y = 5
    Output: 19
    Explanation:
    - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
    - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
    - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
    - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
    Total score = 5 + 4 + 5 + 5 = 19.
    Example 2:
    Input: s = "aabbaaxybbaabb", x = 5, y = 4
    Output: 20

    
    Constraints:
    1 <= s.length <= 105
    1 <= x, y <= 104
    s consists of lowercase English letters
"""

def maximumGain(s: str, x: int, y: int) -> int:
    def remove_pair(s, first, second, score):
        stack = []
        total = 0
        for ch in s:
            if stack and stack[-1] == first and ch == second:
                stack.pop()
                total += score
            else:
                stack.append(ch)
        return "".join(stack), total

    res = 0
    if x >= y:
        # Remove "ab" first
        s, temp = remove_pair(s, 'a', 'b', x)
        res += temp
        # Remove "ba"
        s, temp = remove_pair(s, 'b', 'a', y)
        res += temp
    else:
        # Remove "ba" first
        s, temp = remove_pair(s, 'b', 'a', y)
        res += temp
        # Remove "ab"
        s, temp = remove_pair(s, 'a', 'b', x)
        res += temp
    return res
