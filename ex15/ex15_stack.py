class StackNode(object):
    
    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"{self.value}: {nval}"

class Stack(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        node = StackNode(obj, None)
        if self.end:
            self.end.next = node
            self.end = node
        else:
            self.begin = self.end = node

    def pop(self):
        if self.end:
            if self.begin == self.end:
                result = self.end.value
                self.begin = self.end = None
            else:
                result = self.end.value
                node = self.begin
                while node.next != self.end:
                    node = node.next
                node.next = None
                self.end = node
        else:
            result = None

        return result

    def dump(self, mode='normal'):
        the_list = []
        node = self.begin

        if mode == 'silence':
            silence = True
        else:
            silence = False
        
        if not node:
            if not silence:
                print('Empty List!')
            return None

        the_list.append(node.value)

        while node.next:
            node = node.next
            the_list.append(node.value)

        if not silence:
            print('list: ', the_list)

        return the_list
