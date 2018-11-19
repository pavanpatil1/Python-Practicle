# myworld

class student(object):
     def __init__(self,prn,name,surname,branch,contact):
        self.prn = prn
        self.name = name
        self.surname = surname
        self.branch = branch
        self.contact = contact


     def display(self):
         print("\n")
         print(self.prn)
         print(self.name)
         print(self.surname)
         print(self.branch)
         print(self.contact)
         print("\n")

     @property
     def roll(self):
            return self.__roll
     @roll.setter
     def roll(self,roll):
            if roll >0 and roll !=0:
                self.__roll = roll    
     @property
     def name(self):
            return self.__name
     @name.setter
     def name(self,name):
            if name ==None:
                raise"invalid entered name"
            else:
                 self.__name = name    

       
p = 0  
         
while p == 0:
    print("\n \n")
    print("\n_______________________________________________________________________________ \n \n**** Welcome To the MIT Academy Of Engineering Student Management System ****  \n\n1.Insert \n2.Delete \n3.Search \n4.Update \n5.Display All Data Of Student \n6.Quit \n____________________________________________________________________________")
    ch = input("enter your choice:-")
    if ch == 1:
        list1 = []
        n = input("\nHow Many Student You Should Add :  ")
        choice2 = 1
        choice3 = 2
        choice4 = 3
        choice5 = 4
        choice6 = 5
        
   
        for i in range(n):
            choice2 = 1
            while choice2 == 1:
                 
                print('Number Of Student :   '+str(i+1))
                prn = raw_input("\tprn:--") 
                 
                if prn == "":
                    print("enter the something..")  
                else:
                    choice2 = 0
            choice3 = 2
            while choice3 == 2:
                name = raw_input('\tName : ')
                if name == "":
                    print("enter the something")
                else:
                    choice3 = 1

            choice4 = 3       
            while choice4 == 3:        
                 surname = raw_input('\tSurname : ')
                 if surname == "":
                    print("enter something")
                 else:
                     choice4 = 2 
            choice5 = 4
            while choice5 == 4:
                     branch = raw_input('\tBranch :-')
                     if branch == "":
                         print "Enter Something"
                     else:
                          choice5 = 3   
                     
            choice6 = 5
            while choice6 == 5:                
                     contact =raw_input('\tContact')
                     if contact == "":
                         print "Enter something"
                     else:
                         choice6 = 4    

                     list1.append(student(prn,name,surname,branch,contact))

    elif ch == 2:
           print("1.Delete By PRN:-- \n 2. Delete By Name:--") 
           choice =  input("Enter Your Choice:--")

           if choice == 1:
              deleteid = raw_input("Enter the PRN: ")

              for obj in list1:
                
                  if obj.prn == deleteid:
                     list1.remove(obj)

           else:
               deleteid = raw_input(" Enter the Name of Student: ")    
            
               for obj in list1:

                if obj.rollNo == deleteid:
                    list1.remove(obj)

    elif ch == 3:
         print("\n1. Search By Name \n2. Search by Branch ")   
         Searchchoice= input("Enter your Option:---")
         if Searchchoice == 1:
               names=raw_input("Enter the name of Student :---")     
               for obj in list1:
                
                if obj.name == names: 
                    print "PRN :-- " ,obj.prn
                    print "name :-- ",obj.name
                    print " surname:---",obj.surname
                    print " Branch :-- ",obj.branch
                    print " Contact :-- ",obj.contact

         elif Searchchoice == 2:
                branchs = raw_input("Enter the Branch of student") 
                for obj in list1:

                    if obj.branch == branchs:
                       print "PRN :-- " ,obj.prn
                       print "name :-- ",obj.name
                       print " surname:---",obj.surname
                       print " Branch :-- ",obj.branch
                       print " Contact :-- ",obj.contact

                     
    elif ch == 4:
        
        ustudent = raw_input(" Enter the PRN of student to update : ")
        
        for i in list1:
                 if i.prn == ustudent:

                    print("1.prn \n2.name \n3.branch  ")
                    uchoice = input("Enter your choice : ")

                    if uchoice == 1:
                         uprn = raw_input("enter new PRN  : ")
                         i.prn = uprn
                     
                    elif uchoice == 2:
                         uname = raw_input("enter new name  : ")
                         i.name = uname 

                    elif uchoice == 3:
                         ubranch = raw_input("enter new branch  : ")
                         i.branch = ubranch      

                
            



    elif ch == 5:
        print("\n")
        print("MIT Aoe Student DataBase ")
        for i in list1:
             print("______________________")
             print("\n Prn :-- " +i.prn)
             print("Name " +i.name)
             print(" Surname " +i.surname ) 
             print(" Branch  " +i.branch )
             print("contact " +i.contact)
             print("______________________")



    else:
         p =  1
    
