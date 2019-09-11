#!/usr/bin/env pybricks-micropython

# some basic

# "from...import" is Python way of bringing in someone else's program
# so that you can use it. In this case we are bringing in what LEGO provided
# for Python (called pybricks).
# for example: this line means we will bring in the ev3brick and call it "brick"
# - the programs from which you import are called "libraries"
# - the things you bring in (for example ev3brick) are called "classes"
# - you use those classes by "calling" a "function" on them (we will see examples later)
from pybricks import ev3brick as brick
from pybricks.tools import print, wait

# "call" a function on "brick" (which is what decided to call ev3brick) to make some noise.
# - the name of the function is brick.sound.file
# - we need to make the function know what sound to make, this is done by give a "parameter"
# - the parameter "SoundFile.HELLO" tells the function to say "HELLO"
brick.sound.file(SoundFile.HELLO)

# Call "print" to show something. This prints in your VS Code, not on EV3 
# It is very useful for "debug" so you can see what's going on in your program.
print("Hello, EV3")

# simply wait for 2 seconds (or 2000 milliseconds), don't do anything
wait(2000)

# make some different noise
brick.sound.file(SoundFile.KUNG_FU)

