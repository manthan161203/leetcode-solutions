# Solution - PYTHON

class Solution:\n    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:\n        stack = []\n        n = len(temperatures)\n        answer = [0] * n\n        for i in range(n):\n            while stack and temperatures[i] > temperatures[stack[-1]]:\n                idx = stack.pop()\n                answer[idx] = i - idx\n            stack.append(i)\n        return answer
