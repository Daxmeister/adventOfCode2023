# Turn every row into an objekt
# Have attribute "possible"=ture/false
# Create add method for objects where they only add their id if possible

class Game():
    
    
    def __init__(self, row):
        self.game_number = row.strip().split(":")[0].split()[1] #Chained stuff that gets the number..
        self.all_rounds_list = row.strip().split(":")[1].split(";")
        self.all_rounds_dic = self.create_dictionary(self.all_rounds_list)
        
    def create_dictionary(self, list_w_rounds):
        dic_w_colors = {"green": [], "blue": [], "red": []}
        for round in list_w_rounds:
            list_w_color_amounts = round.split(",")
            for color in list_w_color_amounts:
                color = color.strip()
                dic_w_colors[color.split()[1].strip()].append(int(color.split()[0]))
        return dic_w_colors
        
    
    def __str__(self):
        return str(self.all_rounds_dic)
        
    
    def find_largest_of_each_color(self):
        dic_of_max = {"green": max(self.all_rounds_dic["green"]), "blue": max(self.all_rounds_dic["blue"]), 
                      "red": max(self.all_rounds_dic["red"])}
        return dic_of_max
    
    def see_if_largest_is_less_than(self, dictionary_with_limits):
        possible_result = True
        dic_with_max = self.find_largest_of_each_color()
        list_of_colors = ["green", "blue", "red"]
        for color in list_of_colors:
            if dictionary_with_limits[color] < dic_with_max[color]:
                possible_result = False
        return possible_result
        
    def add_if_possible(self, dictionary_with_limits):
        if self.see_if_largest_is_less_than(dictionary_with_limits):
            return int(self.game_number)
        else:
            return 0
        
        
        
        
        
test_row = "Game 13: 1 green, 0 red, 4 blue; 2 blue, 6 green, 7 red; 3 red, 4 blue, 6 green; 3 green; 3 blue, 2 green, 1 red"

#print(test_row.strip().split(":")[1].split(";"))
dictionary_w_limits = {"green":13 , "blue": 14, "red": 12}

test_game = Game(test_row)
print(test_game.add_if_possible(dictionary_w_limits))

def run_code(file_path):
    "Goes through the file, line by line, and adds numbers"
    total_number = 0
    dictionary_w_limits = {"green":13 , "blue": 14, "red": 12}
    with open(file_path, 'r') as file:
        for line in file:
            game_object = Game(line)
            total_number += game_object.add_if_possible(dictionary_w_limits)
    return total_number

print(run_code('/Users/alakazam/Programmering/AdventOfCode/adventOfCode2023/Day 2/new_file.txt'))

