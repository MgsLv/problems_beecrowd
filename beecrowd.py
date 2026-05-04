def problema1000():
    print('Hello World!')

def problema1001():
    a = int(input())
    b = int(input())
    x = a + b
    print('X =', x)

def problema1002():
    pi = 3.14159
    raio = float(input())
    area = pi * (raio*raio)
    print("A=%.4f" % area)

def problema1003():
    a = int(input())
    b = int(input())
    soma = a + b
    print(f"SOMA = {soma}")

def problema1005():
    a = float(input())
    b = float(input())
    result = ((a*3.5) + (b*7.5))/11
    print(f"MEDIA = {result:.5f}")

def problema1051():
    renda = float(input())

    if renda <=  2000:
        print("Isento")
    elif renda >= 2000.01 and renda <= 3000.00:
        renda -= 2000
        imposto = (8/100) * renda
        print(imposto)
    elif renda >= 3000.01 and renda <= 4500.00:
        renda -= 3000
        imposto = (8/100) * 1000 + (18/100) * renda
        print(imposto)
    elif renda > 4500.00:
        renda -= 4500
        imposto = (8/100) * 1000 + (18/100) * 1500 + (28/100) * renda
        print(imposto)

def problema1052():
    mes = int(input())

    if mes == 1:
        print("January")
    elif mes == 2:
        print("February")
    elif mes == 3:
        print("March")
    elif mes == 4: 
        print("April")
    elif mes == 5:
        print("May")
    elif mes == 6:
        print("June")
    elif mes == 7: 
        print("July")
    elif mes == 8: 
        print("August")
    elif mes == 9: 
        print("September")
    elif mes == 10: 
        print("October")
    elif mes == 11:
        print("November")
    elif mes == 12: 
        print("December")
    else:
        print("Error")

def problema1541():
    while True:
    try:
    
        numeros = input().split(" ")
        if numeros == "0":
            break
        
        lNum= [int(i) for i in numeros]
        
        calc = (lNum[0] * lNum[1]) * (100/lNum[2])
        result = int(calc ** 0.5)
        
        print(result)
    except EOFError:
        break

def main():
    problema1000()

if __name__ == "__main__":
    main()
