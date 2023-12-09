class Number():
    # Class variable
    class_matrix = None # TODO. BTW needs first column and row and last column and row padding with .......
    
    def __init__(self, number, row_index, first_number_index, last_number_index):
        self.value = number
        self.index_of_number = [row_index, first_number_index, last_number_index]
        self.is_adjacent_to_symbol = False # TODO
        
    def check_if_not_dot_or_int(self, character):
        if type(character) == int or character == ".":
            return False
        else:
            return True
        
    def return_list_of_characters(self, row_above_or_below):
        # Row above is True. Row below is False
        pass
        
        
    
    def calculate_if_symbols_adjacent(self):
        if self.check_if_not_dot_or_int(Number.class_matrix[self.index_of_number[0]][self.self.index_of_number[1] -1]) or self.check_if_not_dot_or_int(Number.class_matrix[self.self.index_of_number[2] + 1]):
            return True
        
        charcters_in_row_above = Number.class_matrix[self.self.index_of_number[0]]
        
        for character in charcters_in_row_above:
            if self.charcters_in_row_above(character):
                return True
        
        return False
        
        