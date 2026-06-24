# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local variable

def func1():
    a = 1
    print(a)
def func2():
    b = 2
    print(b)
func1()
func2()

# Enclosed variables

def func1():
    x = 10
    def func2():
        print(x)
    func2()
    
func1()

# Global scope

def func1():
    print(x*1)
def func2():
    print(x*2)
x = 2

func1()
func2()

from math  import e
def func1():
    print(e)
    
# e = 3 this will override
func1()