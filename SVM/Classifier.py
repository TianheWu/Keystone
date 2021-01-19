# Date: 2020.10.11
# File function: Train the data with SVM
# Person write this file: Zhengwu Yang, Tianhe Wu

from sklearn.svm import SVC


class SVM_CF:

    def __init__(self, dimension_: int, matrix_: [list]) -> None:
        self.dimension = dimension_
        self.matrix = matrix_
        self.w = 0
        self.b = 0

    # load data
    def load_data_set(self) -> list:

        label_mat = []
        # Numbers represent the dimensions of data
        data_mat = [[] for i in range(self.dimension)]

        for line in self.matrix:
            line_arr = line
            for i in range(self.dimension):
                # Load data to dataMat
                data_mat[i].append(float(line_arr[i]))
            # load label to labelMat
            label_mat.append(float(line_arr[self.dimension]))

        # Define the converted data matrix
        data_mat_re = [[] for i in range(len(data_mat[0]))]

        # Start conversion
        for i in range(len(data_mat[0])):
            for j in range(self.dimension):
                data_mat_re[i].append(data_mat[j][i])

        return data_mat_re, label_mat

    # Train the w and b
    def train(self) -> None:
        # Import the data matrix
        data_mat_, label_mat_ = self.load_data_set()
        # Define SVM classifier
        svm = SVC(kernel='linear', random_state=1, gamma='auto', C=1.0)
        # wTx + b = 0
        svm.fit(data_mat_, label_mat_)
        # The parameter of w
        self.w = svm.coef_
        # The parameter of b
        self.b = svm.intercept_
