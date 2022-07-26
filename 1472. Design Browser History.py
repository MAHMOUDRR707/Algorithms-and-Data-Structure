class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.result =  [self.homepage]
        self.n =  0
    def visit(self, url: str) -> None:
        self.n +=1
        self.result =  self.result[:self.n] + [url]
         
    def back(self, steps: int) -> str:
        self.n =  max(0,self.n - steps)
        x =  self.result[self.n]        
        return x

    def forward(self, steps: int) -> str:
        self.n =  min(len(self.result)-1,self.n+steps)
        x =  self.result[self.n] 
        #print(self.result)
        return x


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
