from typing import List
def maximumWealth(self, accounts: List[List[int]]) -> int:
    ret = []        
    for val in accounts:
        x = 0
        for item in val:
            x = x + item
        ret.append(x)
    return max(ret)

maximumWealth(self,accounts=[[1,2,3],[3,2,1]])