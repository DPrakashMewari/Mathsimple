import math
from math import sqrt

class Numbers:
    def isprime(self,num):
        if num <1:
            return False
        for i in range(2,int(sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    def isArmstrong(self,num):
        res,n = 0,num
        while(num>0):
            rem = num%10
            res = res +(rem*rem*rem)
            num = num//10
        return n==res
              

