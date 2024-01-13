def sort_dict(d):
   return {k: sort_dict(v) if isinstance(v, dict) else v for k, v in sorted(d.items())}


def restructure(data, structure, fill_with_empty_columns=None, fill_with_empty_rows=None, empty_dicts=None, empty_lists=None, empty_cells=None, replace_empty=None):
    
    if data in empty_lists or data in empty_dicts:
        return [replace_empty]
    

    else:
        str1 = type(data) 
        
        if str1 is list:
            str2 = type(data[0]) 
        
        elif str1 is dict:
            str2 = type(next(iter(data.values()))) 
        
        if structure == "list":    
            data_structure = str1.__name__

            if data_structure == "dict":            
                columns = list(data.keys())
                columns = sorted(columns)

                if len(columns) >= 2:
                    for i in range(columns[0], columns[-1]):
                        if i not in columns:
                            data[i] = replace_empty

                data = dict(sorted(data.items()))
                data = [i for i in list(data.values())]
                
            for index, i in enumerate(data):
                if i in empty_cells:
                    data[index] = replace_empty

            return data
        
        if structure == "list_in_list":
            data_structure = f"{str2.__name__}_in_{str1.__name__}"

            if data_structure == "dict_in_list":
                
                if fill_with_empty_rows:
                    rows = [key for d in data for key in d]
                    rows = sorted(rows)
                    for row in range(rows[0], rows[-1]):
                        if row not in rows:
                            data.append({row:[]})
                
                new_content = []
                data = sorted(data, key=lambda d: next(iter(d)))

                for line in data:
                    
                    if any(str(val) in empty_dicts for val in line.values()):
                        new_content.append([replace_empty])
                    
                    else:
                        new_content.extend([char for char in line.values()])
                
                data = new_content

            elif data_structure == "list_in_dict":
                
                if fill_with_empty_rows:
                    rows = list(data.keys())
                    rows = sorted(rows)
                    for row in range(rows[0], rows[-1]):
                        if row not in rows:
                            data[row] = []
                
                new_content = []
                data = dict(sorted(data.items()))
                
                for line in data.values():
                
                    if line in empty_lists:
                        new_content.append([replace_empty])
                
                    else:
                        new_content.append(line)
                
                data = new_content

            elif data_structure == "dict_in_dict":
                
                if fill_with_empty_rows:
                    rows = list(data.keys())
                    rows = sorted(rows)
                    for row in range(rows[0], rows[-1]):
                
                        if row not in rows:
                            data[row] = {}
                
                if fill_with_empty_columns:
                
                    for key, row in data.items():
                        columns = list(row.keys())
                
                        if len(columns) >= 2:
                
                            for col in range(columns[0], columns[-1]):
                
                                if col not in columns:
                                    data[key][col] = ""
                
                new_content = []
                data = {k: dict(sorted(v.items())) if isinstance(v, dict) else v for k, v in sorted(data.items())}

                for line in data:
                
                    if data[line] in empty_dicts:
                        new_line = [replace_empty]
                
                    else:
                        new_line = []
                
                        for cell in data[line].values():
                
                            if str(cell) in empty_cells:
                                cell = replace_empty
                
                            new_line.append(cell)
                
                    new_content.append(new_line)
                
                data = new_content

            return data



class Table:
    def __init__(self, content, space_left=1, space_right=1, orientation="left", 
                empty_cells=["", "#empty"], empty_lists=[[], [""], ["#empty"]], empty_dicts=[{""}, {"#empty"}], replace_empty="",
                header={"row":[]}, fill_with_empty_rows=True, fill_with_empty_columns=True):
        
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
        self.saved_header = {}
        for i in self.header:
            self.saved_header[i] = self.header[i]
        self.rows = 0 
        self.columns = 0  
        self.header_action_col = "insert"
        self.header_action_row = "insert"    

   
    def add_row(self, index, row):
        
        if index == -1:
            index = "end"
        else:
            if index < 0:
                index += 1
            
            if "row" in self.header:
                index += 1
        
        row = restructure(row, "list", self.fill_with_empty_columns, self.fill_with_empty_rows, self.empty_dicts, self.empty_lists, self.empty_cells, self.replace_empty)
        
        if "col" in self.header:
            row.insert(0, "")
        
        if index == "end":
            self.content.append(row)
        else:
            self.content.insert(index , row)
        self.header_action_row = "update"
        self.header_action_col = "update"

   
    def add_column(self, index, column):

        if index == -1:
            index = "end"
        
        else:
            if index < 0:
                index += 1

            if "col" in self.header:
                index += 1
        
        column = restructure(column, "list", self.fill_with_empty_columns, self.fill_with_empty_rows, self.empty_dicts, self.empty_lists, self.empty_cells, self.replace_empty)
        
        if "row" in self.header:
            column.insert(0, "")
        
        for i in range(len(column)):
            if index == "end":
                self.content.append(column[i])
            else:
                self.content[i].insert(index, column[i])
        
        self.header_action_col = "update"
        self.header_action_row = "update"


    def remove_row(self, index):
        if "row" in self.header:
            index += 1
        self.content.pop(index)
        self.header_action_row = "update"
        self.header_action_col = "update"


    def remove_column(self, index):
        if "col" in self.header:
            index += 1
        for i in self.content:
            i.pop(index)
        self.header_action_row = "update"
        self.header_action_col = "update"


    def replace_cell(self, row, col, replace=None, ignore_header=True):
        if replace == None:
            replace = self.replace_cell
        if "row" in self.header and ignore_header:
            row += 1
        if "col" in self.header and ignore_header:
            col += 1
        self.content[row][col] = replace


    def swap_cols_rows(self):
        self.header_action_col = "update"
        self.header_action_row = "update"
        self.content = list(map(list, zip(*self.content)))

    
    def change_header(self, header):
        for h in list(header.keys()):
            self.saved_header[h] = restructure(header[h], "list", self.fill_with_empty_columns, self.fill_with_empty_rows, self.empty_dicts, self.empty_lists, self.empty_cells, self.replace_empty)
            if h == "row":
                self.header_action_row = "update"
            if h == "col":
                self.header_action_col = "update"

    
    def remove_header(self, header):
        if header in self.header:
            del self.header[header]
            if header == "row":
                self.content.pop(0)
            if header == "col":
                for i in self.content:
                    i.pop(0)
    
    def add_header(self, header):
        for i in list(header.keys()):
            self.saved_header[i] = header[i]
            self.header[i] = header[i]             
            if i == "col":
                self.header_action_col = "insert"
            elif i == "row":   
                self.header_action_row = "insert"


    def main(self):
        
        if self.orientation not in ["left", "right"]:
            self.orientation = "left"
        
        for arg in [self.fill_with_empty_columns, self.fill_with_empty_rows]:
        
            if arg != True and arg != False:
                arg = False
        
        self.content = restructure(self.content, "list_in_list", self.fill_with_empty_columns, self.fill_with_empty_rows, self.empty_dicts, self.empty_lists, self.empty_cells, self.replace_empty)

        if "row" in self.header:
            
            if self.header_action_row == "update":
                self.content.pop(0)
                self.header["row"] = self.saved_header["row"]
                self.header_action_row = "insert"

            if self.header_action_row == "insert":
                self.columns = 0
                
                for row in self.content:

                    if len(row) > self.columns: 
                        self.columns = len(row)

                if self.header["row"] == []:    
                    self.header["row"] = [f"{index+1}." for index in range(0, self.columns)]

                else: 
                    
                    if len(self.header["row"]) < self.columns -1 if "col" in self.header else self.columns:

                        for i in range(self.columns -1 if "col" in self.header else self.columns - len(self.header["row"])):
                            self.header["row"].append("")
             
                self.content = [self.header["row"]] + self.content
        
        if "col" in self.header:

            if self.header_action_col == "update":
            
                for i in self.content:
                    i.pop(0)
                
                self.header["col"] = self.saved_header["col"]
                self.header_action_col = "insert"

            if self.header_action_col == "insert":
            
                if self.header["col"] == []:
                    self.header["col"] = [f"{index+1}." for index in range(0, len(self.content))]

                else:

                    if len(self.header["col"]) < len(self.content):
            
                        for i in range(len(self.content) - len(self.header["col"])):
                            self.header["col"].append("")

                
                if "row" in self.header:
                    self.header["col"].pop(-1)
                    self.header["col"].insert(0, "")
                
                for index, i in enumerate(self.header["col"]):
                    self.content[index] = [i] + self.content[index]

        self.header_action_col = "nothing"
        self.header_action_row = "nothing"
        
        self.rows = len(self.content)
        self.columns = 0
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
            new_content.append([str(char) if char not in self.empty_cells else self.replace_empty for char in line])
        
        self.content = new_content 

        self.max_chars = []
        
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
            
                if "col" in self.header  and column_index == 0:
                    print("╦", end="")
            
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
                
                    if "col" in self.header and column_index == 0:
                        line = "║"
                
                    else:
                        line = "│" 
                    
                    print(line, end="")

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
                
                    if "col" in self.header and column_index == 0:
                
                        if row_index == self.rows - 1:
                            print("╩", end="")
                
                        elif "row" in self.header and row_index == 0:
                            print("╬", end="")
                
                        else:
                            print("╫", end="")
                
                    else:
                        print(cross_connection, end="") 

                column_index += 1

            row_index += 1


Table1 = Table(content=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
Table1.main()
