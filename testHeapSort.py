"""
@author: William E Basquez
@Course: CS 2302
@Assignment: Lab 5, Option A
@Instructor: Diego Aguirre
@T.A: Manoj Saha
@Last modification: Nov 27, 2018
"""
from Heap_class import Heap, Heap_sort

def my_sorted_heaps():
	test1 = [71,31,67,91,75]
	test2 = [14,75,4,84,19,52,1]
	test3 = [90,91,93,31,76,1,39,36,23,82]
	test4 = [7,44,99,30,69,22,73,32,97,49,15,23]

	h1 = Heap()
	h2 = Heap()
	h3 = Heap()
	h4 = Heap()

	for i in test1:
		h1.insert(i)
	for i in test2:
		h2.insert(i)
	for i in test3:
		h3.insert(i)
	for i in test4:
		h4.insert(i)

	sorted_h1 = Heap_sort(h1)
	sorted_h2 = Heap_sort(h2)
	sorted_h3 = Heap_sort(h3)
	sorted_h4 = Heap_sort(h4)

	return sorted_h1, sorted_h2, sorted_h3, sorted_h4

def main():
	answer1 = [31,67,71,75,91]
	answer2 = [1,4,14,19,52,75,84]
	answer3 = [1,23,31,36,39,76,82,90,91,93]
	answer4 = [7,15,22,23,30,32,44,49,69,73,97,99]
	
	print(answer1 == my_sorted_heaps()[0])
	print(answer2 == my_sorted_heaps()[1])
	print(answer3 == my_sorted_heaps()[2])
	print(answer4 == my_sorted_heaps()[3])
	
main()