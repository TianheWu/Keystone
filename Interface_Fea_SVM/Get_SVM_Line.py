# Date: 2020.10.17
# File function: Transform the matrix to lower triangle and append the label to construct a SVM input line
# Person write this file: Zijian Feng, Tianhe Wu


class Connect:

    # Send mutual information matrix
    def __init__(self, matrix_: [[list]], label_: int) -> None:
        self.matrix = matrix_
        self.label = label_

    # Transform the matrix to lower triangle and append the label
    def get_line(self) -> list:
        print('start get line:')
        vec_ = []
        for z in self.matrix:
            for i in range(1, len(z)):
                for j in range(i):
                    print(self.matrix[z][i][j])
                    vec_.append(self.matrix[z][i][j])
        print('write the label')
        vec_.append(self.label)
        return vec_
