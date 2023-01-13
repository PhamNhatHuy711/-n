#1. tạo list ngẫu nhiên số thực
import numpy as np
def ngau_nhien_so_thuc(a, b):
    x = []
    for i in range(100):
        v = np.random.random()*(b-a)+a
        x.append(v)
    return x
#2. sắp xếp
def sap_xep(reverse, x):
    #x = ngau_nhien_so_thuc(-5, 5)
    x1 = x.copy()
    if reverse == True:
        for i in range(len(x)-1):
            for j in range(i + 1, len(x)):
                if x1[i] > x1[j]:
                    x1[i], x1[j] = x1[j], x1[i]
    else:
        for i in range(len(x)-1):
            for j in range(i + 1, len(x)):
                if x1[i] < x1[j]:
                    x1[i], x1[j] = x1[j], x1[i]
    return x1
#3. Tìm kiếm
def tim_kiem(x, n):
  flag = False
  for i in range(len(x)):
    if n == x[i]:
      print('vị trí xuất hiện n trong x là: ', i)
      flag = True
  if flag == False:
   print("n không xuất hiện trong x")
  return x
#4 lưu list vào tập tin
def luu_list(a, x, file):
    if a == 'a+':
        with open(file, 'a+', encoding='utf-8') as f:
            f.write(str(x))
            f.write('\n')
    if a == 'b+':
        with open(file, 'b+', encoding='utf-8') as f:
            pickle.load(f)
            f.write('\n')

def main():
    x = ngau_nhien_so_thuc(-5, 5)
    luu_list('a+', x, 'huy')
    x1 = sap_xep(False, x)
    luu_list('a+', x1, 'huy')
    tim_kiem(x1, 6)
if __name__ == '__main__':
    main()