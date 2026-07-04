# a Simple Neural Network Project
this project implements a simple neural network 
it consists of:
- **input layer**: takes the feature matrix.
- **hidden layer**: processes features using weights and biases , followed by an activation function.
- **output layer**: produces the final prediction.

## Features
- uses classes and objects for organizing the project.
- the project is written manually to understand mathematical complicated details.
- supposes weight values.
- implements forward propagation to calculate output of hidden layer & final output.
- implements backwark propagation to optimize weight values.
- uses for loop to repeat forward & backward propagation.


## implementation details
- creates inputs and outputs.
- creates class.
- supposes weights.
- definition function for forward propagation and calculates output of hidden layer and final output.
- optimize weight values.


## Result
```
input = [[0 0 1]
 [0 1 1]
 [1 0 1]
 [1 1 1]]

 y = [[0]
 [1]
 [1]
 [0]]

# final predicted output
output =
[[0.07134774]     # Approaches 0
 [0.92663403]     # Approaches 1
 [0.90540792]     # Approaches 1
 [0.09672117]]    # Approaches 0
```


## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Hassan-mahmoud33/neural_network.git
```

2. Navigate to the project directory:

```bash
cd neural_network
```

3. Install the required libraries:
pip install numpy 

4. Run the project:
```bash
python main.py
```
## library used
- numpy


## purpose
this project is for educational purposes.

