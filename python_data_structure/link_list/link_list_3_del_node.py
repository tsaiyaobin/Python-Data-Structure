class Link_list():
    def __init__(self, val):
        self.val = val
        self.next = None
# 刪除節點後的節點，eg:要刪除n3節點
def delete(node):
    if node is None or node.next is None:
        return
    temp = node.next
    node_next = temp.next
    node.next = node_next 
    '''
    node.next = node.next.next
    '''
if __name__ == "__main__":
    n1 = Link_list(5)
    n2 = Link_list(4)
    n3 = Link_list(3)
    n4 = Link_list(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head = n1
    delete(n2)
    cur = head
    while cur is not None:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")