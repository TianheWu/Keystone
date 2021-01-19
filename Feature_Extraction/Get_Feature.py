# Date: 2020.10.11
# File function: Extract feature
# Person write this file: Tianhe Wu

from Preprocessing.Window_Processing import Window
from Feature_Extraction.Shannon_Entropy import Entropy
from Feature_Extraction.Mutual_Information import MI
import time


class Extraction:

    # No parameter need to send
    def __init__(self) -> None:
        # Define matrix about Mutual Information value
        self.matrix_graph = [[0] * 18 for _ in range(18)]
        # Define a big list contain all matrix_graph
        self.matrix_MI = []

    # Return label
    def get_label(self):
        return self.Window_oj.label

    # Extract feature process
    def extract(self, seconds_: int, minutes_all_: int, label_: int) -> None:

        # Define object of Window
        self.Window_oj = Window(seconds_, minutes_all_, label_)

        # Get all window
        print('start get window')
        w_graph = self.Window_oj.get_window()
        print('End get window')

        # Define debug index
        idx_de = 0

        for w in w_graph:
            # Get one window channel
            window_ch = []

            # Create channel and append into window_ch
            for i in range(len(w)):
                channel = Entropy(w[i], i)
                window_ch.append(channel)

            start = time.time()
            print('start create mutual information matrix ' + str(idx_de))
            idx_de += 1

            # Create Mutual Information matrix
            for j in range(len(window_ch)):
                for z in range(j + 1, len(window_ch)):
                    MI_oj = MI(window_ch[j], window_ch[z])
                    MI_oj.create_MI_matrix(self.matrix_graph)

            self.matrix_MI.append(self.matrix_graph)

            print('append matrix process')
            print(self.matrix_graph)
            self.matrix_graph = [[0] * 18 for _ in range(18)]
            end = time.time()
            print("time spent:" + str(end - start))

