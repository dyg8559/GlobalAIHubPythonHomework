# User Identification Program
inform= ['Adı', 'Soyadı', 'Yaşı', 'Dogum Tarihi']

firstname =input("Lütfen adınızı giriniz: ")
lastname= input("Lütfen soyadınızı giriniz: ")
age= int(input("Lütfen yaşınızı giriniz: "))
birthdate= int(input("Lütfen doğum tarihinizi giriniz: "))

mylist=[firstname, lastname, age, birthdate]

j=0
for  i in mylist :
    print("Kullanıcının {} : {}".format(inform[j], i))
    j+=1

if age < 18 :
    print("You can't go out because it's dangerous")
else:
    print("You can go out to the street")
