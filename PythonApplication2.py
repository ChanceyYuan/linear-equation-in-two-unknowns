print('hello!')
print('Ax2+Bx+C=0')

A = float(input('请输入A：')) 
B = float(input('请输入B：')) 
C = float(input('请输入C：')) 

DELTA = B**2 -4 * A * C

if DELTA < 0 :
    print('方程无解！')
elif DELTA == 0 :
    x = B /(-2 * A)
    print('方程的解为：',x)
else:
    x1 = (B + DELTA**0.5) / (-2*A)
    x2 = (B - DELTA**0.5) / (-2*A)
    print('方程的解为：')
    print('X1=',x1)
    print('X2=',x2)