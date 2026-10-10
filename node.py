class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
        
def target_exists(head,target):
    current = head
    
    while current is not None:
        if current.value == target:
            return True
        current = current.next
        
        
    return False     
        
 
def node_count(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next 
    
    return count    
     
                
                

def display_linked_list(head):
    current = head
    
    while current is not None:
        print(current.value,end="->")
        current = current.next                
        
        
        
        
        