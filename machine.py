def __next_instruction(program):
    val = program.pop(0)
    program.append(val)
    return val

def literal(p,q,s,i,o):
    s.append(__next_instruction(p))

def jump(p,q,s,i,o):
    for i in range(s.pop()):
        __next_instruction(p)

def conditional_jump(p,q,s,i,o):
    x = s.pop()
    if s.pop() != 0:
        for i in range(x):
            __next_instruction(p)

def dequeue(p,q,s,i,o):
    s.append(q.pop(0))

def enqueue(p,q,s,i,o):
    q.append(s.pop())

def cycle(p,q,s,i,o):
    for i in range(s.pop()):
        q.append(q.pop(0))

def size(p,q,s,i,o):
    s.append(len(q))

def get_input(p,q,s,i,o):
    s.append(i.pop(0))

def print_output(p,q,s,i,o):
    o.append(s.pop())

def pop(p,q,s,i,o):
    s.pop()

def swap(p,q,s,i,o):
    x = s.pop()
    y = s.pop()
    s.append(x)
    s.append(y)

def reverse(p,q,s,i,o):
    x = s.pop()
    temp = s[-x::]
    temp.reverse()
    s[-x::] = temp

def duplicate(p,q,s,i,o):
    x = s.pop()
    s.append(x)
    s.append(x)

def add(p,q,s,i,o):
    x = s.pop()
    y = s.pop()
    s.append(y + x)

def subtract(p,q,s,i,o):
    x = s.pop()
    y = s.pop()
    s.append(y - x)

def greater(p,q,s,i,o):
    x = s.pop()
    y = s.pop()
    if y > x:
        s.append(1)
    else:
        s.append(0)

isa = ['stop', literal, jump, conditional_jump, dequeue, enqueue, size, get_input, print_output, pop, swap, reverse, duplicate, add, subtract, greater]
asm = ['stop', 'lit', 'jump', 'cond', 'deq', 'enq', 'size', 'input', 'output', 'pop', 'swap', 'rev', 'dup', 'add', 'sub', 'greater']

def run(program = [], queue = [], stack = [], userin = [], userout = []):
    count = 0
    while True:
        count += 1
        instruction = __next_instruction(program)
        if instruction >= len(isa) or instruction == 0:
            return count
        isa[instruction](program,queue,stack,userin,userout)

def assemble(code = ""):
    program = []
    for line in code.split():
        try:
            val = int(line, 16)
            program.append(val)
        except ValueError:
            if line in asm:
                program.append(asm.index(line))
            else:
                raise ValueError('\'' + line + '\' is not a valid instruction')
        
    return program
        
if __name__ == '__main__':
    program = assemble("""input
dup
lit
0x1
cond
stop
output""")
    userin = [1, 2, 3, 4, 420, 69, 0]
    userout = []
    run(program=program, userin=userin, userout=userout)
    print(userout)