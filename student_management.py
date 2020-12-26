print("**************Simple Student Management System**************")

adi = "Duygu"
soyad= "Savaşcı"

courselist=['Matematik', 'Turkce', 'Fen', 'Sosyal', 'Bilgisayar']

i=1
midterm=0
final=0
project=0

adi1 =input("Lütfen adınızı giriniz: ")
soyad1= input("Lütfen soyadınızı giriniz: ")

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
        print(f'{courselist[0]},{courselist[1]},{courselist[2]},{courselist[3]} and {courselist[4]} derslerini alabilirsiniz:')
        lessonsayisi= int(input("Kaç tane ders seçtiniz: "))

        if  3 <= lessonsayisi <= 5 : 
            derssecimi = input("Aldığınız derslerden sadece birini giriniz: ")

            if derssecimi == "Matematik" :
                matematik_dict = {midterm: 87, final: 94, project: 90}
                grade= matematik_dict[midterm]*0.3 + matematik_dict[final]*0.5 + matematik_dict[project]*0.2
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

            if  derssecimi == "Turkce" :
                turkce_dict = {midterm: 59, final: 72, project: 80}
                grade= turkce_dict[midterm]*0.3 + turkce_dict[final]*0.5 + turkce_dict[project]*0.2
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

            if  derssecimi == "Fen" :
                fen_dict = {midterm: 32, final: 25, project: 10}
                grade= fen_dict[midterm]*0.3 + fen_dict[final]*0.5 + fen_dict[project]*0.2
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

            if  derssecimi == "Sosyal" :
                sosyal_dict = {midterm: 62, final: 62, project: 65}
                grade= sosyal_dict[midterm]*0.3 + sosyal_dict[final]*0.5 + sosyal_dict[project]*0.2
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

            if  derssecimi == "Bilgisayar" :
                bilg_dict = {midterm: 74, final: 52, project: 85}
                grade= bilg_dict[midterm]*0.3 + bilg_dict[final]*0.5 + bilg_dict[project]*0.2
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
       
        else:
            print("You failed in class")
            continue


