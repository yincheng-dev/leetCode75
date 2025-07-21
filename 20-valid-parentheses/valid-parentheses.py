class Solution(object):
    def isValid(self, s):
        # use stack to keep the open brackets
        stack = []
        # hash map to map closing brackets to the corresponding opening brackets
        bracket_map = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:

            if char in bracket_map:
                #pop the last item from the stack if it is not empty
                top = stack.pop() if stack else '#'

                if bracket_map[char]!=top:
                    return False
            else: 
                stack.append(char)

        return True if not stack else False                

        

        