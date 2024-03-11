class Node:
  def __init__(self,elem=None,next=None):
    self.elem = elem
    self.next = next

class Stack:
  def __init__(self):
    self.__top = None

  def push(self,elem):
    nn = Node(elem,self.__top)
    self.__top = nn

  def pop(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    e = self.__top
    self.__top = self.__top.next
    return e.elem

  def peek(self):
    if self.__top == None:
      #print('Stack Underflow')
      return None
    return self.__top.elem

  def isEmpty(self):
    return self.__top == None


class Solution(object):
    def isValid(self, s):
        stack = Stack()
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.push(i)
            elif i==')' and stack.peek()=='(':
                stack.pop()
            elif i=='}' and stack.peek()=='{':
                stack.pop()
            elif i==']' and stack.peek()=='[':
                stack.pop()
            else:
                return False
        return stack.isEmpty()

call1 = Solution()
call1.isValid("()")

call2 = Solution()
call2.isValid("()[]{}")

call3 = Solution()
call3.isValid("(]")