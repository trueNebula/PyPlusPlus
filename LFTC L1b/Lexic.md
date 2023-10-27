## Alphabet

a. Uppercase and Lowercase letters of the English language (A-Z a-z)
b. Decimal digits (0-9)

## Lexic

a. Special symbols
	- Operators: + - \* / % < <= > >= != ? : -> 
	- Separators: space, newline, ","
	- Reserved Words: main, num, bool, str, vec, in, out, lin, min, max
b. Identifiers
	- a sequence of letters and digits such that the first character is always a letter.
	
```EBNF
identifier = letter | letter {letter|digit}
letter = "a" | ... | "z" | "A" | ... | "Z"
digit = "0" | ... | "9"
```

c. Constants
- Integer
```EBNF
const_int = ["-"] int
int = "0" | nonzero_digit [digit_seq]
nonzero_digit = "1" | ... | "9"
digit_seq = {digit}
```

- Boolean
```EBNF
bool = "true" | "false"
```

- Character
```EBNF
character = "'" base_character "''
base_character = letter | digit
```

- String
```EBNF
string = "'" base_string "''
base_string = character {character}
```