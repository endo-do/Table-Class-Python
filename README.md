# Terminal Table Python
A simple Python Class for displaying information as a customizable table in the console

## How to use the Terminal Class

### How to specifiy Indexes correctly:

- When adding, removing or editing the content of the table, the headers dont count as a row/col so the first row will still have the index 0
- The specified index also works the same as in standart python list
    - This means you can access the first element with 0, the second with 1 and so on
    - You can also access the last element with -1, second last with -2, and so on

### Data Structures:

- The table class supports different data structures when adding or editing content to the table or configuring the headers
- Supported structures are list_in_list, list_in_dict, dict_in_list or dict_in_dict structure


### Settings of the table:

- space_left and space_right (int) add spaces at the left and right side of each cell's content
- orientation (str) is orientate the cell's content to either the right ('right') or left ('left') side of the cell
- min_width and max_width (int) set a minimum or maximum width for the cells
- same_sized_cols (bool) sets the max_width for each cell to the largest width of the table to create a evenly spaced table
- fill_with_empty_rows/cols (bool) fills not specified rows/cols with empty ones
- empty_cells/lists/dicts (list) definies what cells/lists/dicts will be treated as empty
- replace_empty (str) definies with what empty cells/lists/dicts will be replaced
- header ([{header_type:header_content}, ..]) definies the active headers
    - header_types are 'row' and 'col'

### Functions:

#### Add/Remove/Replace Content:

- You can configure the content of the table with the following functions:
    - add_row / add_column
    - replace_row / replace_column
    - remove_row / remove_column
    - replace_cell

- All these functions have an index as parameter to specify which row/col will be affected
    - the replace_cell functions take 2 arguments (row and col) instead of an index

- The add and replace functions also have a row or col as parameter to specify the content of the added or replaced row / col

#### Get Content:

- You can get specific content from the table with the following functions:
    - get_content
    - get_row / get_col
    - get_cell
    - get_header

- The get_content function return the whole table without the headers
    - To work with the full content (headers included) use the table.content variable

- The get_row and get_column functions each take an index as parameter and return the content of the specified row/col in a list

- The get_cell functions takes col and row as parameter and returns the content of the specified cell

- The get_header functions takes header as parameter which can either be 'col' or 'row' and returns the content of the specified header if active

#### Handle Headers:

- With the conf_header function you can add, remove, edit or replace the headers of the table

- It takes header, action, content and index as parameters

    - header secifies which header will be configured ('col' or 'row')

    - action definies if a header is being added, removed, it's content being edited or it's content being fully replaced
        - working parameters are: 'add', 'remove', 'edit' and 'replace'

    - content definies the content that will be added, fully replace or replace a single col/row in the header if the action is 'add', 'edit' or 'replace'
        - content should be a list when replacing or adding a header
        - content should be a str when editing a header

    - index definies what col or row of the header will be replaced when editing the header

- The get_header function returns a header's content and takes header as an arument to specify which header should be returned
    - possible arguments are 'row' or 'col'


## All Links related to this Project:

### This Project:

- My Profile: https://github.com/endo-do
- This Repository: https://github.com/endo-do/Terminal-Table-Python/blob/main/Table.py

### Sources:

- Box Drawing Characters: https://en.wikipedia.org/wiki/Box-drawing_character
