class Link_list():
    def __init__(self, val):
        self.val = val
        self.next = None

def visited(head):
    while head is not None:
        print(head.val,'->',end = " ")
        head = head.next
    print('None')
    
if __name__ == "__main__":
    n1 = Link_list(5)
    n2 = Link_list(4)
    n3 = Link_list(3)
    n4 = Link_list(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head = n1
    visited(head)