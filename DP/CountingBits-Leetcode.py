class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]* (n+1)
        offset=1
        for i in range(1,n+1):
            if offset*2==i:
                offset=i
            dp[i]=1+dp[i-offset]
        return  dp
        

https://leetcode.com/problems/counting-bits/solutions/1808298/python-recursive-and-dynamic-solution-detailed-explaination-o-n

https://leetcode.com/problems/pascals-triangle/solutions/4635105/beats-95-pythonmadeeasy-recursion-optimal-solution

https://leetcode.com/problems/pascals-triangle/solutions/4016726/beats-100-drawing-with-simple-explanation

https://leetcode.com/problems/pascals-triangle/solutions/4017545/bottom-up-tabulation-dynamic-programming-in-python3

https://algo.monster/liteproblems/1025