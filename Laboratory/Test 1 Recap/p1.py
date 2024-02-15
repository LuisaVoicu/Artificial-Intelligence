# 1. Se da o lista de tuple, fiecare tupla continand un numar n de stringuri. Gasiti tupla in care lungimea 
# stringurilor sa fie cea mai mare. Ulterior, extrageti ultimul string din tupla si returnati un string continand
# concatenarea de 3 ori a jumatatii stangi de caractere ale stringului.

# Exemplu: lista = [("ab", "123456", "lok"), ("epustuflant", "rapso918!", "incomprehensibil"), ("12!", "a", "vestejel")]
# 	 => functie(lista) => "incompreincompreincompre"

def functie(lista,n):
    maxLength=0
    tupla=0
    for t in lista:
        dim = sum(len(string) for string in t)
        if(dim>maxLength):
            maxLength = dim
            tupla = t
    

    string = tupla[n-1]
    halfLenString = int(len(string)/2)
    halfString = string[0:halfLenString]
    result = halfString+halfString+halfString
    print(result)



    
lista = [("ab", "123456", "lok"), ("epustuflant", "rapso918!", "incomprehensibil"), ("12!", "vestejel")]
functie(lista,3)