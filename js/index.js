const virtualMachine = require('./vm')

let program1 = [
    "PUSH", 3,
    "PUSH", 4,
    "ADD"
]

virtualMachine(program1)

let program2 = [
    "PUSH", 3,
    "PUSH", 4,
    "ADD",
    "PUSH", 5,
    "MINUS"
]

virtualMachine(program2)
