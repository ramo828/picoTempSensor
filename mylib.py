from math import log


istilik = 0.0
R = 10000
resistor = 0
buffer = 0
Vout = 0
Vin = 3.3

T0 = 298.15
B = 4100
R0 = 5000


def ln(x):
    return log(x)/log(2.7182818284)


def calcTemp(tempRes):
    a = 1/T0
    val = (tempRes/R0)
    c = ln(val)
    b = c/B
    d = a+b
    print("A:",a)
    print("B",b)
    print("C",c)
    print("D",d)
    print("VAL: ",val)
    
    return (1/d)-273.15


def calc(data):
    buffer = data*Vin
    Vout=(buffer)/65535;
    buffer=(Vin/Vout)-1;
    resistor=R*buffer;
    Data=resistor;
    return Data

def ferq(dataA, dataB):
    ferqData = 0
    if(dataA> dataB):
        ferqData = dataA-dataB
    else:
        ferqData = dataB-dataA
    return ferqData

def smoothData(resistorData):
    smooth = 0
    sample = 100000
    for i in range(sample):
        smooth += resistorData 
    
    return smooth/sample
    