# CS332

For this semester's projec
t, you will be implementing both deadlock avoidance using banker’s
algorithm and deadlock de
tection (both topics are covered in Chapter 6). You will have the
options of using either Py
thon, Java, or C++. Treat your algorithm as a series of functions that
will be passed a series of
 test cases in your main function.
Inputs
​
: allocation matrix,
 claim matrix, and resource vector (you will have to collect the available
vector and C-A  yourself 
using the above inputs)
Outputs: 
​
determination o
f safe state (and your program’s reasoning for it) and a list of all
deadlocked processes.
How you implement your
 inputs is up to you, but you need to be able to identify processes by
their number in the matrix 
(two dimensional array).
Your test cases should b
e numerous and cover all edge cases. If inputs are not formatted
properly or the sizes betw
een matrices and vectors don't match up, your code should return info
on those inconsistencies 
(i.e your code is “stupid-proof”).
