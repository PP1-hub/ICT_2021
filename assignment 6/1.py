string = str(input())
i=5
print("Input: description:",string ,"Please enter i-th element in string to remove it.",i)

new_s = ""
for k in range(len(string)):
    if k!=i:
        new_s=new_s+string[k]
print("Output: description:",new_s) 