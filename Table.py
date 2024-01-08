
def sort_dict(d):
   return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(d.items())}

class Table:
    def __init__(self, content, space_left=1, space_right=1, orientation="left", 
                empty_cell="", empty_dict_value="", empty_list="", empty_dict="", replace_empty="",
                header=True, fill_with_empty_rows=False, fill_with_empty_columns=False):
        self.content = content 
        self.space_left = space_left 
        self.space_right = space_right 
        self.orientation = orientation 
        self.empty_cell = empty_cell 
        self.empty_dict_value = empty_dict_value
        self.empty_list = empty_list
        self.empty_dict = empty_dict
        self.replace_empty = replace_empty
        self.header = header
        self.fill_with_empty_rows = fill_with_empty_rows
        self.fill_with_empty_columns = fill_with_empty_columns
        self.orientation = orientation

        self.rows = 0 
        self.columns = 0 
        self.max_chars = [] 

    def main(self):

        if self.orientation not in ["left", "right"]:
            self.orientation = "left"

        for arg in [self.header, self.fill_with_empty_columns, self.fill_with_empty_rows]:
            if arg != True and arg != False:
                arg = False

        str1 = type(self.content) 

        if str1 is list:
            str2 = type(self.content[0]) 
        elif str1 is dict:
            str2 = type(next(iter(self.content.values()))) 

        self.structure = f"{str2.__name__}_in_{str1.__name__}"
        
        if self.structure == "dict_in_list":
            self.content = sorted(self.content, key=lambda d: next(iter(d)))
            new_content = []

            for line in self.content:
                
                if any(str(val) == str(self.empty_dict) for val in line.values()):
                    new_content.append([""])
                else:
                    new_content.extend([char for char in line.values()])

            self.content = new_content

        elif self.structure == "list_in_dict":
            self.content = dict(sorted(self.content.items()))
            new_content = []
            for line in self.content.values():
                if list(line) == [self.empty_list]:
                    new_content.append([""])
                else:
                    new_content.append(line)
            
            self.content = new_content

        elif self.structure == "dict_in_dict":
            self.content = {k: dict(sorted(v.items())) if isinstance(v, dict) else v for k, v in sorted(self.content.items())}
            new_content = []

            for line in self.content:
                if self.content[line] == {self.empty_dict}:
                    new_line = [""]
                else:
                    new_line = []
                    for cell in self.content[line].values():
                        if str(cell) == str(self.empty_cell):
                            cell = ""
                        new_line.append(cell)
                new_content.append(new_line)
            
            self.content = new_content

        self.rows = len(self.content) 
        
        for row in self.content:
            if len(row) > self.columns: 
                self.columns = len(row)

        for index, row in enumerate(self.content):
            if row == []:
                for i in range(self.columns):
                    self.content[index] = ["" for i in range(self.columns)]

        for row in self.content:
            while len(row) < self.columns:
                row.append("")

        new_content = []

        for line in self.content: 
            new_content.append([str(char) if char != self.empty_cell else self.replace_empty for char in line]) 

        self.content = new_content 

        for cell in range(self.columns): 
            self.max_chars.append(0)
        

        for row in self.content: 
            active_column = 0
            for cell in row:
                if len(str(cell)) > self.max_chars[active_column]: 
                    self.max_chars[active_column] = len(str(cell))
                active_column += 1

        column_index = 0  
        
        print("╔", end="") 
        
        for column in self.max_chars:
            print("═" * self.space_left, end="")  
            print("═" * column, end="")  
            print("═" * self.space_right, end="")  
            
            if column_index == len(self.max_chars) - 1:  
                print("╗")
            else:
                print("╤", end="")  
    
            column_index += 1  

        row_index = 0  
        
        for row in range(self.rows): 
    
            print("║", end="") 
            
            column_index = 0

            for column in range(self.columns):
                
                spacebar_counter = self.max_chars[column] - len(str(self.content[row][column])) 
                
                text = str(self.content[row][column])

                if self.orientation == "left": 
                    content = text + str(spacebar_counter * " ")  
                elif self.orientation == "right":
                    content = str(spacebar_counter * " ") + text 

                print(" " * self.space_left, end="")
                print(content, end="")
                print(" " * self.space_right, end="")
                
                if column_index == self.columns - 1: 
                    print("║") 
                else:
                    print("│", end="") 

                column_index += 1  
            
            if row_index == 0 and self.header: 
                left_border = "╠"
                connection = "═"
                right_border = "╣"
                cross_connection = "╪"

            elif row_index == self.rows - 1:
                left_border = "╚"
                connection = "═"
                right_border = "╝"
                cross_connection = "╧"

            else:
                left_border = "╟"
                connection = "─"
                right_border = "╢"
                cross_connection = "┼"

            print(left_border, end="") 
                
            column_index = 0

            for column in self.max_chars: 
                print(connection * self.space_left, end="") 
                print(column * connection, end="") 
                print(connection * self.space_right, end="") 
                if column_index == len(self.max_chars) - 1: 
                    print(right_border)
                else:
                    print(cross_connection, end="") 

                column_index += 1

            row_index += 1  

t = Table({1:[1, 2, 3, 4], 3:["a", " ", "hello", "#empty"], 6:["#empty"], 5:[2, 4, 6, 8], 4:[]}, replace_empty="", empty_cell="#empty", header=True)
t.main()