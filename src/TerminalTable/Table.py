### The Table Class
        
class Table:
    def __init__(
        self,
        content,
        space_left=1,
        space_right=1,
        space_left_table=0,
        orientation="left",
        min_width=None,
        max_width=None,
        same_sized_cols=False,
        empty_cells=["", "#empty"],
        empty_lists=[[], [""], ["#empty"]],
        replace_empty="",
        col_header=False,
        row_header=False
    ):
        
        """
        Initialize a Table object with specified parameters

        Args:
        - content: content of the table in a list_in_list, list_in_dict, dict_in_list or dict_in_dict structure
        - space_left: int: space from the content of a cell to its border on the left side
        - space_right: int: space from the content of a cell to its border on the right side
        - orientation: str: "left" or "right" | orientates the content to the left or to the right side of the cell
        - min_width: int: minimum width of a cell. spaces will be added when to short
        - max_width: int: maximum width of a cell. content will be shortened when to long
        - same_sized_cols: bool: toggles same width for each column
        - fill_with_empty_rows: bool: toggles filling empty rows for every not specified row in content
        - fill_with_empty_columns: bool: toggles filling empty columns for every not specified column in content
        - empty_cells: list: specifies what is considered as an empty cell
        - empty_lists: specifies what is considered as an empty list
        - empty_dicts: specifies what is considered as an empty dict
        - replace_empty: str: replaces empty cells and the content of empty lists and dicts with this str
        - col_header: bool: if true first collumn will be seperated and displayed as header
        - row_header: bool: if true first row will be seperated and displayed as header
        """

        self.content = content
        self.space_left = space_left 
        self.space_right = space_right 
        self.orientation = orientation 
        self.min_width = min_width 
        self.max_width = max_width
        self.same_sized_cols = same_sized_cols
        self.empty_cells = empty_cells 
        self.empty_lists = empty_lists 
        self.replace_empty = replace_empty 
        self.col_header = col_header
        self.row_header = row_header
        self.space_left_table = space_left_table

        self.check_types()
    
    def check_types(self):
        if type(self.content) is not list:
            raise Exception("ValueError: self.content has to be a list")
        if type(self.content[0]) is not list:
            raise Exception("ValueError: self.content has to be a 2 dimensional list")
        for value in (self.space_left, self.space_right, self.min_width, self.max_width):
            if type(value) is not int and value is not None:
                raise Exception(f"Value Error: {value} should be an integer")
        for value in (self.same_sized_cols, self.row_header, self.col_header):
            if type(value) is not bool:
                raise Exception(f"Value Error: {value} should be a bool")
        for value in (self.empty_cells, self.empty_lists):
            if type(value) is not list:
                raise Exception(f"Value Error: {value} is not a list")
        if type(self.replace_empty) is not str:
            raise Exception(f"Value Error: self.replace_empty is not a str")
    
    def clean_data(self):
        for index, row in enumerate(self.content):
            if row in self.empty_lists:
                self.content[index] = [self.replace_empty]
            else:
                for index2, cell in enumerate(row):
                    if cell in self.empty_cells:
                        self.content[index][index2] = self.replace_empty
            while len(row) < max([len(i) for i in self.content]):
                self.content[index].append(self.replace_empty)

    def get_content(self):
        return self.content

    def get_row(self, row):
        try:
            return self.content[row]
        except IndexError:
            raise Exception(f"IndexError: row '{row}' does not exist")
        
    def get_column(self, column):
        try:
            return [i[column] for i in self.content]
        except IndexError:
            raise Exception(f"IndexError: column '{column} does not exist'")
    
    def get_cell(self, row, column):
        try:
            return self.content[row][column]
        except IndexError:
            raise Exception(f"IndexError: cell '{row}x{column}' does not exist")
    
    def replace_content(self, content):
        if type(content) is list and type(content[0]) is list:
            self.content = content
        else:
            raise Exception(f"ValueError: content has to be in a list format")
            
    def replace_column(self, index, content):
        try:
            for row_index, i in enumerate(content):
                self.content[row_index][index] = i
        except IndexError:
            raise Exception(f"IndexError: column '{index}' does not exist")

    def replace_row(self, index, content):
        self.content[index] = content

    def replace_cell(self, col, row, content):
        self.content[row][col] = content

    def add_row(self, row, content):
        if str(row) == "-1":
            row = "end"
        elif row < 0:
            row += 1
        
        if row == "end":
            self.content.append(content)
        else:
            self.content.insert(row, content)

    def add_column(self, column, content):
        if str(column) == "-1":
            column = "end"
        elif column < 0:
            column += 1
        for index, i in enumerate(content):
            if column == "end":
                self.content[index] = i
            else:
                self.content[index].insert(column, i)

    def remove_row(self, row):
        self.content.pop(row)

    def remove_column(self, column):
        for i in self.content:
            i.pop(column)

    def sort_col(self, col, reverse=False):
        column = [i[col] for i in self.content]
        column = sorted(column, reverse=reverse)
        for index, i in enumerate(column):
            self.content[index] = i
    
    def sort_row(self, row, reverse=False):
        self.content[row] = sorted(self.content[row], reverse=reverse)
    
    def sort_on_col(self, column, reverse=False):
        self.content = sorted(self.content, key=lambda x: x[column], reverse=reverse)

    def sort_on_row(self, row, reverse=False):
        to_be_sorted_row = self.get_content()[row]
        other_rows = [sublist for i, sublist in enumerate(self.get_content()) if i != row]

        sorted_indices = sorted(range(len(to_be_sorted_row)), key=lambda k: to_be_sorted_row[k], reverse=reverse)

        sorted_row = [to_be_sorted_row[i] for i in sorted_indices]
        sorted_other_rows = [[lst[i] for i in sorted_indices] for lst in other_rows]

        sorted_other_rows.insert(row, sorted_row)

        self.content = sorted_other_rows

    def swap_cols_rows(self):
        self.content = list(map(list, zip(*self.content)))
    
    def display(self):
        
        self.clean_data()

        self.rows = len(self.content)
        self.columns = 0
        for row in self.content:
            if len(row) > self.columns: 
                self.columns = len(row)
        
        self.max_chars = []
        for cell in range(self.columns): 
            self.max_chars.append(0)
        for row in self.content: 
            active_column = 0
            for cell in row:
                if len(str(cell)) > self.max_chars[active_column]: 
                    self.max_chars[active_column] = len(str(cell))
                active_column += 1

        if self.min_width != None:
            for index, i in enumerate(self.max_chars):
                if self.min_width > int(i):
                    self.max_chars[index] = self.min_width
        
        if self.max_width != None:
            for index, i in enumerate(self.max_chars):
                if self.max_width < int(i):
                    self.max_chars[index] = self.max_width

        if self.same_sized_cols:
            self.max_chars = [max(self.max_chars) for i in self.max_chars]
        
        self.header = {"col":[], "row":[]}

        column_index = 0  
        print(self.space_left_table * " ", end="")
        print("╔", end="")
        for column in self.max_chars:
            print("═" * self.space_left, end="")  
            print("═" * column, end="")  
            print("═" * self.space_right, end="")  
            
            if column_index == len(self.max_chars) - 1:  
                print("╗")
            
            else:
            
                if self.col_header and column_index == 0:
                    print("╦", end="")
            
                else:
                    print("╤", end="")  
            
            column_index += 1  
        row_index = 0
        
        for row in range(self.rows): 
            print(self.space_left_table * " ", end="")
            print("║", end="") 
            column_index = 0

            for column in range(self.columns):

                spacebar_counter = self.max_chars[column] - len(str(self.content[row][column])) 
                text = str(self.content[row][column])

                if len(text) > self.max_chars[column_index]:

                    if self.max_chars[column_index] == 2:
                        text = ".."
                    elif int(self.max_chars[column_index]) == 3:
                        text = [i for i in text]
                        text = text[0]
                        text += ("..")
                    
                    elif int(self.max_chars[column_index]) >= 3:
                        text = [i for i in text]
                        text = text[:int(self.max_chars[column_index])-2]
                        text.append("..")
                        textstr = ""
                        for i in text:
                            textstr += i
                        text = textstr
                    spacebar_counter = 0
                
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
                    if self.col_header and column_index == 0:
                        line = "║"
                    else:
                        line = "│" 
                    print(line, end="")
                column_index += 1  
            
            if row_index == 0 and "row" in self.header: 
                left_border = self.space_left_table * " " + "╠"
                connection = "═"
                right_border = "╣"
                cross_connection = "╪"

            elif row_index == self.rows - 1:
                left_border = self.space_left_table * " " + "╚"
                connection = "═"
                right_border = "╝"
                cross_connection = "╧"

            else:
                left_border = self.space_left_table * " " + "╟"
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
                
                    if self.col_header and column_index == 0:
                
                        if row_index == self.rows - 1:
                            print("╩", end="")
                
                        elif self.row_header and row_index == 0:
                            print("╬", end="")
                
                        else:
                            print("╫", end="")
                
                    else:
                        print(cross_connection, end="") 

                column_index += 1

            row_index += 1
