class function():
    def ai():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Laguage Processing")
        return
    def oddeven():
        num=(int(input("Enter the Number")))
        if(num%2==1):
            print(num,"is Odd number")
        else:
            print(num,"is Even number")
        return
    def eligible():    
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))
        if(gender in("Male")):
            if(age>21):
                print("Eligible")
            else:
                print("Not Elgible")
        elif(gender in ("Female")):
            if (age>18):
                print("Elgible")
            else:
                print("Not Eligible")
            return
    def marks():
        num1=int(input("Subject1: "))
        num2=int(input("Subject2: "))
        num3=int(input("Subject3: "))
        num4=int(input("Subject4: "))
        num5=int(input("Subject5: "))
        total=(num1+num2+num3+num4+num5)
        print("Total :",total)
        per=(total/5)
        print("Percentage :",per)
        return
    def triangle():
        hight=int(input("Hight :"))
        breath=int(input("Breath :"))
        formula1=((hight*breath)/2)
        print("Area formula: (Height*Breath)/2")
        print("Area of Triangle:",formula1)
        angle="Area of Triangle:"
        hight1=int(input("Hight1 :"))
        hight2=int(input("Hight2 :"))
        breath=int(input("Breath :"))
        formula=(hight1+hight2+breath)
        print("Area formula: (hight1+hight2+breath)")
        print("Perimeter of Trianle:",formula)
        angle="Perimeter of Trianle:"
        return 