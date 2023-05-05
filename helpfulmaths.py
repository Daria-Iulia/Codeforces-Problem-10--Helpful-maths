s = input()
num = s.split("+")

sorted_num = sorted(map(int, num))
sorted_num_str = list(map(str, sorted_num))


output="+".join(sorted_num_str)

print(output)