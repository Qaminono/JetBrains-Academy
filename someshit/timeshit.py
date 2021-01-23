import pyperclip

string = "The main diagonal of a matrix is a line with elements from a1,1a_{1, 1}a1,1​ to an,na_{n,n}an,n​:"
list_str = string.split()
for index, element in enumerate(list_str):
    if len(element) == 3 and len(set(element)) == 1:
        list_str[index] = f"![](https://latex.codecogs.com/svg.latex?{element[1]})"
res = " ".join(list_str)
print(res)
pyperclip.copy(res)
