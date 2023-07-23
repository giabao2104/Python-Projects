def summation(k):
    x = 1/k
    return x


def main():
    target = float(input("Input the target value: "))

    file = open('myoutput.txt','w')
    file.write(f"For a target value of {target}\n")
    file.write("The summation values at each iterations are:\n")
    k = 1
    sum = 0 
    while sum<target:
        sum += (summation(k))
        file.write (f"{sum:.3f}\n")
        k += 1

    file.close()

if __name__ == ("__main__"):
    main()