a = int(input("ساعت حال حاضر:"))
if a>=0 and a<=6 :
    print ("شب بخیر")
elif a>=7 and a<=12 :
    print ('صبح بخیر')
elif a>=13 and a<=18 :
    print ('عصر بخیر')
elif a>=19 and a<=24 :
    print ('شب بخیر')
else :
    print ('یک عدد در بازه 0 تا 24 وارد کنید')
