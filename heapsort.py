f = open("input.txt",'r')
data = list(map(int,f.read().split()))
print(data)
f.close()

def heap_sort(array):
    n = len(array)
    for i in range(n):
        c = i
        while c != 0:
            r = (c-1)//2
            if (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            c = r

    for j in range(n-1, -1, -1):
        array[0] , array[j] = array[j], array[0]
        r = 0
        c = 1
        while c<j:
            c = 2*r +1
            if (c<j-1) and (array[c] < array[c+1]):
                c += 1
            if (c<j) and (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            r=c

heap_sort(data)
print(data)
str_data=[str(i) for i in data]

with open("output.txt","w") as file:
  file.writelines("\n".join(str_data))
