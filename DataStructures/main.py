# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# n1 = Node(2)
# n2 = Node(3)
# n3 = Node(4)

# n1.next = n2
# n2.next = n3

# current = n1

# while current:
#     print(current.data)
#     current = current.next
    

# stack = [] 

# stack.append(20)
# stack.append(30)
# stack.append(40)

# print(stack)

# print(stack.pop())

# print(stack)


# from collections import deque

# queue = deque()

# queue.append(20)
# queue.append(30)
# queue.append(40)

# print(queue)

# print(queue.popleft()) #Pops first element
# print(queue.pop())  #Pops last Element

# print(queue)


import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 30)

print(heap)

print(heapq.heappop(heap)) #Removed 10 Smallest element Min Heap 

print(heap)

#Python doesn't have max heap 
#so we store negative numbers and 

import heapq

heap = []

heapq.heappush(heap, -10)
heapq.heappush(heap, -20)
heapq.heappush(heap, -30)

print(heap)  

print(-heapq.heappop(heap))  # 30 Max Heap 
