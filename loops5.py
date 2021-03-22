# 4.7 Nested Loops - A loop inside another loop

### (Digital Clock Loop)
##for hours in range(24):
##    for minutes in range(60):
##        for seconds in range(60):
##            print(hours, ':', minutes, ':', seconds)


## (printing stair steps)

num_steps = 6
for r in range(num_steps):
    for c in range(r):
        print(' ', end='')
    print('#')

for r in range(2, 3):
    for c in range(r):
        print('#', end='')
    print()

for r in range(1, 4):
    for c in range(r):
        print('#', end='')
    print()
