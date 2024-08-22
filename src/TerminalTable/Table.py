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
    
    def display(self):

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
