#!/usr/bin/env python
from awesome_print import ap

objects = [
        None,
        True,
        "Hello, World!",
        65535,
        3.1415926,
        [1,2,3,4,5],
        {'one': 1, 'two': 2, 'ten': 10},
        {
            'one': 1,
            'two': ['uno', 'dos', 'tres'],
            'six': {
                'ein': 1,
                'zwei': 2,
                'drei': 3
            }
        }
        ]

print '>> from awesome_print import ap'
for object in objects:
    if type(object) is str:
        print '>> ap("' + str(object) +'")'
    else:
        print '>> ap(' + str(object) +')'
    ap(object)
