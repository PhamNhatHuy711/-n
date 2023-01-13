class NhanVien:
  def __init__(self, fullname, yob, score):
    self.hoten = fullname
    self.tuoi = yob
    self.luong = score
  def __str__(self):
    message = '[Họ và tên : ' + self.hoten + '; Tuổi: ' + str(self.tuoi) + '; Lương : ' + str(self.luong) + ']'
    return message
  def __gt__(self, obj):
    return(self.tuoi > obj.tuoi)
  def __ge__(self, obj):
    return(self.tuoi >= obj.tuoi)
  def __lt__(self, obj):
    return(self.tuoi < obj.tuoi)
  def __le__(self, obj):
    return(sefl.tuoi <= obj.tuoi)
  def __eq__(self, obj):
   return(self.tuoi == obj.tuoi)

def nhap_du_lieu():
  nv = [NhanVien('Phạm Nhật Huy', 18, 20),
        NhanVien('Phan Bá Hùng', 20, 30),
        NhanVien('Trần Hữu Bảo Anh', 40, 60),
        NhanVien('Lê Nguyễn Vũ Duy', 25, 20),
        NhanVien('Phạm Văn Nhật Minh', 34, 40),]
  return nv

def doc_du_lieu(nv):
  for item in nv:
    print(item)

def sap_xep(nv):
  nv1 = nv.cooy()
  nv1 = sorted(nv, reverse= True)
  for item in nv1
    print(item)

def luu_ham(thumuc, ten_taptin, x):
  try:
    with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
      pickle.dump(x, f)
    print('Hoan thanh qua trinh ghi du lieu vao tap tin')
  except Exception as e:
    print(e)
    print('Xay ra loi trong qua trinh ghi file')

def doc_ham():
  try:
    with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
      sv = pickle.load(f)
    return sv
  except Exception as e:
    print(e)

def main():
  nv1 = NhanVien('Phạm Nhật Huy', 18, 10 )
  nv2 = NhanVien('Phan Bá Hùng', 20, 20 )
  nv3 = doc_du_lieu()
  doc_du_lieu(nv3)
  sap_xep(nv3)
  luu_ham()
  print(nv1)
if __name__ == "__main__":
  main()