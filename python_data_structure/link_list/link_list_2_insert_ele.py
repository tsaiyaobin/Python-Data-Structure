class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    

def insert(node, insert_node):
    if node is None:
        return
    temp = node.next
    node.next = insert_node
    insert_node.next = temp


if __name__ == "__main__":
    # 建立鏈結串列 head -> 5 -> 3 -> 6 -> None
    n1 = ListNode(5)
    n2 = ListNode(3)
    n3 = ListNode(6)
    n1.next = n2
    n2.next = n3
    head = n1
    # 在鏈結串列中插入元素 4，插入後的鏈結串列為 head -> 5 -> 4 -> 3 -> 6 -> None
    n4 = ListNode(4)
    insert(n1, n4)
