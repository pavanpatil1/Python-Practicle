#Write a Programme to Construct the DFA which Have an 5 Possiblites 1.Equal no of a's followed by equal no of b's \n2.First and last symbols are same \n3.No of a's are divisible by 2 \n4.Binary no divisible by 5 \n5.No of a's divisible by 4 & No of b's are not divisible by 3 


while True:
    print("_______________________________________________________________________________________________________")
    print("\n1.Equal no of a's followed by equal no of b's \n2.First and last symbols are same \n3.No of a's are divisible by 2 \n4.Binary no divisible by 5 \n5.No of a's divisible by 4 & No of b's are not divisible by 3 ")
    print("________________________________________________________________________________________________________")

    choice = int(input("\nEnter your choice = "))
    if(choice == 4):
        binaryno = int(input("Enter Binary no = "))
        decvalue = 0
        base = 1
    else:
        string = input("Enter your String =")
        strlen = len(string)
    i = counter = counter2 = 0


# Number of A's are Equal no of B's 

    if(choice == 1): 
        st=string
        counta=sum(map(lambda x : 1 if 'a' in x else 0, st))
        countb=sum(map(lambda x : 1 if 'b' in x else 0, st))
        if (counta == countb) and (counta > 0 ) and (len(st)==counta*2): 
            for i in st[0:(counta):1]: 
                if (i !='a'): 
                    print("Sorry, String is not Accepted")
                    exit()
            print("Your String is Accepted")
        else: print("Sorry, String is not Accepted")
        
# first and the Last symbol are Same
    if(choice == 2):

        if(string[0] == string[strlen-1]):
            print("Your String is Accepted")
        else:
            print("Sorry, String is not Accepted")

# No of A;s are Divisible by 2            
    if(choice == 3):
        for i in range(0,strlen-1):
            if(string[i] == "a"):
                counter += 1
            
        if(counter%2 == 0):
            print("Your String is Accepted")
        else:
            print("Sorry, String is not Accepted")

# Binary no Divisible By 5
    if(choice == 4):
        temp = binaryno
        while(temp): 
            lastdigit = temp % 10 
            temp = int(temp / 10)          
            decvalue += lastdigit * base 
            base = base * 2 
        if(decvalue%5 == 0):
            print("Your String is Acceptable")
        else:
            print("Sorry, String is not Accepted")


# No of A's Divisible by 4 & b's are not Divisible by 3
    if(choice == 5):
        for i in range(0,strlen ):
            if(string[i] == "a"):
                counter += 1
            if(string[i] == "b"):
                counter2 += 1
            
        if(counter%4 == 0 and counter2%3 != 0):
            print("Your String is Accepted")
        else:
            print("Sorry, String is not Accepted")