takeInput = True
numbers=""
maxSize=int(199)
minSize=int(0)
   
def low(numbers,position):
    distance=0
    for i in reversed(range(position+1)):
        distance += numbers[i+1]-numbers[i]
        #print(numbers[i+1],'-',numbers[i]," = ",numbers[i+1]-numbers[i])
        numbers.remove(numbers[i+1])
    for i in range(len(numbers)):
            if(numbers[i]==maxSize):
                break;
            else:
                distance += numbers[i+1]-numbers[i]  
                #print(numbers[i+1],'-',numbers[i]," = ",numbers[i+1]-numbers[i])
    
    return(print(distance))


def high(numbers,position):
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
        if numbers[i] == minSize or i == 0:
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
    userinput1= input("Numbers between 0 and 199: ")
    
    if userinput1 =="quit":  
        takeInput=False
        break;
    numbers=userinput1.split(" ") #rozdelenie čisel do array pri medzerách
    numbers2=[]
    for i in range(0,len(numbers)):#odstráneni zbytočných whitespace a iných znakov
        if numbers[i].isnumeric():
            numbers2.append(numbers[i])
    
    numbers=numbers2
    
    for i in range(0,len(numbers)): #ak je nejaké číslo väčise ako max tak skončí program
        numbers[i]=int(numbers[i])
        if(int(numbers[i])>maxSize or int(numbers[i])<minSize):
            userinput1 ="quit"
            
    if userinput1 =="quit":
        print("Wrong input")
        takeInput=False
        break;

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
    print("Write high to move from lower track number to higher track.")
    print("Write low to scan from higher track number to lower track.")
    print("if neither direction is chosen the program will move from lower track number to higher track.")
    userinput3= input("Direction: ")
    userinput3.lower()
    userinput3.strip()
    if userinput3 =="quit":
        takeInput=False
        break;
    
    if userinput3 == "high" or userinput3 == "low" :
        direction = userinput3
    else:
        direction = "high"
        
    #print(numbers)
    #print(userinput2)
    #print(position)
    #print(direction)
    if maxSize not in numbers and direction == "high":
        numbers.insert(len(numbers)+1,maxSize)
    
    if minSize not in numbers and direction =="low" :
        numbers.insert(0,minSize)
    
    if direction == "high":
        high(numbers,position)
        
    elif direction =="low":
        low(numbers,position)
    