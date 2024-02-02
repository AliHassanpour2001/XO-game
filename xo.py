#import needed libraries
import numpy as np


#check for win
def is_going(l) :
    for i in range(3) :
        o1 = []
        o2 = []
        if l[i] == 3*["X"] :
            return "x win"
        elif l[i] == 3*["O"] :
            return "O win"
        check = []
        for j in range(3) :
            o1.append(l[j,j])
            o2.append(l[j,2-j])
            check.append(l[i,j])
        if check == 3*["X"] :
            return "X win"
        elif check == 3*["O"] :
            return "O win"
        elif o1 == 3*["X"] or o2 == 3*["X"] :
            return "X win"
        elif o1 == 3*["O"] or o2 == 3*["O"] :
            return "O win"
    return 1
        
        



#main function for give inputs and run code
def main() :
    ground = np.array(3*[3*["-"]]).reshape(3,3)
    l = ["X", "O"]
    n1 = input("please enter a name for player1 : ")
    n2 = input("please enter a name for player2 : ")
    p1 = np.choose(l)
    p2 = "O" if p1=="X" else "O"
    starter = np.choose(l)
    print("start".center(51, "-"))
    print()


if __name__ == "__main__" :
    main()
