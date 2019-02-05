import queue
class Node:
    def __init__(self, data = {}):
       self.data = data
       self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
  
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
 
    def display(self):
        printval = self.head
        while printval is not None:
            print("--------------------------------------------------")
            print("DAY ==>                       ",printval.data.get("DAY"))
            print("Customer name is ==>          ",printval.data.get("NAME"))
            print("Customer address is ==>       ",printval.data.get("ADDRESS"))
            print("Customer age is ==>           ",printval.data.get("AGE"))
            print("Customer mobile no is ==>     ",printval.data.get("MOBILE_NO"))
            print("Customer email is ==>         ",printval.data.get("EMAIL"))
            printval = printval.next
        return


    

    def search(self):
        cust=input("The day on which customer you want to see ==>      ")
        printval = self.head
        while printval is not None:
            if(printval.data.get("DAY")==cust):
                print("Found")
                print("--------------------------------------------------")
                print("Customer name is ==>          ",printval.data.get("NAME"))
                print("Customer address is ==>       ",printval.data.get("ADDRESS"))
                print("Customer age is ==>           ",printval.data.get("AGE"))
                print("Customer mobile no is ==>     ",printval.data.get("MOBILE_NO"))
                print("Customer email is ==>         ",printval.data.get("EMAIL"))
                return
            printval = printval.next




a_stack = Queue()
choice = 0

while True:
    print("\n_________________________________________MENU FOR CUSTOMER MANAGEMENT IN RESTAURANT __________________________________________ \n\n\t\t\t\t\t1.Add Customer \n\t\t\t\t\t2.Delete Customer \n\t\t\t\t\t3.Show all Customers \n\t\t\t\t\t4.Search Customer \n\t\t\t\t\t5.Exit\n")

    choice = input("\nEnter your choice==>  ")

    if (choice == "1"):
        print("------------------------------------------------------------------")
        day = input("\nEnter the Day ==>      ")
        name = input("\nEnter the Name of the Customers ==>      ")
        address = input("\nEnter the Address of the Customers ==>   ")
        age = input("\nEnter the Age of the Customers ==>          ") 
        mobile_no = input("\nEnter the Mobile No of the Customers ==>   ")
        email = input("\nEnter the Email of the Customers ==>       ")
        print("------------------------------------------------------------------")
        data = {"DAY":day,"NAME":name,"ADDRESS":address,"AGE":age,"MOBILE_NO":mobile_no,"EMAIL":email}
       
        a_stack.enqueue(data)
      
    elif(choice == "2"):
        dequeued = a_stack.dequeue()
        if dequeued is None:
            print('Queue is empty.')
        else:
            print('Dequeued element: ',dequeued)

    elif(choice == "3"):
         a_stack.display()
         
    elif(choice == "4"):
       a_stack.search()
    
    elif(choice == "5"):
        break






  