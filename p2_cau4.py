import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def ham1(x, y):
    z = (x/3)**2 - (y/2)**2
    return z

def ham2(x, y):
    z = np.sqrt(4*(x/3)**2 + 4*(y/5)**2 -4)
    return z

def do_thi1(x, y):
    x, y = np.meshgrid(x, y)
    z = ham1(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf = ax.plot_surface(x, y, z, cmap=cm.cool,linewidth=0, antialiased=False)
    ax.set_zlim(-10, 10)
    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    plt.show()

def do_thi2(x, y):
    x, y = np.meshgrid(x, y)
    z = ham2(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf = ax.plot_surface(x, y, z, cmap=cm.cool,linewidth=0, antialiased=False)
    ax.set_zlim(-10, 10)
    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    plt.show()

def hinh_cau(a, b, c, d):
    u = np.linspace(0, 2*np.pi, 10)
    v = np.linspace(0, np.pi, 10)
    x = (np.outer(np.cos(u), np.sin(v))*d) + a
    y = (np.outer(np.sin(u), np.sin(v))*d) + b
    z = (np.outer(np.ones(np.size(u)), np.cos(v))*d) + c
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    rosen_surf = ax.plot_surface(x, y, z, cmap=cm.cool, linewidth=0)
    fig.colorbar(rosen_surf, shrink=0.5, aspect=5)
    ax.set_title('Hinh cau')
    plt.show()

def main():
    x = np.linspace(start=-10, stop=10, num=1000)
    y = np.linspace(start=-10, stop=10, num=1000)
    do_thi1(x,y)
    do_thi2(x,y)
    hinh_cau(-2,1,4,2)

if __name__ == '__main__':
    main()