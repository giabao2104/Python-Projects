r_n = int(input("Enter the number of rows: "))
c_n = int(input("Enter the number of columns: "))

def m_make(r_n, c_n):
    rC = 1 
    matrix = [[]]
    while rC <= r_n: 
        cC = 1 
        list1 = []
        while cC <= c_n:
            value = rC*cC
            if cC == c_n and rC == r_n:
                list1.append(0)

            elif value <= 12: 
                list1.append(value)

            else: 
                list1.append(4)
        cC+=1
    rC+=1
    matrix.append(list1)
    return matrix

list2 = m_make(r_n,c_n)
print (f"The number of rows is {r_n} and columns is {c_n}\n")

with open('out_p.txt','w') as fileout: 
    fileout.write(str(list2))

    
    

print (f"The number of rows is {r_n} and columns is {c_n}\n")
m_make(r_n,c_n)