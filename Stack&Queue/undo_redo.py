global Undo
global Redo

Undo = []
Redo = []

def WRITE(Undo, X):
    Undo.append(X)
 
def UNDO(Undo, Redo):
    X = Undo[-1]
    Undo.pop()
    Redo.append(X)
 
def REDO(Undo, Redo):
 
    X = Redo[-1]
    Redo.pop()
    Undo.append(X)
 
def READ(Undo):
    print(*Undo, sep = "",
          end = " ")
 
def QUERY(Q):
    N = len(Q)
    for i in range(N):
        if(Q[i] == "UNDO"):
            UNDO(Undo, Redo)
        elif(Q[i] == "REDO"):
            REDO(Undo, Redo)
        elif(Q[i] == "READ"):
            READ(Undo)
        else:
            WRITE(Undo, Q[i][6])
 
Q = ["WRITE A", "WRITE B", "WRITE C",
     "UNDO", "READ", "REDO", "READ"]
QUERY(Q)
print()