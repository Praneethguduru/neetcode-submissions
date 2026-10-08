class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        left_wall = right_wall = 0
        for i in range(len(height)):
            j = -i-1
            left_max[i] = left_wall
            right_max[j] = right_wall

            left_wall = max(left_wall, height[i])
            right_wall = max(right_wall, height[j])

        summ = 0
        for i in range(len(height)):
            p = min(left_max[i], right_max[i])

            summ += max(0, p - height[i])
        return summ