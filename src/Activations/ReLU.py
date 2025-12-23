def ReLU_activation(preactivation: float) -> float:
    """
    ReLU activation function.

    Parameters
    ----------
    preactivation : float
        The pre-activation value.

    Returns
    -------
    float
        The activated output (same as pre-activation).
    """
    return max(0.0, preactivation)