class Solution:
    def merge(self, l, r):
        if not l or not r:
            return l or r

        head = diter = ListNode(-1)
        while l and r:
            if l.val < r.val:
                diter.next = l
                l = l.next
            else:
                diter.next = r
                r = r.next
            diter = diter.next
        diter.next = l or r
        return head.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)
