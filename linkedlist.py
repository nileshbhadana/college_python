#!usr/bin/python3
class Node:
	def __init__(self):
		self.coeff=None
		self.expo=None
		self.next=None
class linkedlist:
	def __init__(self):
		self.head=None

	def insert(self):
		coeff=input("Add Coefficient: ")
		expo=input("Add Exponent: ")
		node=Node()
		node.coeff=coeff
		node.expo=expo
		node.next=self.head
		self.head=node
	
	def print_lis(self):
		print_list=self.head
		while print_list:
			print(print_list.coeff,'x^',print_list.expo,'+',end='')
			print_list=print_list.next
	

m=linkedlist()
ch='y'
while True:
	ch=input("Do want to insert another Node (y/n):")
	if ch=='y':
		m.insert()
	else :
		m.print_lis()		
		break
