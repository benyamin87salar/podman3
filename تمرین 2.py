import datetime

choose = int(input('halat :'))
if choose == 1 :
    a = int(input("ساعت حال حاضر"))
    while a>=24:
         a = int(input("ساعت حال حاضر"))
    if a>=0 and a<=6 :
        print ("شب بخیر")
    elif a>=7 and a<=12 :
        print ('صبح بخیر')
    elif a>=13 and a<=18 :
        print ('عصر بخیر')
    elif a>=19 and a<=24 :
        print ('شب بخیر')
elif choose == 2 :
    t = datetime.datetime.now()
    houre = t.hour
    if houre>=0 and houre<=6 :
            print ("شب بخیر")
    elif houre>=7 and houre<=12 :
            print ('صبح بخیر')
    elif houre>=13 and houre<=18 :
            print ('عصر بخیر')
    elif houre>=19 and houre<=24 :
            print ('شب بخیر')
