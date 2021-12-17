# Question#03
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        #solution leetcode:605
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        num=0
        temp=[0]+flowerbed+[0]
        for i in range(1,len(temp)-1):
            if(temp[i-1]==0 and temp[i+1]==0 and temp[i]==0):
                temp[i]=1
                num+=1
        if(num>=n):
            return True
        else:
            return False