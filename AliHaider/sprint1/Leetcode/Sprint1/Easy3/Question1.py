# Question#01:
class Solution(object):
    def minimumAbsDifference(self, arr):
        #solution leetcode:1200
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


