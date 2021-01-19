# Date: 2020.10.9-2020.10.11
# File function: Split the whole data to the equal length window
# Person write this file: Tianhe Wu


class Window:

    # Send the seconds for one window and the whole time which the unit is minute of the data into class Window
    def __init__(self, seconds_: int, minutes_all_: int, label_: int) -> None:
        self.seconds = seconds_
        self.minute_all = minutes_all_
        self.label = label_

    # Create the every window size
    def create(self) -> None:
        # Define window num
        # self.window_num = 2
        self.window_num = self.seconds * 256
        # Create the window graph
        # self.window_graph = [[] for _ in range(4)]
        all_seconds_ = self.minute_all * 60
        self.window_graph = [[] for _ in range(int(all_seconds_ // self.seconds))]

    # Get the window_graph
    def get_window(self) -> [[list]]:
        self.create()
        # Get the Data file
        file_object = open('D:\wutianhe_document\Keystone_Code\data2.txt', encoding='utf-8')
        # Process the data
        for line in file_object.readlines():
            line = line.strip('\n').split('\t')
            # Deal the idx for every window
            window_pos = 0
            # Second list in window_graph
            idx_plus = 0
            # Create small window list
            cur_list = []

            # Put each window(Two-dimensional matrix) into a big list
            # Each row in window graph means one window
            for i in range(len(line)):
                cur_list.append(line[i])
                window_pos += 1
                if window_pos >= self.window_num:
                    self.window_graph[idx_plus].append(cur_list)
                    idx_plus += 1
                    window_pos = 0
                    cur_list = []

        return self.window_graph

    # Debug fuc: Check the window
    def print_window(self) -> None:
        for i in self.window_graph:
            print(i)