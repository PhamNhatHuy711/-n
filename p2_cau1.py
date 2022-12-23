import numpy as np
# câu 1
def tich(a, b):
    tich = a.dot(b)
    print(tich)
    return tich
# câu 2
def tich2(b, c):
    tich = b.dot(c)
    b = b.T
    tich1 = c.dot(b)
    print(tich)
    print(tich1)
def main():
    a = v5 = np.random.randint(low=-3, high=3, size=5)
    b = np.random.randint(low=-5,high=5, size=25).reshape((5,5))
    c = np.random.randint(low=-7, high=7, size=25).reshape((5, 5))
    tich(a, b)
    tich2(b, c)
if __name__ == '__main__':
    main()