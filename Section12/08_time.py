import time as t

print(t.time())
print(t.ctime())
print(t.strftime('%Y-%m-%d(%a) %H:%M:%S'))
print(t.strftime('%Y-%m-%d %A %p %I:%M:%S'))
print(t.strftime('%b/%d/%Y %H:%M:%S'))
print(t.strftime('start time : %Y-%m-%d(%a) %H:%M:%S'))
t.sleep(5) # 입력한 초 동안 멈춤
print(t.strftime('end time : %Y-%m-%d(%a) %H:%M:%S'))