def file_in():
    try:
        file = input("Enter file name:")
    except TypeError:
        print ("TypeError, please enter a string")
        return
    return file

def Absorb_calc(A,b,e):
    concentration = (A/(b*e))
    return concentration

def main():
    #file = open('out_3.txt','w')
    #file.write("The name of the substance is Glucose Oxidase")
    #file.write(f"For absorbency of___, the concentration is {Absorb_calc(A,b,e)}")

    with open('Example_3input.txt','r') as filein:
        with open('out_3.txt','w') as fileout: 
            substance = filein.readline()
            fileout.write(f"The name of the substance is {substance}.") /{filein.readline}
            b = float(filein.readline())
            e = float(filein.readline())
            for i in filein.readlines():
                i.replace('\n','')
                y = float(i)
                absorbency = float(Absorb_calc(y,b,e))
                fileout.write(f"For the absorbency of {y:.4f}, the concentration is {absorbency:.7f}\n.")

if __name__ == ("__main__"):
    main()


