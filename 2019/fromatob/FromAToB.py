a, b= map(int, input().split())

counter = 0
stop = False
while a != b:
    if(a < b):
        print(b-a + counter)
        stop = True
        break
    else:
        if(a % 2 == 0):
            a //= 2
        else:
            a += 1
    counter += 1
if stop == False:
    print(counter)
