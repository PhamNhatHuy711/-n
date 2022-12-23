from sympy import*
# câu 1
def giai_he_pt_3_an(a,b,c,d,e,f,g,h,i,k,l,m,x,y,z,t):
  eq1 = Eq(a*x + b*y + c*z + d*t, 0)
  eq2 = Eq(e*x + f*y + g*z + h*t, 0)
  eq3 = Eq(i*x + k*y + l*z + m*t, 0)
  answer = solve((eq1, eq2, eq3), (x,y,z))
  print(answer)
# câu 2
def gioi_han(x):
    f = pow((x*x*x-3*x*x), (-1/3)) + sqrt(x*x - 2*x)
    answer = limit(f, x, 0)
    print('Kết quả giới hạn: ', answer)
# câu 3
def dao_ham(x):
    f = (2*x -1)/(x+2)
    answer = diff(f, x)
    print(answer)
# câu 4
def tich_phan(x):
    f = x/(x*x + 1)
    answer = integrate(f, x)
    print(answer)
# câu 5
def tich_phan_gioi_han(x):
    f = (1-tan(x)*x)/(x*x*cos(x)+x)
    answer = integrate(f, (x, pi, (2*pi)/3))
    print(answer)
    # câu 6
def main():
    x, y, z = symbols('x y z')
    giai_he_pt_3_an(2,-5,1,5,4,2,-2,-2,1,1,-1,0,x,y,z,1)
    gioi_han(x)
    dao_ham(x)
    tich_phan(x)
    tich_phan_gioi_han(x)
if __name__ == '__main__':
    main()