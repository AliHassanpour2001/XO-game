#import needed libraries
import numpy as np

#a function for print beautiful
def print_ground(ground) :
    for i in ground :
        print(str(i)[1:-1].replace(",", " ").replace("'", ""))


#main function for give inputs and run code
def main() :
    ground = 3*[3*["-"]]
    print(print_ground(ground))


if __name__ == "__main__" :
    main()
