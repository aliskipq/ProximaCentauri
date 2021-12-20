class Solution(object):
    #solution 1491. Average Salary Excluding the Minimum and Maximum
    def average(self, salary):
        #solution of leetcode_1491: 
        salary.remove(max(salary))
        salary.remove(min(salary))
        add=0.0
        for i in range(len(salary)):
            add+=salary[i]
        avg = add/len(salary)
        return avg
        
    def minimumAbsDifference(self, arr):
        #solution leetcode:1200 Minimum Absolute Difference  
        arr.sort()
        mini=[]
        for i in range(len(arr)-1):
            mini.append(arr[i+1]-arr[i])
        smallest = min(mini)
        result=[]
        for index,num in enumerate(mini):
            if num==smallest:
                result.append([arr[index],arr[index+1]])
        return result
        
    def canPlaceFlowers(self, flowerbed, n):
        #solution leetcode:605 Can Place Flowers
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