class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count = [0] * 101
        for num in nums:
            count[num] += 1
            
        for i in range(1, 101):
            count[i] += count[i - 1]
            
        final_answer = []
        for num in nums:
            if num == 0:
                final_answer.append(0)
            else:
                final_answer.append(count[num - 1])
        return final_answer