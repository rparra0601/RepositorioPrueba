
# Online Python - IDE, Editor, Compiler, Interpreter
print("-="*40+"-")

def criba_de_eratostenes (n):
    num_primos = []
    criba = list(range(2,n+1))
    #generamos la criba de eratostenes
    while criba != []:
        a = min(criba)
        num_primos.append(a)
        for i in range (a,n+1,a):
            if i in criba:
                criba.remove(i)
    return num_primos
    
n = int(input())
print(criba_de_eratostenes(n))
print("-="*40+"-")

    