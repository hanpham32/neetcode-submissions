class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [0] * N
        postfix = [0] * N
        # cacl. prefix
        for i in range(N):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = nums[i-1] * prefix[i-1]
        # print(f"debug=== prefix: {prefix}")
        #calc. postfix
        for i in range(N - 1, -1, -1):
            if i == N - 1:
                postfix[i] = 1
            else:
                postfix[i] = postfix[i+1] * nums[i+1]
            # postfix.insert(0, nums[i] * postfix[0])  --> insert() is too slow
        # print(f"debug=== postfix: {postfix}")
        return [prefix[i] * postfix[i] for i in range(N)]