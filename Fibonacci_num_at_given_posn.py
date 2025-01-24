# F(0) = 0
# F(1) = 1
# F(n) = F( n-1 ) + F( n-2 )  [ for n > 2 ]

def Fibonacci_num(n):
   if ( n == 0 ) : return 0
   elif ( n == 1 ) : return 1
   else: return ( Fibonacci_num( n - 1 ) + Fibonacci_num( n - 2 ) )
   

# Main Function for Fibnacci Num calculation
try: 
   posn = int( input( "Enter the Fibonacci Number Position: "))

except Exception as msg:
   print("Error: ", msg)

else:
   fibonacci_num = Fibonacci_num( posn )

   print(f"Fibonacci Number of {posn}: {fibonacci_num}")
