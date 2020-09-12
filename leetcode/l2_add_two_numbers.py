class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l1_val = l1.val
        current_mul = 10
        while l1.next:
            l1 = l1.next
            l1_val += current_mul * l1.val
            current_mul *= 10

        l2_val = l2.val
        current_mul = 10
        while l2.next:
            l2 = l2.next
            l2_val += current_mul * l2.val
            current_mul *= 10

        result = l1_val + l2_val
        current_node = ListNode()
        root = current_node

        while True:
            current_node.val = result % 10
            result //= 10
            if result > 0:
                current_node.next = ListNode()
                current_node = current_node.next
            else:
                break
        return root

"""
문제주소 : https://leetcode.com/problems/add-two-numbers/submissions/
시간 : 측정안함


다른 사람 풀이 :
========================================================================================

========================================================================================
노트 :
- 
"""