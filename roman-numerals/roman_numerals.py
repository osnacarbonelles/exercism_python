def roman(number):
    units = [("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),
        ("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)]


    numeral = ""
    nn = number
    for ii in range(len(units)):
        factor = nn // units[ii][1]
        if factor>0:
            numeral += units[ii][0] * factor
            nn -= factor*units[ii][1]        
    return numeral
