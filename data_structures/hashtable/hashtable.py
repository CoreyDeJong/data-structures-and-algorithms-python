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
        ## code help from geeksforgeeks
        hashed_key = self.hash(key)

        if self.map[hashed_key]:
            ll = self.map[hashed_key]

            while ll.head:
                if ll.head.data[0] == key:
                    return ll.head.data[1]
                else:
                    ll.head = ll.head.next
        else:
            return None




    def contains(self,key):
        hashed_key = self.hash(key)

        # look into the hashmap using the hashed_key
        if self.map[hashed_key]:
            return True
        else:
            return False

## collaborated with Vij on this code
def left_join_hashtable(table1, table2):
    # print("this is table1", table1)
    # print("this is table2", table2)
    output = []
    #iterate over the table1
    # for i in range(len(table1.map)):
    #     #check for match in table2 at these spots
    #     if table1.map[i] and table2.map[i]:
    #         # print(table1.map[i],table2.map[i])
    #         output.append(table1.map[i])
    #         output.append(table2.map[i])
    #     elif table1.map[i]:
    #         # print(table1.map[i])
    #         output.append(table1.map[i])


    for key in table1:
        key_word = key
        synonym = table1[key]
        # this will get the value in table2 for the key, .get will only get the value if it exists, if not None
        antonym = table2.get(key, None)
        trio = [key_word, synonym, antonym]
        output.append(trio)

    return output


if __name__ == "__main__":
    table1 = Hashmap(10)
    table2 = Hashmap(10)
    table1.add("JB",27)
    table1.add("Vij",32)
    table2.add("JB", 55)
    table2.add("Corey",12)
    left_join_hashtable(table1, table2)
