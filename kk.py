class Node:
def __init__(self, data):
self.data = data
self.next = None
class LinkedList:
def __init__(self):
self.head = None
def get_node(self, index):
current = self.head
for i in range(index):
if current is None:
return None
current = current.next
return current
def get_prev_node(self, ref_node):
current = self.head
while (current and current.next != ref_node):

current = current.next
return current
def insert_after(self, ref_node, new_node):
new_node.next = ref_node.next
ref_node.next = new_node
def insert_before(self, ref_node, new_node):
prev_node = self.get_prev_node(ref_node)

self.insert_after(prev_node, new_node)
def insert_at_beg(self, new_node):
if self.head is None:
self.head = new_node
else:
new_node.next = self.head
self.head = new_node
def insert_at_end(self, new_node):
if self.head is None:
self.head = new_node
else:
current = self.head
while current.next is not None:
current = current.next
current.next = new_node

def remove(self, node):
prev_node = self.get_prev_node(node)
if prev_node is None:
self.head = self.head.nextelse:
prev_node.next = node.next
def display(self):
current = self.head

while current:
print(current.data, end = &#39; &#39;)
current = current.next
a_llist = LinkedList()
print(&#39;Menu&#39;)
print(&#39;insert &lt;data&gt; after &lt;index&gt;&#39;)
print(&#39;insert &lt;data&gt; before &lt;index&gt;&#39;)
print(&#39;insert &lt;data&gt; at beg&#39;)
print(&#39;insert &lt;data&gt; at end&#39;)
print(&#39;remove &lt;index&gt;&#39;)
print(&#39;quit&#39;)
while True:
print(&#39;The list: &#39;, end = &#39;&#39;)
a_llist.display()
print()
do = input(&#39;What would you like to do? &#39;).split()
operation = do[0].strip().lower()
if operation == &#39;insert&#39;:
data = int(do[1])
position = do[3].strip().lower()
new_node = Node(data)
suboperation = do[2].strip().lower()
           
