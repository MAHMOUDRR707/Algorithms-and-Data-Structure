class Node:
    def __init__(self,head = None):
        self.data =  head
        self.next = None


class LinkedList:
    def __init__(self,head):
        self.head = None

    def append(self,data):
        new_node =  Node(data)
        if self.head is None :
            self.head =  new_node
            return
        cur  = head
        while cur.next is not None :
            cur  = cur.next

        cur.next =  new_node
        return

    def preappend(self,data):
        new_node =  Node(data)
        new_node.next =  self.head
        self.head =  new_node


    def print_link(self):

        if self.head is None:
            return
        cur = head
        while cur  :
            print(cur)
            cur = cur.next

    def insert_after_node(self, prev , data):
        if prev is None :
            return
        new_node = Node(data)
        new_node.next =  prev.next
        prev.next =  new_node

    def delete_with_key(self,key):
        cur  =  self.head
        
        while cur and cur.data  ==  key :
            self.head = cur
            cur = None
            return
        
        prev =  None
        while cur and cur.data != key :
            prev = cur
            cur = cur.next
        if cur ==  None :
            return
        prev.next  = cur.next
        cur = None

    def delete_with_pos(self,pos):
        cur = head
        count = 0

        while cur and count ==  pos :
            self.head =  cur.next
            cur =  None
            return

        prev =  None
        while cur and count != pos-1 :
            prev =  cur
            cur =  cur.next
            count +=1
        if cur is None :
            return

        prev.next = cur
        cur =  None

    def lenght(self):
        l = 0
        if self.head   is None:
            return l 

        cur  = head  
        while cur:
            l+=1
            cur = cur.next
        return l

    def  merge_sort(self,llist):
        p =  self.head
        q  =  llist.head
        if p is None or q is None :
            return

        cur  =  None
        if p.data  >  q.data :
            cur =  q
            cur.next =  self.merge_sort(p,q.next)
        else :
            cur =  p
            cur.next = merget_sort(p.next,q)
        return cur

    def reverse(self):
        if self.head is None:
            return 
        cur  =  self.head
        prev =  None
        while cur is not None :
            next = cur.next
            cur.next =  prev
            prev =  cur
            cur =  next
        self.head =  prev
        
