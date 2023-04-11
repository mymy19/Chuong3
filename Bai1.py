a=input('a=')
b=input('b=')
c=input('c=')
max = a 
min = b
if max < b:
    max=b
    if max < c:
       print('SLN=',float(c),sep='') 
    else:
        print('SLN=',float(b),sep='') 
elif max < c:
    print('SLN=',float(c),sep='') 
else:
    print('SLN=',float(a),sep='') 

if min > a:
    min = a
    if min > c:
        print('SBN=',float(c),sep='') 
    else: 
        print('SBN=',float(a),sep='') 
elif min >c:
    print('SBN=',float(c),sep='') 
else:
    print('SBN=',float(b),sep='') 
    
        
    

