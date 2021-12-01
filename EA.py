
takeInput = True

maxSize=int(100)
minSize=int(0)
while takeInput == True:
    
    print("######################")
    print("Hello user, please enter the numbers for the Elevator algorithm.")
    print("Separate them with space and once you are done press enter:")
    print("You can also write 'quit' to exit the program.")
    userinput1= input("Numbers between 0 and 100: ")
    
    if userinput1 =="quit":
        takeInput=False
        break;

    numbers=userinput1.split(" ")
    for i in range(0,len(numbers)):
        numbers[i]=int(numbers[i])
        if(int(numbers[i])>maxSize):
            userinput1 ="quit"
        elif(int(numbers[i])<minSize):
            userinput1 ="quit"
            
    if userinput1 =="quit":
        takeInput=False
        break;


    numbers.sort()
    numbers.insert(0,0)
    
    numbers.insert(len(numbers)+1,maxSize)
    print(numbers)
    userinput2str= input("Please enter the starting position: ")
    
    if userinput2str =="quit":
        takeInput=False
        break;
    
    userinput2=int(userinput2str)
    
    
    print("Please enter the scanning direction.")
    print("Write left to scan from right to left.")
    print("Write right to scan from left to right:")
    print("if neither direction is chosen the program will move from left to right.")
    userinput3= input("Direction: ")
    
    if userinput3 =="quit":
        takeInput=False
        break;
    
    
    if userinput3 == "left" or userinput3 == "right" :
        direction = userinput3
    else:
        direction = "right"
        
    
    
    
    if userinput1 =="quit":
        takeInput=False
        break; 