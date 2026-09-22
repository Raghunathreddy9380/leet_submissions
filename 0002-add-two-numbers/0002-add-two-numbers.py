class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.getNumber(l1)
        num2 = self.getNumber(l2)

        result = num1 + num2

        return self.createList(result)


    def getNumber(self, head):
        node = head
        num = 0
        dec = 1
        while node:
            num += node.val * dec
            dec *= 10
            node = node.next
        return num
            
      
    def createList(self, num):
        dummy = node = ListNode(0)
        if not num:
            return dummy
            
        while num:
            node.next = ListNode(num % 10)
            num = num // 10
            node = node.next

        return dummy.next