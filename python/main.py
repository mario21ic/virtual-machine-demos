#!/usr/bin/env python

from vm import virtual_machine

virtual_machine([
    "PUSH", 3, 
    "PUSH", 4, 
    "ADD"
])

virtual_machine([
    "PUSH", 3, 
    "PUSH", 4, 
    "ADD",
    "PUSH", 5,
    "MINUS"
])
