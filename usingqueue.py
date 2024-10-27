from queue import LifoQueue
stack=LifoQueue(maxsize=5)
stack.put(4)
stack.put(2)
stack.put(5)
stack.put(6)
print(stack.qsize())
stack.put(9)
print(stack.qsize())
print(stack.full())
stack.get()
stack.put(1)
print(stack.full())
print(stack.empty())