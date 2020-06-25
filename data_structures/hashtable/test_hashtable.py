import pytest
from hashtable import *
from linked_list import *



def test_add():
    hashmap = Hashmap(10)
    hashmap.add('Corey', 37)
    hashmap.add('Kristin', 33)
    hashmap.add('Porter', 14)
    actual = hashmap.get('Corey')
    expected = [['Corey', 37]]
    assert actual == expected

def test_contains_true():
    hashmap = Hashmap(10)
    hashmap.add('Corey', 37)
    hashmap.add('Kristin', 33)
    hashmap.add('Porter', 14)
    actual = hashmap.contains('Corey')
    expected = True
    assert actual == expected

def test_contains_false():
    hashmap = Hashmap(10)
    hashmap.add('Corey', 37)
    hashmap.add('Kristin', 33)
    hashmap.add('Porter', 14)
    actual = hashmap.contains('Bob')
    expected = False
    assert actual == expected


# hashmap = Hashmap(1024)
# hashmap.add('corey','37')

# .get will return the value of the key
# hashmap.get('corey')
# this will return '37'

##### Left Join #######
def test_demo1():

    hashmap1 = {
        'fond' : 'enamored',
        'wrath' : 'anger',
        'diligent' : 'employed',
        'outfil' : 'garb',
        'guide' : 'usher',
    }

    hashmap2 = {
        'fond' : 'averse',
        'wrath' : 'delight',
        'diligent' : 'idle',
        'guide' : 'follow',
        'flow' : 'jam',
    }

    actual = left_join_hashtable(hashmap1, hashmap2)
    expected = [
        ['fond', 'enamored', 'averse'],
        ['wrath', 'anger', 'delight'],
        ['diligent', 'employed', 'idle'],
        ['outfil', 'garb', None],
        ['guide', 'usher', 'follow']
    ]
    assert actual == expected



