takeInput = True
numbers=""

maxSize=int(100)
minSize=int(0)


      
def left(numbers,position):
    distance=0
    for i in reversed(range(position)):
        distance += numbers[i+1]-numbers[i]
        #print(numbers[i+1],'-',numbers[i]," = ",numbers[i+1]-numbers[i])
        numbers.remove(numbers[i+1])
        
    for i in range(len(numbers)):
            if(numbers[i+1]==maxSize):
                break;
            else:
                distance += numbers[i+1]-numbers[i]  
                #print(numbers[i+1],'-',numbers[i]," = ",numbers[i+1]-numbers[i])
    
    
    return(print(distance))


def right(numbers,position):
    distance=0
    
    for i in range(position,len(numbers)):
        if numbers[i] == maxSize:
            break;
        else:
            distance += numbers[i+1]-numbers[i]
            #print(numbers[i+1],'-',numbers[i]," = ",numbers[i+1]-numbers[i])
        
    numbers=numbers[:position]
    
    numbers.insert(len(numbers)+1,maxSize)  
    
    for i in reversed(range(len(numbers))):
        if numbers[i] == minSize:
            break;
        else:
            distance += numbers[i]-numbers[i-1]
            #print(numbers[i],'-',numbers[i-1]," = ",numbers[i]-numbers[i-1])
  

    return(print(distance))   


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
        if(int(numbers[i])>maxSize or int(numbers[i])<minSize):
            userinput1 ="quit"
            
    if userinput1 =="quit":
        print("Wrong input")
        takeInput=False
        break;


    if minSize not in numbers:
        numbers.insert(0,minSize)

    if maxSize not in numbers:
        numbers.insert(len(numbers)+1,maxSize)
        
        
    numbers.sort()
    
    userinput2str= input("Please enter the starting position: ")
    
    if userinput2str =="quit":
        takeInput=False
        break;
    
    userinput2=int(userinput2str)
    
    
    if (userinput2>maxSize or userinput2<minSize ):
        break;
    

    for i in range(len(numbers)):
        if numbers[i]>userinput2:
            position=i
            break
        
    numbers = numbers[:position] + [userinput2] + numbers[position:]
        
    
    
    
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
        
    #print(numbers)
    #print(userinput2)
    #print(position)
    #print(direction)
    
    
    if direction == "right":
        right(numbers,position)
        
    elif direction =="left":
        left(numbers,position)
    
    
    
    
    if userinput1 =="quit":
        takeInput=False
        break; 
        
        
        
  