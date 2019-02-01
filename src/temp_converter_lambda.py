"""temperature converter lambda"""

from __future__ import print_function

import json

print('Loading function')

def f2c(farenheit):
    '''converts f farenheit to celcius'''
    return ((farenheit - 32.0) * 5.0) / 9.0

def c2f(celcius):
    '''converts c celcius to farenheit'''
    return (celcius * 1.8) + 32.0

def handler(event, context):
    '''Provide an event that contains the following keys'''
    print("Received event: " + json.dumps(event, indent=2))

    conversion = event.get('conversion')
    temp = event.get('temp')

    if not temp or not conversion:
        raise ValueError('Missing an argument')

    operations = {
        "f2c": f2c,
        "c2f": c2f
    }

    if conversion in operations:
        return operations[conversion](temp)
    raise ValueError('Unrecognized operation "{}"'.format(conversion))
