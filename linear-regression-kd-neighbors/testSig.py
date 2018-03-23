from numpy import 
import ma tpl o t l ib . pyplot as p l t
#Sigmoid func t i on
de f s igmoid ( x ) :
y = 1/(1+exp(􀀀x ) )
r e turn y
#Dimensions
D = 2
N = 10
#Create random samples .
#Clas s 0 c o n t i a i n s 5 samples randomly d i s t r i b u t e d over the l o c a t i o n ( 0 . 5 , 0 . 5 )
#Clas s 1 c o n t i a i n s 5 samples randomly d i s t r i b u t e d over the l o c a t i o n ( 2 . 5 , 2 . 5 )
X =random. rand (D,N)
X[ : , 5 : 1 0 ] = X[ : , 5 : 1 0 ] + 2 ones ( (D, 5 ) )
#Add the row o f bi a s va lue s
X = concat enat e ( (X, ones ( ( 1 ,N) ) ) , a x i s=0)
D = 3
#Create the ve c t o r o f output l a b e l s
c = ar ray ( [ [ 0 . 0 ] , [ 0 . 0 ] , [ 0 . 0 ] , [ 0 . 0 ] , [ 0 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] , [ 1 . 0 ] ] )
#I n i t i a l i s e we ight s to random va lue s
w = random. rand (D, 1 )
w = z e r o s ( (D, 1 ) )
#Set the l e a r n i n g r a t e
e ta = 0 . 2
pr int ( ' nnX=' )
pr int (X)
7
pr int ( ' nnc=' )
pr int ( c )
pr int ( ' nnw=' )
pr int (w)
pr int ( ' n neta=' )
pr int ( e ta )
#I n i t i a l i s e the pl o t
p l t . c l o s e ( ' a l l ' )
p l t . f i g u r e ( )
#Number o f algor i thm i t e r a t i o n s
numI ters = 100
#I n i t i a l i s e the memory f o r the e r r o r .
endI t e r = i t e r a t i o n s
J = z e r o s ( ( numIters , 1 ) )
#Gradient de s c ent loop
f o r i t e r a t i o n in range ( 0 , numI ters ) :
#Compute the output o f the l o g i s t i c r e g r e s s i o n func t i on
o = s igmoid ( dot (X.T,w) )
#Compute the e r r o r
J [ i t e r a t i o n ] = 0.5 dot ( t r anspo s e ( c􀀀o ) , ( c􀀀o ) )
#Compute the weight updates
dw = dot (X, ( c 􀀀 s igmoid ( dot (X.T,w) ) ) )
#Update the we ight s
w = w + e ta dw
#Pr int out the r e s u l t s
pr int ( ' nnnnITERATION %i nn ' % i t e r a t i o n )
pr int ( ' nnoutput=' )
pr int ( o )
pr int ( ' nnJ=' )
pr int ( J [ i t e r a t i o n ] )
pr int ( ' nndw=' )
pr int (dw)
pr int ( ' nnw=' )
pr int (w)
#Plot the r e s u l t s
p l t . c l a ( )
p l t . pl o t (X[ 0 , 0 : 5 ] , X[ 1 , 0 : 5 ] , 'b ' )
p l t . pl o t (X[ 0 , 5 : 1 0 ] , X[ 1 , 5 : 1 0 ] , ' ro ' )
x0 = [ 0 , 3 ]
x1 = (􀀀w[ 0 ]  x0 􀀀 w[ 2 ] ) / (w[ 1 ] )
p l t . pl o t ( x0 , x1 )
p l t . pause ( 0 . 1 )
p l t . draw ( )
#Terminating c ondi t i on
i f ( i t e r a t i o n > 0 ) :
i f ( abs ( J [ i t e r a t i o n ] 􀀀 J [ i t e r a t i o n 􀀀1]) < 0 . 0 0 1 ) :
endI t e r = i t e r a t i o n
pr int ( ' n nTerminating nn ' )
break ;
#Plot the e r r o r
p l t . f i g u r e ( )
p l t . pl o t ( J [ 0 : endI t e r ] )