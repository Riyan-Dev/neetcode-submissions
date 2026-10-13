class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n-2,-1,-1):
            arr[i] = max(arr[i], arr[i+1])

        ans = arr[1:]
        ans.append(-1)
        return ans