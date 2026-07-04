import numpy as np

def sigmoid (x):
    return 1 / ( 1 + np.exp( - x))


def sigmoid_derivative(x):
    return x * ( 1 - x )



X = np.array( [[0 , 0 , 1],
             [0 , 1 , 1 ], 
             [1 , 0 , 1 ],
             [1 , 1 , 1]]
             )


y = np.array( [[0], 
              [1], 
              [1],
              [0]
              ])


# this network contains input layer = 3
# hidden layer = 4 cells , there is one hidden layer
# output layer = 1 cell

cells_of_hidden = 4

class Neural_network :

    def __init__ ( self , x , y ):

        self.input = x
        self.weights1 = np.random.rand( self.input.shape[1] , cells_of_hidden )
        self.weights2 = np.random.rand( cells_of_hidden , 1 )

        self.y = y 
        self.output = np.zeros(self.y.shape)
        

    def forward_prop( self ):

        self.layer1 = sigmoid( self.input.dot( self.weights1 )) # output of hidden layer
        self.output = sigmoid( np.dot( self.layer1 , self.weights2 )) # final output 


    def back_prop(self):

        b_weights2 = np.dot( self.layer1.T  ,
         ( 2 * ( self.y - self.output) * sigmoid_derivative(self.output)))     
        
        b_weights1 = np.dot( self.input.T ,  
        np.dot( 2 * ( self.y - self.output )  * sigmoid_derivative( self.output ) ,
            self.weights2.T ) * sigmoid_derivative( self.layer1 ) )
        
        self.weights1 += b_weights1
        self.weights2 += b_weights2



nn = Neural_network(X , y)


for i in range(400):
    nn.forward_prop()
    nn.back_prop()

print(f"output = {nn.output}")

