from node import Node,target_exists,node_count,display_linked_list
# My nodes
a = Node(2)
b = Node(4)
c = Node(6)
d = Node(10)
e = Node(500)
f = Node(-100)
g = Node(0.58)


# Now I connect them
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g


print(target_exists(a,120))
print(node_count(a))
print(display_linked_list(a))