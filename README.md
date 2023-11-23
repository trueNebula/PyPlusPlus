# PyPlusPLus
It's like Python and C++ had an ugly baby.
All the funky functionality with none of the elegance.

## Symbol Table
The Symbol Table is implemented using a custom Hash Table. Collisions are solved using separate chaining.
Internally, it’s represented as an array of linked list nodes, where the key of a node is its position in the array and its value is the given symbol.

### Class attributes
- capacity -> the maximum capacity of the symbol table (default = 100)
- size -> the current size of the symbol table
- buckets -> the internal array of linked list nodes

### Operations
- add(value) -> adds a new node that has a given value
- find(value) -> finds the index of the node that has a given value
- remove(value) -> removes the node that has a given value
- size() -> returns the number of elements in the symbol table
- export() -> exports the contents of the symbol table to a file st.out

## Program Information File
The Program Information File (abbreviated as PIF from now on) is implemented using a simple array.

### Class attributes
- array -> the internal array of PIF entries

### Operations
- add(code, position) -> adds a new entry to the PIF
- export() -> exports the contents of the PIF to a file pif.out

## Scanner
The Scanner is implemented.

### Regex
The following regexes are used to match the tokens:
- identifier: `^[a-zA-Z][a-zA-Z0-9]*$`
- constant: `^\"[A-Za-z0-9\.\?\!, ]*\"$` (strings) and `^-?[1-9][0-9]*$` (integers)
