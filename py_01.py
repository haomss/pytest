# import os
# print(os.getcwd()) #获取当前路径
# print(os.listdir("./")) #同ls
# if os.path.exists("b") == False:
#     os.mkdir("b")
# if not os.path.exists("/b/test.txt"):
#     f = open("b/test.txt","w")
#     f.write("hms")
#     f.close()
# os.remove("b/test.txt")
# os.removedirs("b")

# import time
# print(time.asctime()) #Mon Aug 29 19:38:14 2022
# print(time.time()) #1661773135.58261时间戳
# print(time.localtime()) #time.struct_time(tm_year=2022, tm_mon=8, tm_mday=29, tm_hour=19, tm_min=39, tm_sec=56, tm_wday=0, tm_yday=241, tm_isdst=0)
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) #2022-08-29 19:43:37
# #获取两天前的时间
# before2 = time.time() - 60*60*24*2
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(before2)))

import math

print(math.ceil(1.2)) #2
print(math.floor(1.2)) #1
print(math.sqrt(36)) #立方根
