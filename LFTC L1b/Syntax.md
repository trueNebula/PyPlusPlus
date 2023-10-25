Predefined tokens are specified between double quotes.
Newlines act like ";" in C++
Indentations (tabs) are used in place of blocks

## Syntactical Rules

```EBNF
identifier = word {number}
word = letter {letter}
letter = "a" | ... | "z" | "A" | ... | "Z"
number = digit {digit}
digit = "0" | ... | "9"

constant = const_int | bool | character | string

tab = "  "
type = ("num" | "bool" | "str" | "vec")
operator = "+" | "-" | "*" | "/" | "%"
cond_operator = "<" | "<=" | "=" | ">=" | ">" | "!="
relation_operator = "&" | "|"

const_int = ["-"] int
int = "0" | nonzero_digit [digit_seq]
nonzero_digit = "1" | ... | "9"
digit_seq = {digit}

bool = "true" | "false"

character = 'base_character'
base_character = letter | digit

string = 'base_string'
base_string = character {character}


program = "main" "\n" statements

statements = tab statement {tab statement}
statment = (simple_statement | struct_statement) "\n"

simple_statement =  declaration_statement | assignment_statement | io_statement

declaration_statement = type identifier ["=" expression]
assignment_statement = identifier "=" expression
expression = term {("+" | "-" term)}
io_statement = ("in"|"out") identifier

term = term ("*" | "/" | "%") factor | factor
factor = "(" expression ")" | identifier | constant
operation = term {operator term}

struct_statement = cond_statement | loop_statement

cond_statement = cond_start {tab statement} [: \n {tab statememt}]
cond_start = condition "?" "\n"
condition = identifier cond_operator identifier {relation_operator condition}

loop_statement = for_statement | while_statement
for_statement = for_start {tab statement}
for_start = identifier "," step "->" constant "\n"
while_statement = while_start {tab statement}
while_start = identifier "->" constant {relation_operator identifier "->" constant} "\n"  
```