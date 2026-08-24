# Exercise 1: Warmup

Practice using the tools and workflow we will use in this course.

Demonstrate the ability to read and run a test suite, write Python code, and
submit your work in Canvas.

## What to Do

Implement a simple, naive Vacuum class that exposes an API relevant to the
"Vacuum World" problem in the AIMA book. For example, if a vacuum can jump, you
would implement a `jump` method. You will only need to stub these methods.
In other words, you merely need to define the methods and the method bodies can
be empty.

**Tip**: learn how to use Python's `pass` keyword.

Your goal is to pass the test suite in *test_vacuum.py*, which guides you through
implementing a naive API for a Vacuum class.

### Instructions

Open the *test_vacuum.py* file and read it. Only read it - do not modify this file.
You will find that many tests are commented out, but that the first test is not.

Run the test suite.

`python3 -m unittest test_vacuum`

Notice how the first test runs and reports a failure. Implement just enough
code to pass the test. Run the test suite again to verify that your tests are
passing.

Next, uncomment the next test in *test_vacuum.py*, save it, run the test suite
again, and see that the test is failing. Pass this test, and all subsequent
tests one at a time.

Run the test suite frequently.

You will know when you are done when you have uncommented all the tests in
*test_vacuum.py*, and the entire test suite passes.

&copy; 2023 Yong Joseph Bakos. All rights reserved.
