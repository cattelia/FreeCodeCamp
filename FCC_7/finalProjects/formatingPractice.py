list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

left = ['32', '3801', '45', '123']
operator = ['+', '-', '+', '+']
right = ['698', '2', '43', '49']
answers = [730, 3799, 88, 172]

for line in list:
    print("{:>8} {:>8} {:>8}".format(*line))

# > means right align.
# 8 means how many spaces

#Stack Overflow
#https://stackoverflow.com/questions/8234445/format-output-string-right-alignment

print(f"{'':>3}".join(str(i)) for i in range(1, 11))
#>>> <generator object <genexpr> at 0x000001D126EB14E0>

print(f"{'':>3}".join(str(i) for i in range(1, 11)))
#>>> 1   2   3   4   5   6   7   8   9   10

print(f"{'':>2}".join(str(i) for i in list))
#>>> 32 + 698    3801 - 2    45 + 43    123 + 49
print(list.split())

'''
for i in left, operator, right:
    print(left[i].rjust(10))
    print(operator[i].ljust() + right[i].rjust(10))


for i in left:
    print("{:>}".format(i), end="    ")


l = "32"
o = "+"
r = "694"

if len(l) or len(o) or len(r) < 4:
    print(
        f"{l:>5}"
        "\n"
        f"{o:<} {r:>}", end="   "
        )
else:
    print("ok")
'''
