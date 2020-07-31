import linkedList as l


# reverse the linked list
def helperFunction(myLinkedList, current, previous):
    if current.next is None:
        myLinkedList.head = current
        current.next = previous
        return

    next = current.next
    current.next = previous

    helperFunction(myLinkedList, next, current)


def reverse(myLinkedList):
    if myLinkedList.head is None:
        return

    helperFunction(myLinkedList, myLinkedList.head, None)

# create nth element of the Fibonaci sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


myLinkedList = l.LinkedList()
# add first 100 elements of the Fibonacci sequence to linked list
for i in range(0, 100, 1):
    myLinkedList.append(fibonacci(i))


print("Original linked list for the first 100 elements of the Fibonacci sequence")
myLinkedList.printList()

reverse(myLinkedList)
print("\nReversed linked list for the first 100 elements of the Fibonacci sequence")
myLinkedList.printList()
