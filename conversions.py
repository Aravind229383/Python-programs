
def bin2Dec(val):
    rev=val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
        i += 1

    return dec


def oct2Hex(val):
    rev=val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8**i
        i += 1
    list=[]
    while dec != 0:
        list.append(dec%16)
        dec = dec // 16

    nl=[]
    for elem in list[::-1]:
        if elem <= 9:
            nl.append(str(elem))
        else:
            nl.append(chr(ord('A') + (elem -10)))
    hex = "".join(nl)

    return hex


base = 2
num1 = input("Enter a binary number : ")
# print(bin2Dec(num1))
print(int(num1, base))



# A better implementation
def bin2Dec(val):
    return int(val, 2)


def oct2Hex(val):
    return int(val, 8)


try:
    num1 = input("Enter a binary number : ")
    print(bin2Dec(num1))
except ValueError:
    print("Invalid literal in input with base 2")

try:
    num2 = input("Enter a octal number : ")
    print(oct2Hex(num2))
except ValueError:
    print("Invalid literal in input with base 8")
