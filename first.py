
class student(object):
     """
     This is the simple programme for Store Student College Information
     """
    
     Branch = 'IT'                           #Static Variable of Branch you can access it through Choice 7
     clg = 'MIT Alandi'                      #static variable of college  you can access it through Choice 8
     stream = 'Engineering'                  #static variable of stream  you can access it through Choice 9
     no_of_stud = 0                          #variable to count number of student
     def __init__(self,prn,rol,name,surname,contact,email):
        self.__prn = prn
        self.__rol = rol
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__contact = contact
        student.no_of_stud += 1

     def display(self):
         print("\n")
         print(self.prn)
         print(self.rol)
         print(self.name)
         print(self.surname)
         print(self.email)
         print(self.contact)
         print("\n")

     @property
     def prn(self):
            return self.__prn
     @prn.setter
     def prn(self,prn):
                self.__prn = prn 

     @property
     def rol(self):
            return self.__rol
     @rol.setter
     def rol(self,rol):
                self.__rol = rol               

     @property
     def name(self):
            return self.__name
     @name.setter
     def name(self,name):
                 self.__name = name 

     @property
     def surname(self):
            return self.__surname
     @surname.setter
     def surname(self,surname):
                 self.__surname = surname
     @property
     def email(self):
            return self.__email
     @email.setter
     def email(self,email):
                 self.__email = email

     @property
     def contact(self):
            return self.__contact
     @contact.setter
     def contact(self,contact):
                 self.__contact = contact                          


     list1=[]
     @staticmethod
     def add():
         n = input("\nHey User How Many student You Should Add :  ")
         input1 = 1
         input2 = 2
         input3 = 3
         input4 = 4
         input5 = 5
         for i in range(n):
            input1 = 1
            while input1 == 1:      
                print('Number Of Student :   '+str(i+1))
                prn = raw_input("PRN:--")      
                if prn == "":
                    print("\n")
                    print("enter something..")
                    print("\n")  
                elif prn.isalpha():
                    print("\n")
                    print("Enter Number only")  
                    print("\n") 
                else:
                    input1 = 0


            input2 = 2
            while input2 == 2:      
                rol = raw_input("Roll no:--")      
                if rol == "":
                    print("\n")
                    print("enter something..")
                    print("\n")  
                elif rol.isalpha():
                    print("\n")
                    print("Enter Number only")  
                    print("\n") 
                else:
                    input2 = 0        

            input3 = 3
            while input3 == 3:
                name = raw_input('NAME : ')
                if name == "":
                    print("\n")
                    print("enter something")
                    print("\n")
                elif name.isdigit():
                    print("\n")
                    print("Enter the Name only.")
                    print("\n")     
                else:
                    input3 = 1

            input4 = 3       
            while input4 == 3:        
                 surname = raw_input('SURNAME : ')
                 if surname == "":
                    print("\n")
                    print("enter something")
                    print("\n")
                 elif surname.isdigit():
                     print("\n")
                     print("Enter name only") 
                     print("\n")  
                 else:
                     input4 = 2 

            input4 = 3       
            while input4 == 3:        
                 email = raw_input('Gmail : ')
                 if email == "":
                    print("\n")
                    print("enter something")
                    print("\n")
                 else:
                     input4 = 2          


                     
            input6 = 5
            while input6 == 5:                
                     contact =raw_input('Contact:-')
                     if contact == "":
                         print("\n")
                         print "Enter something"
                         print("\n")
                     elif len(contact) != 10:
                         print("\n")
                         print("enter valid number")
                         print("\n")
                     elif contact.isalpha():
                         print("\n")
                         print("enter the Valid Input")  
                         print("\n")  
                     else:
                         input6 = 4    

                     student.list1.append(student(prn,rol,name,surname,email,contact))

    
                 

     @staticmethod
     def show():
        print("\n")
        print("MIT AOE Student DataBase ")
        for i in student.list1:
             print("______________________")
             print("Prn :-- " +i.prn)
             print "Roll Number :--",i.rol
             print("Name:-- " +i.name)
             print("Surname:-- " +i.surname ) 
             print ("Branch:--" +i.Branch)
             print("contact:-- " +i.contact)
             print("College :-- " +i.clg)
             print("Stream :-- " +i.stream)
             print("\n")
             print("total number of student is:--")
             print (student.no_of_stud)
             print("______________________") 

     @staticmethod
     def search():
         choices= 0
         print("\n")
         print("1.Search By Name")
         print("2.Search by prn")
         print("3.Search by Surname")
         print("4.Search By Contact")
         print("\n")   
         Searchchoice= input("Enter your Option:---")
         if Searchchoice == 1:
               names=raw_input("Enter the name of Student :---")
               for i in student.list1 :              
                     if i.name == names :
                          print("______________________")
                          print("\n Prn :-- " +i.prn)
                          print("Name:-- " +i.name)
                          print(" Surname:-- " +i.surname ) 
                          print ("Branch:--" +i.stream)
                          print("contact:-- " +i.contact)
                          print("total number of student is:--")
                          print (student.no_of_stud)
                          print("______________________") 

         if Searchchoice == 3:
             surnames = raw_input("Enter your surname:--")    
             for i in student.list1:
                if i.surname == surnames:
                          print("______________________")
                          print("\n Prn :-- " +i.prn)
                          print("Name:-- " +i.name)
                          print(" Surname:-- " +i.surname ) 
                          print ("Branch:--" +i.stream)
                          print("contact:-- " +i.contact)
                          print("total number of student is:--")
                          print (student.no_of_stud)
                          print("______________________") 
         if Searchchoice == 2:
             prns = raw_input("Enter your Prn:--")    
             for i in student.list1:
                if i.prn == prns:
                          print("______________________")
                          print("\n Prn :-- " +i.prn)
                          print("Name:-- " +i.name)
                          print(" Surname:-- " +i.surname ) 
                          print ("Branch:--" +i.stream)
                          print("contact:-- " +i.contact)
                          print("total number of student is:--")
                          print (student.no_of_stud)
                          print("______________________")     

         if Searchchoice == 4:
             contacts = raw_input("Enter your Contact:--")    
             for i in student.list1:
                if i.contact == contacts:
                          print("______________________")
                          print("\n Prn :-- " +i.prn)
                          print("Name:-- " +i.name)
                          print(" Surname:-- " +i.surname ) 
                          print ("Branch:--" +i.stream)
                          print("contact:-- " +i.contact)
                          print("total number of student is:--")
                          print (student.no_of_stud)
                          print("______________________")                           
                        
     @staticmethod
     def update():
          upchoice = 0
          updatestudent = raw_input(" Enter the PRN of student to update :- ")    
          for i in student.list1:
                 if i.prn == updatestudent:
                    print("1.PRN")
                    print("2.Name")
                    print("3.Surname")
                    print("4.Contact")
                    uchoice = input("\nEnter your choice:-  ")
                    if uchoice == 1:
                         uprn = raw_input("Enter New prn:-  ")
                         i.prn = uprn
                    elif uchoice == 2:
                         nameu = raw_input("Enter New name:-  ")
                         i.name = nameu
                    elif uchoice == 3:
                         surnameu = raw_input("Enter New Surname:-  ")
                         i.surname = surnameu
                    elif uchoice == 4 :
                         contactu = raw_input("Enter New contact:-  ")
                         i.contact = contactu    

     @staticmethod
     def exit():
         print ("Thanks for visiting MIT AOE Database System Visit Again")                                   

     @staticmethod
     def depart():
            print "Branch Of Student is",student.Branch

     @staticmethod
     def clag():
         print "College of student is:---",student.clg 

     @staticmethod
     def stram():
         print "Stream Of Student :--",student.stream       
                            
n = student  
p = 0
print (student.__doc__)             
while p == 0:   
    print("\n")
    print("\n_______________________________________________________________________________________________________________ \n \n* WELCOME TO  MIT ACADEMY OF ENGINNERING INFORMATION TECHNOLOGY STUDENT MANAGEMENT DATABASE SYSTEM  *  \n\n1.INSERT \n2.DELETE \n3.SEARCH \n4.UPDATE \n5.DISPLAY ALL STUDENT DATA \n6.QUIT \n_________________________________________________________________________________________________________________")
    
    chq = 1
    while chq == 1:      
        choice = raw_input("Enter your choice:--")      
        if choice== "":
             print("\n")
             print("enter something..")
             print("\n")
        elif choice.isalpha():
            print("\n")
            print("Enter only Number") 
            print("\n") 
        elif int(choice) < 0 :
            print("Enter Positive Number")        
        else:   
            ch = int(choice)  
            chq = 0    

    if ch == 1:
        n.add()  
    elif ch == 2:
       print("\n")  
       print("1.Delete By PRN:-- ")
       print ("2.Delete By Roll Number:--")
       print("3. Delete By Name:--")
       print("4.Delete By Surname")
       print("5.Delete By COntact")
       choice =  input("Enter Your Choice:--")
       if choice == 1:
              dele = raw_input("Enter the PRN: ")
              for obj in student.list1:    
                  if obj.prn == dele:
                     student.list1.remove(obj)
       elif choice == 2:
              dele = raw_input("Enter the Roll Number: ")
              for obj in student.list1:    
                  if obj.prn == dele:
                     student.list1.remove(obj)

       elif choice == 3:
               dele = raw_input(" Enter the Name of Student: ")            
               for obj in student.list1:
                if obj.name == dele:
                    student.list1.remove(obj)
       elif choice == 4:
               dele = raw_input(" Enter the Surname of Student: ")            
               for obj in student.list1:
                if obj.surname == dele:
                    student.list1.remove(obj)   
       elif choice == 5:
               dele = raw_input(" Enter the Contact number of Student: ")            
               for obj in student.list1:
                if obj.contact == dele:
                    student.list1.remove(obj)                       

    elif ch == 3:
        n.search()    
    elif ch == 4:
        n.update()            
    elif ch == 5:
        n.show()   
    elif ch == 7: #to find The Branch of Student
        n.depart()
    elif ch == 8: #to Find the College of Student
        n.clag()
    elif ch == 9:  #to Find the Stream of Student
        n.stram()              
    else:
         p = 1

    if ch == 6:
       n.exit()       

