import matplotlib.pyplot as plt
import numpy as np
from sympy import*
def dao_ham(a, b,c, d, e, x):
    f = a*x**b + c*x**d + e
    answer = diff(f, x)
    return answer

x = np.linspace(start=-10.0, stop=10.0, num=200)
y = x**4 -2*x**2 -3
y1 = 4*x**3-4*x
y2 = 12*x*x-4
y3 = 24*x

def do_thi(x, y, z):
    fig, ax = plt.subplots()
    ax.plot(x, y, label=r'')
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.plot(x, y, label= z)
    ax.set_title("Đồ thị phương trình")
    ax.legend()
    plt.show()
do_thi(x, y,r'$x^4-2x^2-3$')
do_thi(x,y1,r'$4x^3-4x$')
do_thi(x,y2,r'$12x^2-4$')
do_thi(x,y3,r'$24x$')
