

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if (head == None):
        head = SinglyLinkedListNode(data)
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = SinglyLinkedListNode(data)
    return head

