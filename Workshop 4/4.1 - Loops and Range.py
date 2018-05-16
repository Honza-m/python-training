
print("#### FOR LOOP ####")
#for loop - iterates through each element in the list/dict/tuple
x = ['a','b','c','d','e']
for each in x:
    print(each)

print()
x = {
    'first': 'a',
    'second': 'b'
    }

for each in x:
    print(each) # will print the key of the dictionary ('first')
    print(x[each]) # will print the corresponding value ('a')

print("\n#### WHILE LOOP ####")
#while loop - evaluates condition on each loop
x = 0
while True:
    x = x + 1
    print(x)
    if x == 10: break

print("\n#### RANGE ####")
#range - creates an iterable filled with numbers
print(range(2))
print(range(2,4))
for i in range(5):
    print(i)
