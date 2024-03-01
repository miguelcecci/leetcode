class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.history = []
        self.forward_list = []
        
    def visit(self, url: str) -> None:
        self.history.append(url)
        self.forward_list = []
        
    def back(self, steps: int) -> str:
        for i in range(min(steps, len(self.history))):
            self.forward_list.append(self.history[-1])
            self.history.pop()
        if len(self.history) == 0:
            return self.homepage
        return self.history[-1]
        
    def forward(self, steps: int) -> str:
        print(self.history)
        print(self.forward_list)
        if self.forward_list == []:
            if self.history == []:
                return self.homepage
            return self.history[-1]
        for i in range(min(steps, len(self.forward_list))):
            self.history.append(self.forward_list[-1])
            self.forward_list.pop()
        return self.history[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

