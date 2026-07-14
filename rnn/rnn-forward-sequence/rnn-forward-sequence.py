import numpy as np

def rnn_forward(X: np.ndarray, h_0: np.ndarray,
                W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> tuple:

    hidden_states = []
    h_final = []

    for i in range(X.shape[0]):

        h = h_0[i].copy()
        batch_hidden = []

        for j in range(X.shape[1]):

            h = np.tanh(
                np.dot(X[i][j], W_xh.T)
                + np.dot(h, W_hh.T)
                + b_h
            )

            batch_hidden.append(h.copy())

        hidden_states.append(batch_hidden)
        h_final.append(h.copy())

    return np.array(hidden_states), np.array(h_final)