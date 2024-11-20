str = input()
list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count=0
for i in list:
    while i in str:
        str = str.replace(i,' ',1)
        count+=1
    
count += len(str.replace(' ', ''))
print(count)