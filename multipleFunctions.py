class multiFunctions():
    def Subfields():
        SubfieldsAI=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for temp in SubfieldsAI:
            print(temp)
            
    def OddEven():
        number=int(input("Enter the number:"))
        if(number%2==0):
            print(number,"is Even number")
        else:
            print(number,"is Odd number")
            
    def Elegiblity():
        gender=input('your gender:')
        Age=int(input('your age:'))
        if(gender.lower()=='male'):
            if(Age>=21):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        elif(gender.lower()=='female'):
            if(Age>=18):
                print('ELIGIBLE')
            else:
                print('NOT ELIGIBLE')
        else:
            print("Don't know")
            
    def percentage():
        Subject1=int(input("Subject1= "))   
        Subject2=int(input("Subject2= "))    
        Subject3=int(input("Subject3= "))    
        Subject4=int(input("Subject4= "))    
        Subject5=int(input("Subject5= "))

        Total= Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",Total)
        Percentage=Total/5
        print("Percentage:",Percentage)

        
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        #print("Area formula: (Height*Breadth)/2")
        AreaOfTriangle=(height*breadth)/2
        print("Area Of Triangle:",AreaOfTriangle)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth1=int(input("Breadth1:"))
        #print("Perimeter formula: Height1+Height2+Breadth")
        PerimeterOfTriangle= height1+height2+breadth1
        print("Perimeter Of Triangle:",PerimeterOfTriangle)
    

            

        