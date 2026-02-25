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
        self.array = array
        self.left = 0
        self.right = 0
        
        if len(array) == 0:
            self.__step_state = BinarySearch.__FAIL
            return
        
        self.__step_state = BinarySearch.__SEARCH
        self.right = len(array) - 1
    
    def GetState(self):
        return self.__step_state
    
    def __check_element_with_possible_fail(self, target) -> str:
        if self.array[self.left] == target or self.array[self.right] == target:
            return BinarySearch.__SUCCESS
        
        return BinarySearch.__FAIL
    
    def Step(self, n):
        if self.__step_state != BinarySearch.__SEARCH:
            return
        
        middle = (self.left + self.right) // 2
        target = self.array[middle]
        
        if self.right - self.left == 1 or self.right == self.left:
            self.__step_state = self.__check_element_with_possible_fail(n)
            return
        
        if target == n:
            self.__step_state = BinarySearch.__SUCCESS
            return
        
        if n < target:
            self.right = middle - 1
        
        if n > target:
            self.left = middle + 1
        
        
    def GetResult(self):
        return self.__states_to_result[self.__step_state]