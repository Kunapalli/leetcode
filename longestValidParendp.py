# https://leetcode.com/problems/longest-valid-parentheses/
# Given a string containing just the characters '(' and ')', find the length of the longest
# valid (well-formed) parentheses substring.

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = [0]*n
    # dp[i] = j if string ending in s[i] is a valid parantheses of length j.
    # "()()"; dp[1] = 2, dp[3] = 4 and dp for all indices where s[index] = '(' is zero
    
    i = 1
    m = 0
    while i < n:
        c = s[i]
        if c == ')':
            if s[i-1] == '(': # we just saw a "()". We use what was there two chars ago. 
                dp[i] = dp[i-2] + 2
                m = max(dp[i], m)
                
            else: # s[i-1] == ')'
                # first make sure we are in bounds.
                # second, traverse the chain. Since prev char is ')' we see if character before it matches is '('
                # this is s[i - dp[i-1] - 1]. If so, we need to look for further chaining
                # consider string: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
                #                  ( ) ( ) ( ( ) ( ( )  (  )  (  )  )  )
                # Let i = 14. s[14] matches s[7] (14 - dp[13] - 1]
                # If s[7] is a '(' then do chaining. Look at the value of dp[6]
                # dp[14] = dp[13] + dp[6] + 2
                # if we have reached beginning of string, no further chaining is necessary
                # so dp[14] = dp[13] + 2
                # note if s[6] happens to be a '(', then no harm done as then dp[6] would be zero and so dp[14] = 6 + 2 = 8
                
                if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
                        m = max(dp[i], m)
                    else:  # we have reached beginning of string
                        dp[i] = dp[i-1] + 2 
                        m = max(dp[i], m)

        i += 1
    return m


print(longestValidParentheses("())"))
print(longestValidParentheses(")()"))
print(longestValidParentheses("(()"))
print(longestValidParentheses(")()())"))
print(longestValidParentheses("(())(()"))
print(longestValidParentheses("()()(()(()()()))"))


