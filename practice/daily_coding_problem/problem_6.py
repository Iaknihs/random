"""

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes
and memory addresses.

____________________________________________

Since I can't solve this properly in python, I'll just quickly note down roughly how to do it.
The trick is simple, starting at the first or last node, whose memory location we know, we can xor the 'both' value
of the next element again to retrieve the 'next' memory location. Remember that, go on to the next one, etc. until done.

Naturally, adding and removing elements will require to memorize any pointers relevant.
Honestly, I feel like this just isn't a very good data type to use...
"""