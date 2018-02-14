while True:
    print("Welcome to the 100 game")
    print("Instructions:")
    print("1-Each player should enter a number from 1 to 10")
    print("2-The player who types the last number to reach the number 100 is the winner")
    print("Good luck!")
    sum=0
    while sum <100:
        x=int(input("Player 1 , Please enter your number:"))
        if ( x<1 or x>10):
            print("Incorrect number.")
            continue
        else:    
         sum =sum+x
         print(sum)
         if (sum>=100):
              print("Player one is the winner!")
         else:
           
            y=int(input("Player 2 , Please enter your number:"))
            if( y<1 or y>10):
             print("Incorrect number.")
            else:
             sum=sum+y
             print(sum)
             if (sum>=100):
               print("Player 2 is the winner!")
              
                
            
              
              

    
