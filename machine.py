def next_instruction(program):
    val = program.pop(0)
    program.append(val)
    return val

def literal(p,q,s,i,o):
    s.append(next_instruction(p))

def jump(p,q,s,i,o):
    for i in range(s.pop()):
        next_instruction(p)

def jump_conditional(p,q,s,i,o):
    x = s.pop()
    if s.pop() != 0:
        for i in range(x):
            next_instruction(p)

def read(p,q,s,i,o):
    s.append(q.pop(0))

def write(p,q,s,i,o):
    q.append(s.pop())

def cycle(p,q,s,i,o):
    for i in range(s.pop()):
        q.append(q.pop(0))

def size(p,q,s,i,o):
    s.append(len(q))

def print_user(p,q,s,i,o):
    o.append(s.pop())

def read_user(p,q,s,i,o):
    s.append(i.pop(0))

def pop(p,q,s,i,o):
    s.pop()

def swap(p,q,s,i,o):
    x = s.pop()
    y = s.pop()
    s.append(x)
    s.append(y)

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

isa = ['stop', literal, jump, jump_conditional, read, write, size, print_user, read_user, pop, swap, duplicate, add, subtract, greater]

def run(program = [], queue = [], stack = [], userin = [], userout = []):
    while True:
        instruction = next_instruction(program)
        if instruction >= len(isa) or instruction == 0:
            break
        isa[instruction](program,queue,stack,userin,userout)

def assemble(code = ""):
    return []
        
if __name__ == '__main__':
    program = [0x1, 69, 0x1, 420, 0x7, 0x7, 0x0]
    userout = []
    run(program=program, userout=userout)
    print(userout)