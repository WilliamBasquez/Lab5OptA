"""
@author: William E Basquez
@Course: CS 2302
@Assignment: Lab 5, Option A
@Instructor: Diego Aguirre
@T.A: Manoj Saha
@Last modification: Nov 27, 2018
"""
class Heap:
	def __init__(self):
		self.heap_array = []

	#This function appends the new elem to the list.
	#It then checks if the new elem is bigger/smaller than its parent
	def insert(self, k):
		self.heap_array.append(k)
		self.percolate_up()

	#This function stores the first element in the list as the min_elem
	#Then it sets the last element to be the new 'root' of the heap
	#As well as it slices the list, getting rid of the last element (already copied as the new root)
	#It then checks, as long as there is a right child, we can compare both children
	#and see which one is the smallest between them, then we percolate down until the set root finds its correct place
	def extract_min(self):
		if self.is_empty():
			return None

		min_elem = self.heap_array[0]
		new_root = self.heap_array.pop()
		
		if len(self.heap_array) > 0:
			self.heap_array[0] = new_root
			self.percolate_down(0)
		
		return min_elem
	
	#This function moves the last added element into the the right position on the heap
	def percolate_up(self):
		if len(self.heap_array) > 1:
			i = len(self.heap_array)-1
			while i > 0:
				j = (i-1)//2
				if self.heap_array[i] < self.heap_array[j]:
					temp_head = self.heap_array[i]
					self.heap_array[i] = self.heap_array[j]
					self.heap_array[j] = temp_head
				i = j
	
	#I took the implementation for this function from zyBook
	def percolate_down(self, index):
		child_index = 2 * index + 1
		elem = self.heap_array[index]

		while child_index < len(self.heap_array):
			min_elem = elem
			min_index = -1
			i = 0
			while i < 2 and i + child_index < len(self.heap_array):
				if self.heap_array[i + child_index] < min_elem:
					min_elem = self.heap_array[i + child_index]
					min_index = i + child_index
				i = i + 1

			if min_elem == elem:
				return
			else:
				temp = self.heap_array[index]
				self.heap_array[index] = self.heap_array[min_index]
				self.heap_array[min_index] = temp

				index = min_index
				child_index = 2 * index + 1
	
	def is_empty(self):
		return len(self.heap_array) == 0

def Heap_sort(h):
	answer = []
	while not h.is_empty():
		answer.append(h.extract_min())
	return answer