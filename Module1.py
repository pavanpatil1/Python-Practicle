class Customer:
    list1 = []
    def __init__(self,day,name,address,age,mobile_no,email):
        self.day = day
        self.name = name 
        self.address = address
        self.age = age
        self.mobile_no = mobile_no
        self.email = email


    
    def add(self):
        addchoice = input("\n Enter no of Customer you want to add =>  ")
         
        for i in range(addchoice):
            print("------------------------------------------------------------------")
            day = raw_input("\nEnter the Day ==>      ")
            name = raw_input("\nEnter the Name of the Customers ==>      ")
            address = raw_input("\nEnter the Address of the Customers ==>   ")
            age =raw_input("\nEnter the Age of the Customers ==>          ") 
            mobile_no =raw_input("\nEnter the Mobile No of the Customers ==>   ")
            email = raw_input("\nEnter the Email of the Customers ==>       ")
            print("------------------------------------------------------------------")

            Customer.list1.append(Customer(day,name,address,age,mobile_no,email))

    
    def display(self):
        daychoice = raw_input("\nEnter the day which result you want to see ==>  ")
        for i in Customer.list1:
            if(i.day == daychoice):
                print("\n----------------------------\n")
                print("Name =>             " +i.name)
                print("Address=>           " +i.address)
                print("age =>              " +i.age ) 
                print("mobile number =>    " +i.mobile_no)
                print("E-mail =>           " +i.email)
                print("\n----------------------------\n")



    def delete(self):
        removename = raw_input("\nEnter the name of the customer you want to remove  => ")
        for i in Customer.list1:
            if i.name == removename:
                Customer.list1.remove(i)

    def search(self):
        s = raw_input("Enter the day you want to search ==>     ")
        l = len(Customer.list1)
        ub = l-1
        lb = 0

        while lb<=ub :
            mid=(lb+ub)//2      

            if Customer.list1[mid].day == s:
                print("Found")

                print("\n------------------------------------------------------n")
                print("Name =>             " +Customer.list1[mid].name)
                print("Address=>           " +Customer.list1[mid].address)
                print("age =>              " +Customer.list1[mid].age ) 
                print("mobile number =>    " +Customer.list1[mid].mobile_no)
                print("E-mail =>           " +Customer.list1[mid].email)
                print("\n-----------------------------------------------------\n")
                break

            elif Customer.list1[mid] > s:
                lb=mid+1
            elif Customer.list1[mid] > s:
                ub=mid-1
            else:
                print("User not found")
                return

                 

           

choice = 0

object1 = Customer(" "," "," "," "," "," ")

while(choice != 5):
    print ("\n_________________________________________MENU FOR CUSTOMER MANAGEMENT IN RESTAURANT __________________________________________ \n\n\t\t\t\t\t1.Add Customer \n\t\t\t\t\t2.Delete Customer \n\t\t\t\t\t3.Show all Customers \n\t\t\t\t\t4.Search Customer \n\t\t\t\t\t5.Exit\n" )
    
    choice = input("\nEnter Your Choice ==>   ")
    if(choice == 1):
        object1.add()

    elif(choice == 2):
        object1.delete()

    elif(choice == 3):
        for i in Customer.list1:
            object1.display()

    elif(choice == 4):
        object1.search()