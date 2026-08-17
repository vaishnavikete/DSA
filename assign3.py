#Display highest sal using bouble sort 
sal = []
n = int(input("enter the number of staff"))
for i in range(n):  
    sal.append(int(input("Enter the sal of staff ")))  
    for i in range(n-1 ):   
       for j in range(n-1 - i):   
        if sal[j]> sal[j+1]:   
           sal[j],sal[j+1]= sal[j+1],sal[j]
           print(sal)  
#Display highest sal using selection sort 
sallary = []
num = int(input('enter the number of staff')) 
for i in range(num): 
     sallary.append(int(input("Enter the sal of staff "))) 
     count = len(sallary)    
for i in range (count - 1 ):
      min_index = i   

for j in range(i + 1,count ):   
       if sallary[j] < sallary[min_index]:      
        min_index = j          
        sallary[i], sallary[min_index]= sallary[min_index],sallary[i] 
       print(sallary)            