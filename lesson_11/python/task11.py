class BinarySearch:
    __FAIL = "fail"
    __SEARCH = "search"
    __SUCCESS = "success"

    __states_to_result = {
        __SEARCH : 0,
        __FAIL : -1,
        __SUCCESS : 1
    }

    @staticmethod
    def get_fail():
        return BinarySearch.__FAIL

    @staticmethod
    def get_search():
        return BinarySearch.__SEARCH
    
    @staticmethod
    def get_success():
        return BinarySearch.__SUCCESS

    def __init__(self, array):
        self.__step_state = BinarySearch.get_search()
        self.array = array
        self.left = 0
        self.right = len(array) - 1
    
    def GetState(self):
        return self.__step_state
    
    def Step(self, n):
        if len(self.array) == 0:
            self.__step_state = BinarySearch.__FAIL
            return
        
        middle = (self.left + self.right) // 2
        target = self.array[middle]

        if self.array[middle] == n:
            self.__step_state = BinarySearch.__SUCCESS
            return
        
        if self.left == self.right:
            self.__step_state = BinarySearch.__FAIL
            return
        
        if target >= n:
            self.right = middle - 1
        
        if target < n:
            self.left = middle + 1

        

    def GetResult(self):
        return self.__states_to_result[self.__step_state]