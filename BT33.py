x=float(input('x='))
y=float(input('y='))
ch=input('Phep toan:')
if ch=='+' or  ch== '-'or ch=='*'or ch=='/':
    if ch=='+':
        print('',x,end='+',sep='')
        print('',y,end='=',sep='')
        print('',x+y,sep='')
    elif ch=='-':
        print('',x,end='-',sep='')
        print('',y,end='=',sep='')
        print('',x-y,sep='')
    elif ch=='*':
        print('',x,end='*',sep='')
        print('',y,end='=',sep='')
        print('',x*y,sep='')
    elif ch=='/':
        if y==0:
            print('Khong hop le')
        else:
            print('',x,end='/',sep='')
            print('',y,end='=',sep='')
            print('',x/y,sep='')
    
else:
    print('Khong hop le')
        
     