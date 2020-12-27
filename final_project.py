print("**************Simple Student Management System**************")

adi = "Duygu"
soyad= "Savaşcı"

j=1
i=1

midterm=0
final=0
project=0

courselist=[]
my_courselist=[]

adi1 =input("Lütfen adınızı giriniz: ")
soyad1= input("Lütfen soyadınızı giriniz: ")

def dersler(lessonsayisi) :

    if 3 <= lessonsayisi <= 5 :
        x=1
        while x <= lessonsayisi :
            my_course= input("Aldığınız derslerin adını  giriniz: ")
            my_courselist.append(my_course)
            x+=1
        
        return("Aldığınız derslerin listesi: ", my_courselist)
            
    else:
        return ("You failed in class")

while i <= 4 :

    if i == 4 :
        print("Please try again later")
        break
       
    if (adi != adi1 or soyad != soyad1):
        print("Hatalı girdiniz !")
        adi1 =input("Lütfen adınızı giriniz: ")
        soyad1= input("Lütfen soyadınızı giriniz: ")
        i += 1
        continue

    else:
        print("Welcome, Succesful log in.")     

        while j <= 5  :
            course_input = input("Lütfen derslerinizi giriniz: ")
            courselist.append(course_input)
            j+=1

        print("Seçebileceğiniz derslerin listesi: ", courselist)

        lessonsayisi= int(input("Lütfen almak istediğiniz ders sayısını giriniz: "))

        derslerReturn = dersler(lessonsayisi)

        if (derslerReturn == "You failed in class"):
            print(derslerReturn)
            break

        derssecimi = input("Sınavını Aldığınız Ders : ")

        for n in my_courselist :

            if derssecimi == n :

                course_dict = {midterm: 75, final: 74, project: 90}
                grade= course_dict[midterm]*0.3 + course_dict[final]*0.5 + course_dict[project]*0.2
        
                if grade >= 90:
                    print("Congrats, You get AA")
                elif 70 <= grade < 90:
                    print("Nice, You get BB")
                elif 50 <= grade < 70:
                    print("You get CC")
                elif 30 <= grade < 50:
                    print("You get DD")
                else:
                    print("You get FF, You failed")

        break






