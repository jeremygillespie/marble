# A Computer Made of Marbles

This is a simulation of a Turing-complete, programmable, mechanical computer that uses marbles for bits. Heavy marbles are 1, light marbles are 0. All data are stored in structures: program, queue, stack, input, and output. These are physical lines of marbles analogous to the digital structures of the same name. The queue and the stack constitute the machine's memory. There is also a register that records the size of the queue. The program, input, and output are also queue structures, however they are subject to certain constraints. The machine cannot push to input nor pop from output. When an instruction is read from the program, it is also appended to the program to create looping functionality.

`machine.run(program = [], queue = [], stack = [], userin = [], userout = [])` takes the initial state of the machine and updates it in-place.

In the future, `machine.assemble(code = "")` will take some assembly code and return a valid program.