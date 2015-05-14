class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "->".join([str(self.val)])
