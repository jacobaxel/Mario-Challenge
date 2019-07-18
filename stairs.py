# Code your functions here!
# descending stairs
# ascending stairs
# pyramid

def downstairs(numberstairs):
    for x in range(1,numberstairs+1):
        print("#"*x)
        
# downstairs(4)

def upstairs(numberstairs):
    for x in range(1,numberstairs+1):
        flights=(' '*(numberstairs-x))+'#'*x
        print(flights)
        
# upstairs(6)

def pyramid(numberstairs):
    for x in range(1,numberstairs+1):
        flights=(' '*(numberstairs-x))+'#'*x + ' ' + '#'*x
        print(flights)

# pyramid(4)