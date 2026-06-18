class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        n = 0
        res = 0
        for ops in operations:
            # sum 2 previous elements
            if ops == "+":
                add = result[n] + result[n - 1]
                result.append(add)
            # multiple by 2
            elif ops == "D":
                double = result[n] * 2
                result.append(double)
            # remove last
            elif ops == "C":
                del result[n]
            # just append
            else:
                num = int(ops)
                result.append(num)
            n = len(result) - 1
        return sum(result)