from collections import defaultdict
import math
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = 0
        freq = defaultdict(int)
        even = []
        odd =[]
        for num in digits:
            freq[num] +=1 
    
        
        for key in freq:
            if key%2 ==0:
                even.append(key)
            else:
                odd.append(key)
            
        if 0 in freq:
            even.remove(0)
        
        n = len(even) + len(odd)
        for i in range(len(even)):
            taken = False
            freq[even[i]] -=1 
            if freq[even[i]] == 0:
                taken = True 
                n -=1 
                
            if freq[even[i]] >= 2:
                count +=1

            count += 2*math.comb(n,2)
            for key,value in freq.items():
                if value >=2 and key!=even[i] and key!= 0:
                    count+=1 

            if 0 in freq:
                count+= n

            freq[even[i]]+=1 
            if taken:
                n+=1 
        
        if 0 not in freq:
            return count 
        
        count+= 2*math.comb(n,2)
        for key, value in freq.items():
            if value >= 2 and key !=0:
                count+=1 

        if freq[0] >=2: 
            count+= n   
        return count