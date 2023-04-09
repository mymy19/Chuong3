T=input('')
L=input('')
H=input('')
DTB=(float(T)*2 + float(L)*3 + float(H))/6
if DTB<3:
    print('Kem')
elif 3<= DTB <5:
    print('Yeu')
elif 5<= DTB <6:
    print('Trung binh')
elif 6<= DTB <7:
    print('Trung binh kha')
elif 7<= DTB < 8:
    print('Kha')
elif 8<= DTB < 9:
    print ('Gioi')
else:
    print ('Xuat sac')    

