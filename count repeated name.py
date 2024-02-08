#using while loop


dict={}
list1=[]

while True:

    line=input('enter line or press enter to end : ')
    
    if line=="":
        break
        
    list1.append(line)
    
    dict[line]= list1.count(line)
    
print(dict)
    

##########################################


#using for loop

dict={}
list1=[]


for i in range(50):   #number of times you want to repeat the loop
    line=input('enter line or press enter to end : ')
    
    if line=="":
        break
        
    list1.append(line)
    
    dict[line]= list1.count(line)
    
    print(dict)