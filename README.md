# Terminal Table Python
A simple Python Class for displaying information as a customizable table in the console

## All Links related to this Project:

### This Project:

- My Profile: https://github.com/endo-do
- This Repository: https://github.com/endo-do/Terminal-Table-Python/blob/main/Table.py


### Sources:

- Box Drawing Characters: https://en.wikipedia.org/wiki/Box-drawing_character


## How to use the Terminal Class

### How to specifiy Indexes correctly:

- When adding, removing or editing the content of the table, the headers dont count as a row/col so the first row will still have the index 0
- The specified index also works the same as in standart python list
    - This means you can access the first element with 0, the second with 1 and so on
    - You can also access the last element with -1, second last with -2, and so on

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

### Functions

#### test: 

-dawd
