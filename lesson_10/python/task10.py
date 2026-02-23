class ksort:
    # max -> 800 values
    # init row: AMN
    # hash_A = max_int_diff_value_of_char * 100 -> 700
    # hash_N = max_int_digit * 10 -> 90
    # hash_M = max_int_digit -> 9
    # 799 indexes -> 800 values
    def __init__(self):
        self.___A_POSITIONING = 100
        self.___M_POSITIONING = 10
        self.___N_POSITIONING = 1

        self.__AMOUNT_VALUES = 800
        self.items = [None] * self.__AMOUNT_VALUES
    
    # mem = O(1), t = O(1)
    def hash(self, row : str) -> int:
        if not self.valid_row(row):
            return -1
        
        return sum([(ord(row[0]) - ord('a')) * self.___A_POSITIONING, int(row[1]) * self.___M_POSITIONING, int(row[2]) * self.___N_POSITIONING])
    
    # mem = O(1), t = O(1)
    def valid_row(self, row : str) -> bool:
        if len(row) != 3:
            return False
        
        valid_letters, valid_digits = set('abcdefgh'), set('0123456789')  
        
        return row[0] in valid_letters and row[1] in valid_digits and row[2] in valid_digits 
    
    # mem = O(1), t = O(1)
    def index(self, s : str) -> int:
        return self.hash(s)

    # mem = O(1), t = O(1)
    def add(self, s : str) -> bool:
        hash = self.hash(s)
        if hash == -1:
            return False
        
        self.items[hash] = s
        
        return True