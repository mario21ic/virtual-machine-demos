def virtual_machine(program = []):
    program_counter = 0
    stack = {}
    stack_pointer = 0

    while program_counter < len(program):
        current_instruction = program[program_counter]
        
        if current_instruction == "PUSH":
            stack[stack_pointer] = program[program_counter + 1]
            stack_pointer += 1
            program_counter += 1

        if current_instruction == "ADD":
            right = stack[stack_pointer - 1]
            stack_pointer -= 1
            left = stack[stack_pointer -1]
            stack_pointer -= 1

            stack[stack_pointer] = left + right
            stack_pointer += 1

        if current_instruction == "MINUS":
            right = stack[stack_pointer - 1]
            stack_pointer -= 1
            left = stack[stack_pointer -1]
            stack_pointer -= 1

            stack[stack_pointer] = left - right
            stack_pointer += 1

        program_counter += 1

    print("stacktop: " + str(stack[stack_pointer - 1]))

