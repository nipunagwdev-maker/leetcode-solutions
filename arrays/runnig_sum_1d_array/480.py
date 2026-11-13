class Solution(object):
    def runningSum(self, nums):
        output = []
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            output.append(total)

        print(output)


nums = list(map(int, input().split()))
solution = Solution()
solution.runningSum(nums)
