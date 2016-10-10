# -*- coding: utf-8 -*-


#a_factaral = lambda x: (  x == 0  and 1 ) or x * a_factaral( x - 1 )
a_factaral = lambda x: (  x == 0  and 1 )+(x>0 and ((x==0 and 1)+x)*a_factaral(x-1))
#a_factaral = lambda x: ((x>0) and x * a_factaral( x - 1 ))or ( ( x == 0 ) and 1 ) 
print(a_factaral(3))
#from sys import *
#from functools import reduce
#print( 'вычисленный факториал = {}'.format(( lambda z: reduce( lambda x, y: x * y, range( 1, z + 1 ) ) ) ( ( lambda : ( len( argv ) > 1 and int( argv[ 1 ] ) ) or  int( input( "число?: " ) ) )() ) ) )
