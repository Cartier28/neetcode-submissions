class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set() #an array that doesn't allow duplicates

        for n in nums: #loops through the indices of the elements in num
            if n in hs: # if that element is in the hashmap (seen already) its a dupe
                return True
            
            hs.add(n) #otherwise it gets added to the hashmap

        return False # no duplicates

                     
         
        



        