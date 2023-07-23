def summation_function(x,n):
    t = x/n 
    return t

def main():
    x = float(input("Input x: "))
    cutoff = float(input("Input cutoff: "))
    file_out = open('file_out.txt','w')

    n = 1
    sum = 0
    series = 0 
    list_of_values = []
    while sum < cutoff: 
        sum+=summation_function(x,n)
        list_of_values.append(sum)
        file_out.write(f"{sum}\n")
        series +=1
    
    value = (list_of_values[-1] - list_of_values[-2])
    file_out.write(f"Number of terms: {series}\n")
    file_out.write(f"Diff = {value}\n")
    file_out.close()

main()