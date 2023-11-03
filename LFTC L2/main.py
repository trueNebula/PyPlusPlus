from symbol_table import SymbolTable

st = SymbolTable()
st.insert(1, "a")
st.insert(2, "b")
st.insert(1, "c")

print(str(st))

print(st.find(1))