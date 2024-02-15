# 2. Se dau doua fisiere (A si B). Sa se creeze un al treilea fisier in care sa se insereze alternativ cate o linie din fisierul
# A, respectiv din B. Ulterior, sa se gaseasca frecventa fiecarui caracter. A se stoca intr-un dictionar.

# File A			File B
# ana are			fanica merge
# mere multe		des la munte	
# bune si rele		cu prietenii
# 			dar si singur.
# 			trist

# File C
# ana are
# fanica merge
# mere multe
# des la munte
# bune si rele
# cu prietenii
# dar si singur.
# trist



def doFreq(freq,text):
    for i in text:
        if ord(i)>=ord('a') and ord(i)<=ord('z'):
            current = freq.get(i)
            current += 1
            freq.update({i:current})
    return freq

freq={}
for a in range(ord('a'),ord('z')):
    freq.update({chr(a):int(0)})

# freq.update({' ':int(0)})
# freq.update({'\n':int(0)})
# freq.update({'?':int(0)})
# freq.update({'.':int(0)})
# freq.update({'!':int(0)})

print(freq)

f1 = open(r'p21.txt')
f2 = open(r'p22.txt')
f3 = open(r'p23.txt','r+')

text1 = f1.readline()
text2 = f2.readline()
while text1!='' and text2!='':
    f3.write(text1)
    f3.write(text2)
    # freq=doFreq(freq,text1)
    # freq=doFreq(freq,text2)
    text1 = f1.readline()
    text2 = f2.readline()


while text1!='':
    f3.write(text1)
    # freq=doFreq(freq,text1)
    text1 = f1.readline()

    
while text2!='':
    f3.write(text2)
    # freq=doFreq(freq,text2)
    text2 = f2.readline()

f3.seek(0)
text3 = f3.readline()
while text3 != '':
    print(text3)
    freq=doFreq(freq,text3)
    text3 = f3.readline()



print(freq)
maxValue= max(value for value in freq.values())
maxFreq= [(key,value) for key,value in freq.items() if value==maxValue]
print(maxValue)
print(maxFreq)