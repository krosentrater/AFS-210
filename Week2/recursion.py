
def loop1():
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num, odd_sum):
    if num > odd_sum:
        return 0
    else:
        return num + loop1Rec(num + 2, odd_sum)

number1 = 1
odd_sum = 20

def loop2Rec(num,even_sum):
    if num >= even_sum:
        return 0
    else:
        return num + loop2Rec(num + 2, even_sum)

startEvenNumber = 2
even_sum = 20

print(f"Sum of odds between 1 and 20 using 'for' loop = {loop1()}")
print(f"Sum of odds between 1 and 20 using recursion = {loop1Rec(number1,odd_sum)}")
print(f"Sum of evens between 1 and 20 using 'while' loop = {loop2()}")
print(f"Sum of evens between 1 and 20 using recursion = {loop2Rec(startEvenNumber,even_sum)}")