class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

if __name__ == "__main__":
    # 建立鏈結串列 head -> 5 -> 3 -> 6 -> None
    n1 = ListNode(5)
    n2 = ListNode(3)
    n3 = ListNode(6)
    n1.next = n2
    n2.next = n3

