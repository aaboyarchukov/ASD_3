class ksort:
    # max -> 800 values
    # init row: AMN
    # hash_A = max_int_diff_value_of_char * 100 -> 700
    # hash_N = max_int_digit * 10 -> 90
    # hash_M = max_int_digit -> 9
    # 799 indexes -> 800 values
    def __init__(self):
        self.__A_POSITIONING = 100
        self.__M_POSITIONING = 10
        self.__N_POSITIONING = 1
        self.__INVALID_RESULT = -1
        self.__VALID_ROW_LEN = 3

        self.__AMOUNT_VALUES = 800
        self.items = [None] * self.__AMOUNT_VALUES

        self.valid_letters, self.valid_digits = set('abcdefgh'), set('0123456789') 
    
    # mem = O(1), t = O(1)
    def hash(self, row : str) -> int:
        if not self.valid_row(row):
            return self.__INVALID_RESULT
        
        return sum([(ord(row[0]) - ord('a')) * self.__A_POSITIONING, int(row[1]) * self.__M_POSITIONING, int(row[2]) * self.__N_POSITIONING])
    
    # mem = O(1), t = O(1)
    def valid_row(self, row : str) -> bool:
        if len(row) != self.__VALID_ROW_LEN:
            return False 
        
        return row[0] in self.valid_letters and row[1] in self.valid_digits and row[2] in self.valid_digits
    
    # mem = O(1), t = O(1)
    def index(self, s : str) -> int:
        return self.hash(s)

    # mem = O(1), t = O(1)
    def add(self, s : str) -> bool:
        hash = self.hash(s)
        if hash == self.__INVALID_RESULT:
            return False
        
        self.items[hash] = s
        
        return True