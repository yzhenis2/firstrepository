x = 1
if x < 1:
    print("x is less than 1")
elif x == 1:
    print("x is 1") 
else:
    print("Fail")
for t in [3, 2, 1]:
    print("t minus " + str(t))
print("blast off")

x_values = [1, 2, 3, 4, 5]

for i in x_values:
    x_2 = i**2
    print(x_2)

entries = ['top', 'CHArm', 'Top', 'sTraNGe', 'strangE', 'top']
quarks = {quark.lower() for quark in entries}
print(quarks)
