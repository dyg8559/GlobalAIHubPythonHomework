i= 1
while i < 6:
    value=input("Please enter a value: ")
    if value.isalpha() :
        print(i, "th value:", value, "--- ", "type is", type(value))
        i+=1
    if value.isdigit():
        value=int(value)
        print(i, "th value:", value, "--- ", "type is", type(value))
        i+=1
    
#or

i= 1
mylist=[]
while i < 6:
    value=input("Please enter a value: ")
    mylist.append(value)
    i+=1
print("Kullanıcıdan alınan degerler: ", mylist)

j=0

while (j < len(mylist)):
    print(j, "th item: ", mylist[j], " type is", type(mylist[j]))
    j+=1
  


  