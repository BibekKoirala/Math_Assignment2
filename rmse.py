import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    mse = np.mean((pred - tar)**2)
    print("mse1:\n", mse)
    rmse = np.sqrt(mse) #None # TODO: Implement RMSE Calculation here...
    return rmse