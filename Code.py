```python
import sys
import time
def prove_some_integers_are_even():
    
    print("Theorem: If a\u00b2 is even, then a must also be even.")
    input("\nWe are proving that a\u00b2 must be even if a is also even through proof by contradiction. (Press enter to continue...)")
    
    input("Proof by Contradiction: Assume that a\u00b2 is even and a is odd. Therefore, a = 2k + 1. (Press enter to continue...)")
    
    print("a = 2k + 1 (an odd integer) can be proven by entering any integer for k. Let's test this.")
    time.sleep(2)
    
    while True:
        k = input("\nEnter an integer: ")
        if k.isdigit():
            number_int = int(k)
        
            SumOfA = 2*number_int + 1
        
            if SumOfA %2 == 0:
                input(f"\n2*{number_int} + 1 = {SumOfA}, which is an even integer. This should not be possible as we assumed 2k+1 is odd. Ending program.")
                sys.exit()
            else:
                input(f"\n2*{number_int} + 1 = {SumOfA}, which is an odd integer. (Press enter to continue...)")
                break
        else:
            print("\nThis is not a number.")
            time.sleep(1)
    
    print("Let's now find what a\u00b2 is:")
    time.sleep(0.8)
    input("\n(Press enter to advance through each step...)")
    input("(a)\u00b2 = (2k + 1)\u00b2")
    input(" a\u00b2   = 4k\u00b2 + 4k + 1")
    input(" a\u00b2   = 2(2k\u00b2 + 2k) + 1")
    input("We can now see that a\u00b2 = an even number + 1, which will result in an odd number. This is a contradiction as a\u00b2 is supposed to be even. \n(Press enter to advance...)")
    
    print("We can check this ourselves and see that for any integer k, we will get back an odd result:\n")
    time.sleep(2)
   
    while True:
        print("Enter an integer: ")
        k = input()
        if k.isdigit():
            number_int = int(k)
        
            SumOfNumber = 2*(2*(number_int**2) + 2*number_int)+1
        
            if SumOfNumber %2 == 0:
                input(f"\nf({number_int}) = 2(2*{number_int}\u00b2 + 2*{number_int}) + 1 = {SumOfNumber}, which is even. This should not be possible as we assumed 2k+1 is odd. Ending program.")
                break
            else:
                print(f"\nf({number_int}) = 2(2*{number_int}\u00b2 + 2*{number_int}) + 1 = {SumOfNumber}.\n\nContradiction: a\u00b2 is odd, despite us assuming it should be should be even.")
                time.sleep(1)
                break
        else:
            print("This is not a number.")
    
    time.sleep(1)
    input("\nTherefore, if a\u00b2 is even, then a must be even.\n(Press enter to exit the program...)")
    

prove_some_integers_are_even()
