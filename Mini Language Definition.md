# Py++
Python-like subset of C++

## Equivalences
### Types

```cpp
int a;
float b;
long a2;
double b2;
bool cond;
std::string text;
std::vector arr;
```

```py++
num a
num b
big a2
big b2
bool cond
str text
vec arr
```

### Statements

```c++
if (a == 3 && b != 4) {
	// do smth
} else {
	// do smth else
}

for (i = 0; i < 10; i++) {
	// repeat smth
}

while (n > 0) {
	// repeat smth else
}
```

```py++
a = 3 & b != 4 ? 
	// do smht
:
	// do smth else

i = 0 -> 10, +1
	// repeat smth

n -> 0
	// repeat smth else
```

Ifs just abuse ternary operators lol

### I/O & Standard Library stuff

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin>>n;
	cout<<n<<endl;
	
	string text, space;
	cin>>space;
	getline(cin, text);
	
	return 0;
}
```

```py++
main
	num n
	in n
	out n, endl
	
	str text, space
	in space
	lin text
```

The `main` keyword defines the main function, along with the return code.
The first appearance of tokens from other libraries automatically includes said library and uses the standard namespace.

E.g.:

```py++
in n
out n
```

maps to

```cpp
#include <iostream>
// gets added at the top of the file
...
std::cin>>n;
std::cout<<n;
```

