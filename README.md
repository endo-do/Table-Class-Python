# Terminal Table Python
A simple Python Class for displaying information as a customizable table in the console

The following is also documented in the code itself

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

- 'empty_cells', 'empty_lists' and 'empty_dicts' (list): Definies what cells/lists/dicts will be treated as empty
    - Default set to '["", "#empty"], [[], [""], ["#empty"]] and [{}, {""}, {"#empty"}]

- 'replace_empty' (str) definies with what empty cells/lists/dicts will be replaced
    - Default set to ""

- 'header' ([{header_type:header_content}, ..]) definies the active headers
    - header_types are 'row' and 'col'
    - header_content can be given as list or dict
    - e.g. {"row":["Name", "Age", "Gender"]}
    - Default set to {}

## Functions:

### Note: Working with indexes:

- Indexes for functions work the exact same ways as in standart python lists
    - Index 0 returns the first element and -1 returns the last

- An index will be adjusted to the active headers accordingly
    - This means that the header dont count as a row or column
    - E.g. the first row is still accesible with index 0 while a row header is active

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
    - if 'row', 'col' or 'replace' were not defnied the row/col/cell will be replaced with standart 'replace_empty'
- E.g. replace_cell(-1, 0, "hello") would replace the first element in the last row with "hello"

### Get Content:

- The functions 'get_col', 'get_column' and 'get_content' are used to get content from the Table

- 'get_col' and 'get_column' each 'index' as an argument

- 'get_content' returns the whole table without the headers and doesnt need an argument

- E.g. get_col(4) would return the fifth column

### Handle Headers:

With the conf_header function you can add, remove, edit or replace the headers of the table

It takes header, action, content and index as parameters:

- header secifies which header will be configured ('col' or 'row')

- action definies if a header is being added, removed, it's content being edited or it's content being fully replaced
    - working parameters are: 'add', 'remove', 'edit' and 'replace'

- content definies the content that will be added as or as part of the header's content if the action is 'add', 'edit' or 'replace'
    - content should be a list when replacing or adding a header
    - content should be a str when editing a header

- index definies what col or row of the header will be replaced when editing the header

The get_header function returns a header's content and takes header as an arument to specify which header should be returned
    - possible arguments are 'row' or 'col'

### Display:

The display function simply displays the table at its current state

## Data Structures:

The table class supports different data structures when adding or editing content to the table or configuring the headers

Supported structures are:
- list_in_list
- list_in_dict
- dict_in_list
- dict_in_dict

## Sources:

- Box Drawing Characters: https://en.wikipedia.org/wiki/Box-drawing_character
