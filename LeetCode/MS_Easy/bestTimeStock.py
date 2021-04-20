# ##time limit exceeded 
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profitArr = []
#         for i in range (len(prices)-1):
#             checkArr = prices[i+1::]
#             if (max(checkArr) > prices[i]):
#                 temp = max(checkArr) - prices[i]
#                 profitArr.append(temp)
#                 # print(profitArr)
#         if(len(profitArr)>=1):
#             return max(profitArr)
#         else:
#             return 0

