# import codecs

from linked_list import LinkedList


class Hashmap:
    def __init__(self,size):
        self.size=size
        self.map = [None]*self.size

    def hash(self, key):
        #split the key into individual characters
        # convert characters to ascii
        # sum all
        total = 0

        for ch in key:
            total += ord(ch)


        # multiple by a prime number
        total *= 19

        # hashed = result % size of
        hashed_key = total % self.size

        return hashed_key

    def add(self,key,value):
        hashed_key = self.hash(key)

        # if the the map is empty at this index, create an emplty linked list at the hashed key index
        if not self.map[hashed_key]:
            #creates an emplty linkedlist node at the index in the map
            self.map[hashed_key] = LinkedList()

        # if a key value pair already exists, this will use the add function in the linkedlist file to add the key/value to the linked list that is currently at the hashmap index
        self.map[hashed_key].add([key, value])

        # return map

        def __str__(self):
            return self.map


    def get(self,key):
        # uses hash function to take in a key as a string and create the hashed key integer
        hashed_key = self.hash(key)

        # take the hashed key integer and make the variable something equal to what is at that hash_key index
        something = self.map[hashed_key]
        return something.display()

        # if there are multiple key:values at an index, loop through the linked list of key:values to find the correct value of the given key

        #1 is there more than one thing at the hash-index
            # - lenght of hash
            # - node.next value != 0



    def contains(self,key):
        hashed_key = self.hash(key)

        # look into the hashmap using the hashed_key
        if self.map[hashed_key]:
            return True
        else:
            return False





# if __name__ == "__main__":
#      hashmap = Hashmap(1024)
#      hashmap.add('ahmad', 30)
#      hashmap.add('silent', True)
#      hashmap.add('listen', 'To me')
#      hashmap.add('lestin', 'Random stuff')
#      hashmap.add('JB', 27)
#      for item in hashmap.map:
#          if item:
#                  print(item.display())
