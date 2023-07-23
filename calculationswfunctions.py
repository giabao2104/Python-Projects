def pressure(R,T,v,b,a):
    pressure = ((R*T)/(v-b))-(a/(v**2))
    return pressure

def temperatureup(v,b,a,R):
    temperature = (((v-b)*(1.1+((a)/(v**2)))/(R)))
    return temperature

def temperaturedown(v,b,a,R):
    temperature = (((v-b)*(1.2+((a)/(v**2)))/(R)))
    return temperature

def main():
    R = 0.0820573661
    a = 6.49
    b = 0.0562
    T = float(input("Input Initial Temperature in Kelvin: "))
    v = float(input("Input volar volume in L/mol: "))
    resultingp = pressure(R,T,v,b,a)
    print ("Initial Conditions: ")
    print (f"Molar volume: {v} [L/mol]")
    if v == 0 or v == b:
        print ("Error")
    print (f"Initial temperature = {T}[K]")
    print (f"Parameter a = {a} [L^2*atm/(mol^2)]")
    print (f"Paramenter b = {b} [L/mol]")
    print(f"Resulting pressure = {resultingp:.4f}[atm]")
    
    if pressure(R,T,v,b,a) > 1.2:
        print (f"The temperature change required is {temperaturedown(v,b,a,R)- T:.2f}[K]")
        tempchange = (temperaturedown(v,b,a,R))
        print (f"New temperature = {tempchange:.2f} [K]")
        print (f"New pressure = 1.20 [atm]")
    
    elif pressure(R,T,v,b,a) < 1.1:
        print (f"The temperature change required is {T - temperatureup(v,b,a,R) - T:.2f}[K]")
        tempchange1 = (temperatureup(v,b,a,R))
        print (f"New temperature = {tempchange1:.2f} [K]")
        print (f"New pressure = 1.10 [atm]")
    else: 
        print ("Temperature is acceptable")


if __name__ == ("__main__"):
    main()