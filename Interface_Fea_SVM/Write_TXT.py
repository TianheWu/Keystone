# Date: 2020.10.17
# File function: Write the input line of SVM into .TXT
# Person write this file: Tianhe Wu

from Feature_Extraction.Get_Feature import Extraction
from Interface_Fea_SVM.Get_SVM_Line import Connect
import time


# Write the input line of SVM into .TXT
def write_file(seconds_: int, minutes_: int, label_: int) -> None:
    Ex_ = Extraction()
    Ex_.extract(seconds_, minutes_, label_)
    Con_ = Connect(Ex_.matrix_MI, label_)
    print('start get line')
    cur_line = Con_.get_line()
    file_write_in = open('D:\wutianhe_document\Keystone_Code\SVM_data.txt', encoding='utf-8')
    for i in cur_line:
        c = str(i) + ' '
        file_write_in.write(c)
    file_write_in.write('\n')


