'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        num=len(lists)
        res=ListNode(0)
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        while len(lists)>1 :
            a=self.mergeTwoLists(lists[0],lists[1])
            lists.append(a)
            lists.remove(lists[0])
            lists.remove(lists[0])
        return lists[0]
        
    def mergeTwoLists(self, l1, l2):
        res=ListNode(0)
        temp=res
        while l1 and l2:
            if l1.val<l2.val:
                temp.next=l1
                temp=temp.next
                l1=l1.next
            else:
                temp.next=l2
                temp=temp.next
                l2=l2.next
        if l1:
            temp.next=l1
        if l2:
            temp.next=l2
        return res.next