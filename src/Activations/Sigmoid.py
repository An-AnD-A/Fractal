import numpy as np

def Sigmoid_activation(preactivation: float) -> float:
    """
    Sigmoid activation function.

    Parameters
    ----------
    preactivation : float
        The pre-activation value.

    Returns
    -------
    float
        The activated output.
    """
    return 1 / (1 + np.exp(-preactivation))