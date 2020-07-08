class Linked_list():
    def __init__(self, collection=None):
        self.head = None    
        if collection:
            for item in reversed(collection):   # [a,b,c] => [a] > [b] > [c] > None
                self.insert(item)
    
    def insert(self, value):
        """adds node to head of new linked list"""
        self.head = Node(value, self.head)
    
    def append(self,value):
        """adds node to end of existing linked list"""
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def __iter__(self):
        """iterator returns generator, gen gives one item at a time when asekd"""
        def value_generator():
            current = self.head

            while current:
                yield current.value
                current = current.next
        return value_generator()

    def __len__(self):
        """returns length of linked list // converts iter by making a list of ll so it can use len // O(N)"""
        # DANGER: NOT O(1) - better IRL to track a left.length
        return len(list(iter(self)))

    def __str__(self):
        output = ''
        for value in self:
            output += f"[ {value} ] -> "
        output += "None"
        return output

    def __eq__(self, other):
        """O(N) compares if two linked lists are equal //list or str works"""
        # using a generator to comapre will save space for early failure
        return list(self) == list(other)

    def __getitem__(self, index):
        """returns item in ll at a given index"""
        # return list(self)[index]  O(N) idx0 still makes an entire list

        if index < 0:
            raise IndexError
        for i, item in enumerate(self): #early success most efficient 
            if i == index:
                return item 
        raise IndexError

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_ 


if __name__ == "__main__":

    foods = Linked_list(['apple', 'banana', 'carrot'])
    first_food = foods[0]
    
    for food in foods:
        print(food)

    def gen():
        
        # for i in range(10):
        #     yield i

        i = 0
        while True:
            yield i 
            i += 1

        for i in range(100):
            print(next(num_gtr))

    num_gtr = gen()
    print(num_gtr)
