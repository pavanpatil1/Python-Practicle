class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None
 
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
 
    def pop(self):
        if self.head is None:
            return None
        else:
            popped = self.head.data
            self.head = self.head.next
            return popped

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


a_stack = Stack()
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
       
        a_stack.push(data)
      
    elif(choice == "2"):
        pop = a_stack.pop()
        if pop is None:
            print('Queue is empty.')
        else:
            print('pop element: ',pop)

    elif(choice == "3"):
         a_stack.display()
         
    elif(choice == "4"):
       a_stack.search()
    
    elif(choice == "5"):
        break
