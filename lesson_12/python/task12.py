class BinarySearch:
    __FAIL = "fail"
    __SEARCH = "search"
    __SUCCESS = "success"

    __states_to_result = {
        __SEARCH : 0,
        __FAIL : -1,
        __SUCCESS : 1
    }

    __result_to_boolean = {
        -1 : False,
        1 : True
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
    
    @staticmethod
    def build_target_index(ind : int) -> int:
        return 2 ** ind - 2
    
    @staticmethod
    def build_previous_target_index(ind : int) -> int:
        return ((2 ** (ind - 1) - 2) - 2) + 1
    
    def get_galloping_search_result(self):
        return self.__result_to_boolean[self.__states_to_result[self.__step_state]]
    
    # mem = O(1), t = O(n*log(i))
    @staticmethod
    def GallopingSearch(array, n) -> bool:
        size = len(array)
        if size == 0:
            return False
        
        init_ind = 1
        target_ind = BinarySearch.build_target_index(init_ind)
        target = array[target_ind]

        while target < n:
            init_ind += 1
            target_ind = BinarySearch.build_target_index(init_ind)
            
            if target_ind >= size:
                target_ind = size - 1
                break

            target = array[target_ind]
            
        if target == n:
            return True

        setup_binary_search = BinarySearch(array)
        lower_bound, upper_bound = BinarySearch.build_previous_target_index(init_ind), target_ind
        setup_binary_search.Left, setup_binary_search.Right = lower_bound, upper_bound

        while setup_binary_search.__step_state == BinarySearch.__SEARCH:
            setup_binary_search.Step(n)
            
        if setup_binary_search.__step_state == BinarySearch.__SEARCH:
            return False
        
        return setup_binary_search.__step_state == BinarySearch.__SUCCESS