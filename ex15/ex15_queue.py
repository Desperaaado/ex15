class QueueNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"{pval} <- {self.value} -> {nval}"

class Queue(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        assert obj != None, "You can not push 'None' to a queue"
        if self.end:
            node = QueueNode(obj, None, self.end)
            self.end.next = node
            self.end = node
        else:
            self.begin = self.end = QueueNode(obj, None, None)

    def unshift(self):
        if self.begin:
            if self.begin.next:
                result = self.begin.value
                node = self.begin.next
                node.prev = None
                self.begin = node
            else:
                result = self.begin.value
                self.begin = self.end = None
        else:
            result = None

        return result

    def dump(self):
        the_queue = []

        if self.begin:
            if self.begin == self.end:
                the_queue.append(self.begin.value)
            else:
                the_queue.append(self.begin.value)
                node = self.begin
                while node.next:
                    node = node.next
                    the_queue.append(node.value)
        else:
            pass
        print('list: ', the_queue)
        return the_queue