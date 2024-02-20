# 5) Write a Python program to implement a stack using a list.(push and pop)
stack = []

def push(item):
    stack.append(item)
    print(f"Pushed {item} into the stack.")

def pop():
    if not stack:
        print("Stack is empty.")
        return None
    else:
        item = stack.pop()
        print(f"Popped {item} from the stack.")
        return item

itm1=input("enter the item1 : ")
itm2=input("enter the item2 : ")
push(itm1)
push(itm2)
print(stack)
pop()
print(stack)
