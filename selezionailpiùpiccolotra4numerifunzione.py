#seleziona il più piccolo tra 4 numeri

def min(a,b,c,d):
    if a<b:
        if a<c:
            if a<d:
                min = a
        
        else:
            min = d
    else:
        if b<c:
            if b<d:
                min = b
        else:
            if c<d:
                min = c
    return min

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))

m = min(a,b,c,d)

print("tra",a,",",b,",",c,"e",d,"il minore è",m)



