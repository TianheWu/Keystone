# Date: 2020.10.11
# File function: Get the entropy from data
# Person write this file: Tianhe Wu

import math


class Entropy:

    # Send one channel data into class Entropy
    def __init__(self, data_: list, idx_: int) -> None:
        self.idx = idx_
        self.data = data_
        # Define the times of every data appeared
        # val_dict: value -> nums, float -> int
        self.val_n = {}
        # Define the probability of each value, float -> float
        self.val_p = {}
        # Define the set of data
        self.val_set = set(data_)

    # Define len_data
    def set_len(self) -> None:
        self.len_data = len(self.data)

    # Count frequency of each value
    def get_frequency(self) -> None:
        print('start compute the frequency')
        # Count the times for each element
        for i in self.data:
            if i not in self.val_n:
                self.val_n[i] = 1
            else:
                self.val_n[i] += 1

        # Get the probability(p) for each element
        self.set_len()
        for i in self.val_set:
            val_f = self.val_n[i] / self.len_data
            self.val_p[i] = val_f

    # Find the value of entropy
    def get_entropy(self) -> float:
        print('start compute the entropy')
        self.get_frequency()
        entropy_val = 0
        # Get the value of entropy according to the formula of entropy
        # Find S(X)
        for i in self.val_set:
            entropy_val += self.val_p[i] * math.log(self.val_p[i])

        return -entropy_val if entropy_val != 0.0 else 0.0
