#import needed libraries
import numpy as np

#check for win
def is_going(l) :
    for i in range(3) :
        o1 = []
        o2 = []
        if list(l[i]) == 3*["X"] :
            return "x win"
        elif list(l[i]) == 3*["O"] :
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


#game function
def xo(l, p1, n1, n2, ind=9) :
    while is_going(l) == 1 :
        if p1 == "X" :
            pos1 = list(map(int,input(f"{n1} please enter your position(point of (0,0) is in left corer) : ").split()))
            if l[pos1[0], pos1[1]] == "-" :
                l[pos1[0], pos1[1]] = "X"
                print(l)
                print(61*"-")
                ind -= 1
                if is_going(l) != 1 :
                    return is_going(l)
                elif ind == 0 :
                    return "play is drow"
            else :
                while l[pos1[0], pos1[1]] != "-" :
                    print("this position selected!")
                    pos1 = list(map(int,input(f"{n1} please enter your position(point of (0,0) is in left corer) : ").split()))
                    if l[pos1[0], pos1[1]] == "-" :
                        l[pos1[0], pos1[1]] = "X"
                        print(l)
                        print(61*"-")
                        ind -= 1
                        if is_going(l) != 1 :
                            return is_going(l)
                        elif ind == 0 :
                            return "play is drow"
                        break
            pos2 = list(map(int,input(f"{n2} please enter your position(point of (0,0) is in left corer) : ").split()))
            if l[pos2[0], pos2[1]] == "-" :
                l[pos2[0], pos2[1]] = "O"
                print(l)
                print(61*"-")
                ind -= 1
                if is_going(l) != 1 :
                    return is_going(l)
                elif ind == 0 :
                    return "play is drow"
            else :
                while  l[pos2[0], pos2[1]] != "-" :
                    print("this position selected!")
                    pos2 = list(map(int,input(f"{n2} please enter your position(point of (0,0) is in left corer) : ").split()))
                    if l[pos2[0], pos2[1]] == "-" :
                        l[pos2[0], pos2[1]] = "O"
                        print(l)
                        print(71*"-")
                        ind -= 1
                        if is_going(l) != 1 :
                            print(61*"-")
                            return is_going(l)
                        elif ind == 0 :
                            return "play is drow"
                        break
        else :
            pos2 = list(map(int,input(f"{n2} please enter your position(point of (0,0) is in left corer) : ").split()))
            if l[pos2[0], pos2[1]] == "-" :
                l[pos2[0], pos2[1]] = "X"
                print(l)
                print(61*"-")
                ind -= 1
                if is_going(l) != 1 :
                    return is_going(l)
                elif ind == 0 :
                    return "play is drow"
            else :
                while  l[pos2[0], pos2[1]] != "-" :
                    print("this position selected!")
                    pos2 = list(map(int,input(f"{n2} please enter your position(point of (0,0) is in left corer) : ").split()))
                    if l[pos2[0], pos2[1]] == "-" :
                        l[pos2[0], pos2[1]] = "X"
                        print(l)
                        print(61*"-")
                        ind -= 1
                        if is_going(l) != 1 :
                            return is_going(l)
                        elif ind == 0 :
                            return "play is drow"
                        break
            pos1 = list(map(int,input(f"{n1} please enter your position(point of (0,0) is in left corer) : ").split()))
            if l[pos1[0], pos1[1]] == "-" :
                l[pos1[0], pos1[1]] = "O"
                print(l)
                print(61*"-")
                ind -= 1
                if is_going(l) != 1 :
                    return is_going(l)
                elif ind == 0 :
                    return "play is drow"
            else :
                while  l[pos1[0], pos1[1]] != "-" :
                    print("this position selected!")
                    pos1 = list(map(int,input(f"{n1} please enter your position(point of (0,0) is in left corer) : ").split()))
                    if l[pos1[0], pos1[1]] == "-" :
                        l[pos1[0], pos1[1]] = "O"
                        print(l)
                        print(61*"-")
                        ind -= 1
                        if is_going(l) != 1 :
                            return is_going(l)
                        elif ind == 0 :
                            return "play is drow"
                        break


#main function for give inputs and run code
def main() :
    ground = np.array(3*[3*["-"]]).reshape(3,3)
    n1 = input("please enter a name for player1 : ")
    n2 = input("please enter a name for player2 : ")
    p1 = np.random.choice(["X", "O"])
    p2 = "X" if p1=="O" else "O"
    print("The player who is X starts.".center(61))
    print(f"{n1} : {p1}".center(61))
    print(f"{n2} : {p2}".center(61)+"\n")
    print("start".center(61, "-"))
    print(xo(ground, p1, n1, n2))


if __name__ == "__main__" :
    main()
