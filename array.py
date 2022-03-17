array = [9,3,0,2,6,0,6,0,7]
count = 0
for i in array:
   if(i==0):
      array.remove(i)
      count = count+1
for i in range(count):
   array.append(0)
print(array)
for i in range(0, len(array)):
    print(array[i], end=" ");
for i in range(0, len(array)):
    for j in range(i + 1, len(array)):
        if (array[i] > array[j]):
            temp = array[i];
            array[i] = array[j];
            array[j] = temp;
result=array[::-1]
print("asending order",(result))