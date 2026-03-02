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
        self.Left = 0
        self.Right = 0
        
        if len(array) == 0:
            self.__step_state = BinarySearch.__FAIL
            return
        
        self.__step_state = BinarySearch.__SEARCH
        self.Right = len(array) - 1
    
    def GetState(self):
        return self.__step_state
    
    # mem = O(1), t = O(1)
    def __check_element_with_possible_fail(self, target) -> str:
        if self.array[self.Left] == target or self.array[self.Right] == target:
            return BinarySearch.__SUCCESS
        
        return BinarySearch.__FAIL
    
    # mem = O(1), t = O(1)
    def Step(self, n):
        if self.__step_state != BinarySearch.__SEARCH:
            return
        
        middle = (self.Left + self.Right) // 2
        target = self.array[middle]
        
        if target == n:
            self.__step_state = BinarySearch.__SUCCESS
            return
        
        if n < target:
            self.Right = middle - 1
        
        if n > target:
            self.Left = middle + 1
        
        if abs(self.Right - self.Left) <= 1:
            self.__step_state = self.__check_element_with_possible_fail(n)
            return
        
    # mem = O(1), t = O(1)
    def GetResult(self):
        return self.__states_to_result[self.__step_state]