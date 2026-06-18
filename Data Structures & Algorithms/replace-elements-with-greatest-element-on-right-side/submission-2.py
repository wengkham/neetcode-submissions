class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrLen = len(arr)
        arrLast = arrLen - 1
        for i in range(arrLen):
            if i != arrLast:
                arr[i] = max(arr[i+1:])
            else:
                arr[i] = -1
        return arr