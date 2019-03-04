# https://leetcode.com/problems/longest-valid-parentheses/
# Given a string containing just the characters '(' and ')', find the length of the longest
# valid (well-formed) parentheses substring.

# key idea
# if we see a '(', add its index.
# So if we see a ')' this implies the previous character was either '(' or ')' or ""
# In all three cases we pop the stack.
# 1. If stack only had [-1] and we see a ')', then we pop stack. And add index of ')' on to stack
# 2. If stack had the index of '(', we pop it and we can check for max
# 3 if stack had the index of a ')' we pop it and replace it with index of current ')' (new marker)

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack = [-1] # initial marker for beginning of string
    i = 0
    m = 0
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            stack.pop()
            if not stack: # stack will be empty only if we encountered a ')' without seeing a '('
                stack.append(i)
            else:
                m = max(m, i - stack[-1]) # stack[-1] will always contain the start of the current valid substring
                
    return m



print(longestValidParentheses("())"))
print(longestValidParentheses(")()"))
print(longestValidParentheses("(()"))
print(longestValidParentheses(")()())"))
print(longestValidParentheses("(())(()"))
print(longestValidParentheses("()()(()(()()()))"))


