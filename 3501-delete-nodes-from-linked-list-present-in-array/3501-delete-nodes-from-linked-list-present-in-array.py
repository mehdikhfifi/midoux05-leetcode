# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums_set = set(nums)
        while head and head.val in nums_set:
            head = head.next
        
        temp_head = head
        while temp_head and temp_head.next:
            while temp_head.next and temp_head.next.val in nums_set:
                temp_head.next = temp_head.next.next
                
            temp_head = temp_head.next
        return head


nums = [1]
head = [5,1,1]


            