import string
word = input()
wx = word.split()
for i in wx:
    if i in string.ascii_letters:
        wx.remove(i)
print(wx)
print(len(wx))
