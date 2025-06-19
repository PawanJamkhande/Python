##TOWER OF HONOI##
import time
class Honoi:
    def __init__(self):
        print("WELCOME TO TOWER OF HONOI GAME")
        print()
        print("Given Problem    A=[3,2,1]     B=[]     C=[]")
        print()
        print("Expected Output  A=[]    B=[]    C[3,2,1]")
        self.A = []
        self.B = []
        self.C = []
    def tower(self,item):
            self.A.append(item)
            time.sleep(1)
            print("A= ",self.A)
            print("Items in Tower A\n")

    def pass1(self):
            self.temp=self.A.pop(2) #A=[3,2]
            self.C.append(self.temp) #c=[1] => temp=1
            time.sleep(1)
            print("A= ",self.A   ,"    ",   "B= ",self.B    ,"     ",    "C= ",self.C)
            print("Pass One Completed====================\n")

    def pass2(self):
            self.temp=self.A.pop(1) #A=[3]
            self.B.append(self.temp) #b=[2] => temp=2
            time.sleep(1)
            print("A= ",self.A   ,"    ",   "B= ",self.B    ,"     ",    "C= ",self.C)
            print("Pass One Completed====================\n")

    def pass3(self):
            self.temp=self.C.pop(0) #C=[1]
            self.B.append(self.temp) #b=[1] => temp=1
            time.sleep(1)
            print("A= ",self.A   ,"    ",   "B= ",self.B    ,"     ",    "C= ",self.C)
            print("Pass One Completed====================\n")

    def pass4(self):
            self.temp=self.A.pop(0) #A=[3,2]
            self.C.append(self.temp) #c=[1] => temp=1
            time.sleep(1)
            print("A= ",self.A   ,"    ",   "B= ",self.B    ,"     ",    "C= ",self.C)
            print("Pass One Completed====================\n")
        
    def pass5(self):
            self.temp=self.B.pop(1) #A=[3,2]
            self.A.append(self.temp) #c=[1] => temp=1
            time.sleep(1)
            print("A= ",self.A   ,"    ",   "B= ",self.B    ,"     ",    "C= ",self.C)
            print("Pass One Completed====================\n")

    def pass6(self):
            self.temp=self.B.pop(0) #A=[3,2]
            self.C.append(self.temp) #c=[1] => temp=1
            time.sleep(1)
            print("A= ",self.A   ,"    ",   "B= ",self.B    ,"     ",    "C= ",self.C)
            print("Pass One Completed====================\n")
        
    def pass7(self):
            self.temp=self.A.pop(0) #A=[3,2]
            self.C.append(self.temp) #c=[1] => temp=1
            time.sleep(1)
            print("A= ",self.A   ,"    ",   "B= ",self.B    ,"     ",    "C= ",self.C)
            print("Pass One Completed====================\n")

obj = Honoi()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

