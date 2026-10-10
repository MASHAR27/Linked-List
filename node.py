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
        
                
                