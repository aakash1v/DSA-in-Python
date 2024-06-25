class Node:
	def __init__(self,k):
		self.key = k
		self.next = None


def display(head):
	curr = head
	print('Printing the elements of the linked list ') 
	while curr!= None:
		print(curr.key,end =',')
		curr = curr.next
	print('\n - - - - - - ')

def search(head,x):
	pos = 1
	curr = head
	while curr !=None:
		if curr.key ==x:
			return pos
		curr = curr.next
		pos +=1
	return -1

#inserting at the beginning of linked list
def insertBegin(head,key):
	temp = Node(key)
	temp.next = head
	return temp

# inserting at the end of the linked list
def insertEnd(head,key):
	curr = head
	temp = Node(key)
	while(curr.next !=None):
		curr= curr.next
	curr.next = temp

#insert at the positino in linked list
def insertPos(head,key,pos):
	temp = Node(key)
	if pos == 1:
		temp.next = head
		return temp
	curr = head
	for i in range(pos-2):
		curr = curr.next
		if curr.next  == None:
			return head
	temp.next = curr.next
	curr.next = temp
	return head

#delete first Node
def deleteFirst(head):

	if head.next == None or head == None:
		return None
	head = head.next
	return head
#delete last node
def deleteLast(head):
	if head ==None or head.next ==None:
		return None
	
	curr = head
	while curr.next.next !=None:
		curr = curr.next
	curr.next = None
	return head


			

# Driver code..
temp1 = Node(10)
temp2 = Node(20)
temp3 = Node(30)
temp1.next = temp2
temp2.next = temp3
head = temp1

display(head)
print(search(head,20))

head = insertBegin(head,50)
insertEnd(head,100)
head = insertPos(head,200,3)
display(head)
head = deleteFirst(head)
display(head)
head = deleteLast(head)
display(head)
