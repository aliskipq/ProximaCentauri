# Question#02
class Solution(object):
    def average(self, salary):
        #solution of leetcode_1491: 
        salary.remove(max(salary))
        salary.remove(min(salary))
        add=0.0
        for i in range(len(salary)):
            add+=salary[i]
        avg = add/len(salary)
        return avg
