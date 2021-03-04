def literal(p,s,q,i,o):
    x = p.pop(0)
    p.append(x)
    s.append(x)

def jump(p,s,q,i,o):
    temp = []
    for i in range(s.pop()):
        temp.append(p.pop(0))
    p.extend(temp)

def conditional_jump(p,s,q,i,o):
    x = s.pop()
    if s.pop() != 0:
        temp = []
        for i in range(x):
            temp.append(p.pop(0))
        p.extend(temp)

def dequeue(p,s,q,i,o):
    s.append(q.pop(0))

def enqueue(p,s,q,i,o):
    q.append(s.pop())

def cycle(p,s,q,i,o):
    for i in range(s.pop()):
        q.append(q.pop(0))

def size(p,s,q,i,o):
    s.append(len(q))

def get_input(p,s,q,i,o):
    s.append(i.pop(0))

def print_output(p,s,q,i,o):
    o.append(s.pop())

def pop(p,s,q,i,o):
    s.pop()

def duplicate(p,s,q,i,o):
    x = s.pop()
    s.append(x)
    s.append(x)

def swap(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    s.append(x)
    s.append(y)

def rotate_up(p,s,q,i,o):
    x = s.pop()
    y = s.pop(-x-1)
    s.append(y)

def rotate_down(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    s.insert(-x,y)

def add(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    s.append(y + x)

def subtract(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    s.append(y - x)

def multiply(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    s.append(y * x)

def less(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    if y < x:
        s.append(1)
    else:
        s.append(0)

def greater(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    if y > x:
        s.append(1)
    else:
        s.append(0)

def equal(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    if y == x:
        s.append(1)
    else:
        s.append(0)

def not_equal(p,s,q,i,o):
    x = s.pop()
    y = s.pop()
    if y != x:
        s.append(1)
    else:
        s.append(0)

isa = ['stop', literal, jump, conditional_jump, dequeue, enqueue, cycle, size, get_input, print_output, pop, swap, rotate_up, rotate_down, duplicate, add, subtract, multiply, less, greater, equal, not_equal]
asm = ['stop', 'lit', 'jump', 'cond', 'deq', 'enq', 'cycle', 'size', 'input', 'output', 'pop', 'swap', 'rotup', 'rotdown', 'dupl', 'add', 'sub', 'mul', 'less', 'greater', 'eq', 'neq']

def run(program = [], stack = [], queue = [], userin = [], userout = []):
    count = 0
    while True:
        count += 1
        instruction = program.pop(0)
        program.append(instruction)
        if instruction >= len(isa) or instruction == 0:
            return count
        isa[instruction](program,stack,queue,userin,userout)

def step(program = [], stack = [], queue = [], userin = [], userout = []):
    instruction = program.pop(0)
    program.append(instruction)
    if instruction >= len(isa) or instruction == 0:
        return 0
    else:
        isa[instruction](program,stack,queue,userin,userout)
        return 1

def assemble(code = ""):
    program = []
    for line in code.split():
        try:
            val = int(line, 16)
            program.append(val)
        except ValueError:
            if line[0] == '#':
                pass
            elif line in asm:
                program.append(asm.index(line))
            else:
                raise ValueError('\'' + line + '\' is not a valid instruction')
    return program
        
if __name__ == '__main__':
    program = assemble("#hello_world input dupl lit 0x1 cond stop output")
    userin = [1, 2, 3, 420, 69, 0]
    userout = []
    print('input = ', userin)
    count = run(program=program, userin=userin, userout=userout)
    print('instructions executed: ', count)
    print('output = ', userout)