class SummaryRanges:

    def __init__(self):
        self.head   = {}
        self.ranges = {}
        
    def find(self, n) :
        if self.head[n] == n : 
            return n
        else :
            self.head[n] = self.find(self.head[n])
            return self.head[n]
        
    def addNum(self, value: int) -> None:
        
        if value not in self.head : 
            casel = value-1 in self.head
            caser = value+1 in self.head
            
            if casel and caser :
                self.head[value+1] = self.find(value-1)
                self.head[value] = self.head[value+1]
                
                self.ranges[self.head[value-1]][1] =  self.ranges[value+1][1]
                                                  
                del self.ranges[value+1]
                
            elif casel :
                
                self.head[value] = self.find(value-1)                
                self.ranges[self.head[value]][1] = value
                
            elif caser :
                self.head[value] = value
                self.head[value+1] = value
                
                self.ranges[value] = [value,self.ranges[value+1][1]]

                del self.ranges[value+1]
                
            else :
                self.head[value] = value
                self.ranges[value] = [value,value]

            
            
    def getIntervals(self) :
        return sorted(list(self.ranges.values()))
            


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
