class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        res = []
        painted = {}
        
        for start, end in paint:
            work = 0
            
            while start < end:
                if start in painted:
                    prev_end = painted[start]
                    
                    painted[start] = max(painted[start], end)
                    start = prev_end
                else:
                    painted[start] = end
                    start += 1
                    work += 1
                    
            res.append(work)
            
        return res
