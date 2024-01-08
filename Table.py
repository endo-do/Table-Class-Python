def sort_dict(d):
   return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(d.items())}

class Table:
    def __init__(self, content, space_left=1, space_right=1, orientation="left", 
                empty_cells=["", "#empty"], empty_lists=["", "#empty"], empty_dicts=["", "#empty"], replace_empty="",
                header={"row":[]}, fill_with_empty_rows=False, fill_with_empty_columns=False):
        
        self.content = content 
        self.space_left = space_left 
        self.space_right = space_right 
        self.orientation = orientation 
        self.empty_cells = empty_cells
        self.empty_lists = empty_lists
        self.empty_dicts = empty_dicts
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
            if self.fill_with_empty_rows:
                rows = [key for d in self.content for key in d]
                for row in range(rows[0], rows[-1]):
                    if row not in rows:
                        self.content.append({row:[]})
            new_content = []
            self.content = sorted(self.content, key=lambda d: next(iter(d)))
            for line in self.content:
                
                if any(str(val) in self.empty_dicts for val in line.values()):
                    new_content.append([""])
                else:
                    new_content.extend([char for char in line.values()])

            self.content = new_content

        elif self.structure == "list_in_dict":
            if self.fill_with_empty_rows:
                rows = [list(self.content.keys())]
                for row in range(rows[0], rows[-1]):
                    if row not in rows:
                        self.content[row] = []
            new_content = []
            self.content = dict(sorted(self.content.items()))
            for line in self.content.values():
                if line in self.empty_lists:
                    new_content.append(self.replace_empty)
                else:
                    new_content.append(line)
            
            self.content = new_content

        elif self.structure == "dict_in_dict":
            if self.fill_with_empty_rows:
                rows = list(self.content.keys())
                for row in range(rows[0], rows[-1]):
                    if row not in rows:
                        self.content[row] = {}
            if self.fill_with_empty_columns:
                for key, row in self.content.items():
                    columns = list(row.keys())
                    if len(columns) >= 2:
                        for col in range(columns[0], columns[-1]):
                            if col not in columns:
                                self.content[key][col] = ""
            new_content = []
            self.content = {k: dict(sorted(v.items())) if isinstance(v, dict) else v for k, v in sorted(self.content.items())}
            for line in self.content:
                if self.content[line] in self.empty_dicts:
                    new_line = [""]
                else:
                    new_line = []
                    for cell in self.content[line].values():
                        if str(cell) in self.empty_cells:
                            cell = self.replace_empty
                        new_line.append(cell)
                new_content.append(new_line)
            
            self.content = new_content

        self.rows = len(self.content)
        
        for row in self.content:
            if len(row) > self.columns: 
                self.columns = len(row)

        if "row" in self.header:
            if self.header["row"] == []:
                self.header["row"] = [f"{index}." for index in range(self.columns)]
                self.rows += 1
            
            self.content = [self.header["row"]] + self.content
        
        for index, row in enumerate(self.content):
            if row == []:
                for i in range(self.columns):
                    self.content[index] = ["" for i in range(self.columns)]

        for row in self.content:
            while len(row) < self.columns:
                row.append("")

        new_content = []

        for line in self.content: 
            new_content.append([str(char) if char not in self.empty_cells else self.replace_empty for char in line])

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
            
            if row_index == 0 and "row" in self.header: 
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
           
