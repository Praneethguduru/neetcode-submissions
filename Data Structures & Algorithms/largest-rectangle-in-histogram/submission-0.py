class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                h, j = stack.pop()
                w = i - j
                area = max(area, h * w)
                start = j
            stack.append((height, start))
        while stack:
            h, j = stack.pop()
            w = n - j
            area = max(area, h * w)
        return area