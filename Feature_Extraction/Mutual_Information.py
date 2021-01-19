# Date: 2020.10.11 - 2020.10.12
# File function: Get MI value from two Entropy
# Person write this file: Tianhe Wu

import math
import numpy as np
import threading
import time

from Feature_Extraction.Shannon_Entropy import Entropy


class MI:

    # Send two Entropy class
    def __init__(self, X_: Entropy, Y_: Entropy):
        self.X = X_
        self.Y = Y_
        # Define dict about (x, y) -> Pij, tuple -> float
        self.val_xy_p = {}

    # Compute the joint shannon entropy
    def get_joint_entropy(self) -> float:
        print('start compute the joint entropy')
        # Define joint entropy val
        joint_entropy_val = 0

        # Compute f(x, y) = f(x) * f(y)
        for x in self.X.val_set:
            for y in self.Y.val_set:
                p_num = len(np.where(np.in1d(np.where(self.X.data == x)[0], np.where(self.Y.data == y)[0]) == True)[0])
                p_xy = p_num / self.X.len_data
                if (x, y) not in self.val_xy_p and p_xy > 0.0:
                    self.val_xy_p[(x, y)] = p_xy

        # Compute the joint shannon entropy S(X, Y)
        for key in self.val_xy_p:
            joint_entropy_val += self.val_xy_p[key] * math.log(self.val_xy_p[key])

        return -joint_entropy_val if joint_entropy_val != 0.0 else 0.0

    # Create two point connection
    def create_MI_matrix(self, matrix_graph: [list]) -> None:
        # MI(x, y) = S(X) + S(Y) - S(X, Y)
        print('start compute MI')
        MI_val = self.X.get_entropy() + self.Y.get_entropy() - self.get_joint_entropy()
        # MI_val = 0.0 if MI_val <= -0.5e-10 else MI_val
        matrix_graph[self.X.idx][self.Y.idx] = MI_val
        matrix_graph[self.Y.idx][self.X.idx] = MI_val
