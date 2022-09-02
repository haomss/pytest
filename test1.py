# s = "33445"
#
# num = 0
# l = len(s)-1
# # if len(s) == 0:
# #     return
# for i in s:
#     for j in range(10):
#         if i == str(j):
#             n = j*(10**l)
#             print(n)
#             num += n
#             l -= 1
# print(num)


# s = "1,33,44,eee"
# ss = s.split(",")
# print(ss)
# l = []
# for i in ss:
#     l.append(len(i))
# a = l.index(max(l))
# print(ss[a])


# class Solution:
#     def ReverseList(self , head: ListNode) -> ListNode:
#         #处理空链表
#         if not head:
#             return None
#         cur = head
#         pre = None
#         while cur:
#             #断开链表，要记录后续一个
#             temp = cur.next
#             #当前的next指向前一个
#             cur.next = pre
#             #前一个更新为当前
#             pre = cur
#             #当前更新为刚刚记录的后一个
#             cur = temp
#         return pre

class ListNode(object):
    pass


# class Solution:
#     def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
#         #加个表头
#         res = ListNode(-1)
#         res.next = head
#         #前序节点
#         pre = res
#         #当前节点
#         cur = head
#         #找到m
#         for i in range(1,m):
#             pre = cur
#             cur = cur.next
#         #从m反转到n
#         for i in range(m, n):
#             temp = cur.next
#             cur.next = temp.next
#             temp.next = pre.next
#             pre.next = temp
#         #返回去掉表头
#         return res.next

# def test(a,b=[]):
#     b.append(a)
#     return b
#
#
# print(test(1))
# print(test(2))



# class myexception(Exception):
#     def __init__(self,a,b):
#         pass
#         self.v1 = a
#         self.v2 = b
# raise myexception(1,2)

a= {}
a["k1"] = 0
a["k2"] = 0
a["k1"] = a["k1"]+11
a["k2"] = a["k2"]+12
print(a)
for i in a:
    print(i,a[i])
