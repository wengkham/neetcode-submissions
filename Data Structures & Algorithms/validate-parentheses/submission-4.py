class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        oBracket = "["
        cBracket = "]"
        ocBracket = "{"
        ccBracket = "}"
        oParen = "("
        cParen = ")"
        stack = []
        
        for n in s:
            if n in [oBracket, ocBracket, oParen]:
                stack.append(n)
            elif n in [cBracket, ccBracket, cParen] and len(stack) >= 1:
                shouldBeOpen = stack.pop()
                if shouldBeOpen == oBracket and n == cBracket:
                    pass
                elif shouldBeOpen == ocBracket and n == ccBracket:
                    pass
                elif shouldBeOpen == oParen and n == cParen:
                    pass
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        else:
            return True