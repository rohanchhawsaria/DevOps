#!/usr/bin/python

class Hello:
     def __init__(self):
        print("Hello Constructor")
        self.name="Instance1"

     def sayHello(self):
        print("Hello Python!")
        print( self.name )
        print( type( self.name ) )
        self.name = 123
        print( type( self.name ) )

def main():
    hello = Hello()
    hello.sayHello()

#if __name__ == "__main__":
#   main()

main()
