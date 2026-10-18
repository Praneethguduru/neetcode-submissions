class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        
        M = l

        if M == 0:
            l, r = 0, n - 1
        elif target >= nums[0] and target <= nums[M - 1]:
            l, r = 0, M - 1
        else:
            l, r = M, n - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1  
