# A Computer Made of Marbles

This is a simulation of a Turing-complete, programmable, mechanical computer that uses marbles for bits. Heavy marbles are 1, light marbles are 0. All data are stored in 5 structures: program, queue, stack, input, and output. These are physical lines of marbles analogous to the digital structures of the same name. The queue and the stack constitute the machine's memory. There is also a register that records the size of the queue. The program, input, and output are similar to queue structures, with the following differences: input cannot be enqueued, output cannot be dequeued, and when the program is dequeued, it immediately re-enqueues the resulting instruction.

`machine.run(program = [], queue = [], stack = [], userin = [], userout = [])` takes the initial state of the machine and updates it in-place. It returns the total number of instructions executed.

`machine.assemble(code = "")` takes assembly code as a string and returns it as a program.

## In the future:
When the machine is physically built and tested, `machine.run()` will also return an estimate of the real execution time.