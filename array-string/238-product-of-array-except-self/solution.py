class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        answer = []

        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] * nums[i-1])

        for i in range(len(nums)-2, -1, -1):
            suffix.append(suffix[len(nums) - i - 2] * nums[i+1])
        suffix.reverse()

        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])
        
        return answer