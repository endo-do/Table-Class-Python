# Terminal Table Python
A simple Python Class for displaying information as a customizable table in the console

The following is also documented in the code itself

### Note: Working with indexes:

- Indexes in the Table Class work the exact same ways as in standard python lists
    - Index 0 returns the first element and -1 returns the last

- An index will be adjusted to the active headers accordingly
    - This means that the header dont count as a row or column
    - E.g. the first row is still accesible with index 0 while a row header is active

## Parameters of the Table Class:

The following are parameters of the Table Class

- 'content': The content of the table. Supported data structures are listed below in the Data Structure Sections

- 'space_left' and 'space_right' (int): Add spaces at the left and right side of each cell's content
    - Default set to '1'

- 'orientation' (str): Orientates the cell's content to either the right ('right') or left ('left') side of the cell.
    - Default set to 'left'

- 'min_width' and 'max_width' (int): Set a minimum or maximum width for the cells. 
    - If content isn't as large as min_width spaces will be added.
    - If content is larger than max_width some of the content will be cut off and replaced with '..'
    - Default set to 'None'

- 'same_sized_cols' (bool): Sets the max_width for each cell to the largest width of the table to create a evenly spaced table
    - Default set to 'False'

- 'fill_with_empty_rows' and 'fill_with_empty_cols' (bool): fills not specified rows/cols with empty ones
    - e.g. if content is given as dict = {1:[a, b, c], 3:[1, 2, 3]}
    - A empty row at index 1 would be added
    - Default set to 'True'

- 'empty_cells', 'empty_lists' and 'empty_dicts' (list): Defines what cells/lists/dicts will be treated as empty
    - Default set to '["", "#empty"], [[], [""], ["#empty"]] and [{}, {""}, {"#empty"}]

- 'replace_empty' (str) defines with what empty cells/lists/dicts will be replaced
    - Default set to ""

- 'header' ([{header_type:header_content}, ..]) defines the active headers
    - header_types are 'row' and 'col'
    - header_content can be given as list or dict
    - e.g. {"row":["Name", "Age", "Gender"]}
    - Default set to {}

## Functions:

### Add Content:

- The functions 'add_row' and 'add_column' are used for adding rows and columns
- They both take 'index' and 'row'/'col' as arguments
- E.g. add_row(0, [1, 2, 3, 4]) would add a new row at position 0 with the values 1, 2, 3 and 4

### Remove Content:

- The functions 'remove_row' and 'remove_column' are used for removing rows and columns
- They both take 'index' as an argument
- E.g. remove_row(0) would remove the first row

### Replacing Content:

- The functions 'replace_row', 'replace_column' and 'replace_cell' are used for replacing rows, column and cells
- 'replace_row' and 'replace_column' both take 'index' and 'row'/'col' as arguments.
- 'replace_cell' takes 'row', 'col' and 'replace' as arguments
    - if 'row', 'col' or 'replace' were not specified the row/col/cell will be replaced with standard 'replace_empty'
- E.g. replace_cell(-1, 0, "hello") would replace the first element in the last row with "hello"

### Get Content:

- The functions 'get_col', 'get_row' and 'get_content' are used to get content from the Table

- 'get_col' and 'get_row' each have 'index' as an argument

- 'get_content' returns the whole table without the headers and doesnt need an argument

- E.g. get_col(4) would return the fifth column

### Headers:

- There are 2 types of headers: a row ('row') and a column ('col') one

    - row header: adds an extra row at the start of the content
        - E.g. [[h1, h2, h3], [1, 2, 3], [4, 5, 6], [7, 8, 9]]

    - column header: adds a header at the start of each row
        - E.g. [[h1, 1, 2, 3], [h2, 4, 5, 6], [h3, 7, 8, 9]]

- The function 'conf_header' is used to configure the headers

- It takes the following parameters:

    - header (str): Defines the type of header that is being configured

    - action (str): Defines what should be done with the header
        
        - 'add' adds the header (if already active overwrites the current one)
            - E.g. if 'row' is active conf_header('row', 'add', ["e.g."]) will overwrite the current row header
        
        - 'replace' does the exact same 'add'

        - 'edit' overwrites the with index specified row/col in the header

        - 'remove' removes the header

    - index (int): Is used when editing a header to specify which row or column should be replaced inside the header

        - Default is 'None'

    - content (list, dict or str): Defines the content that will be used to add or replace the header or part of the header
        
        - if adding or replacing the content should be a list or dict

        - if editing a part of a header the content should be a str

        - Default is 'None'

    - E.g. conf_header("row", "add", ["Name", "Adress", "Gender]) adds a new 'row' header
    
    - E.g. conf_header("row", "edit", content="Age", index=1) would swap the "Adress" with "Age" in the 'row' header
    
    - E.g. conf_header("row", "remove") would remove the 'row' header

### Other Functions:

#### Display:

- The 'display' function simply displays the table at its current state

#### Swap Cols with Rows:

-  The 'swap_cols_rows' functions swaps all the rows with the columns including the headers

- E.g. the table [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

## Data Structures:

The table class supports different data structures when adding or editing content to the table or configuring the headers

Supported structures for adding or replacing rows, columns or headers:

- list:
    - E.g. [a, b, c]

- dict:
    - E.g. {1:a, 2:b, 3:c}

Supported structures for the whole table:

- list_in_list:
    - E.g. [[a, b, c], [d, e, f], [g, h, i]]

- list_in_dict:
    - E.g.g {1:[a, b, c], 2:[d, e, f], 3:[g, h, i]}

- dict_in_list:
    - [{1:a, 2:b, 3:c}, {1:d, 2:e, 3:f}, {1:g, 2:h, 3:i}]

- dict_in_dict:
    - {1:{1:a, 2:b, 3:c}, 2:{1:d, 2:e, 3:f}, 3:{1:g, 2:h, 3:i}}

## Sources:

- Box Drawing Characters: https://en.wikipedia.org/wiki/Box-drawing_character
