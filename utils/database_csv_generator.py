import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

import csv

class CsvGenerator():
    def __init__(self) -> None:
        self.path_node_list = "data/node_TPmetro.csv.csv"
        self.path_metro_list = "data/all_TPmetro.csv"
        self.path_metro_all_data_output = "data/all_TPmetro_output.csv"

    def nodes_loader(self, path=None):
        if not path: path = self.path_node_list
        code, name = [], []
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                code.append(row[0].split()[0])
                name.append(row[0].split()[1])
        return code, name
    
    def result_saver(self, data_list, path):
        if not path: path = self.path_metro_all_data_output
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_list)

    def result_loader(self, path):
        if not path: path = self.path_metro_all_data_output
        price_matrix = []
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                price_matrix.append(row)
        return price_matrix

    def metro_loader(self, path):
        if not path: path = self.path_metro_list
        data = []
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        return data
    
    def TPmetro_extractor(self, codes, names, ALL_DATA):
        nums = len(ALL_DATA)
        ALL_CSV_DATA = []
        for index_station_code in range(nums):
            for i in range(nums):
                found = False
                each_code_data = [codes[index_station_code]]
                for j in range(nums):
                    if not found:
                        if names[index_station_code] in ALL_DATA[i][j]:
                            found = True
                            each_code_data.append(0)
                            continue
                    each_code_data.append(ALL_DATA[j][i] if found else ALL_DATA[i][j])
                    
                if found:
                    ALL_CSV_DATA.append(each_code_data)
                    break
        codes.insert(0, "codes")
        ALL_CSV_DATA.insert(0, codes)
        return ALL_CSV_DATA

    def train_A_B(self) -> list:
        codes, names = self.nodes_loader(path="data/node_train.csv")
        a_b = []
        for i in range(len(codes)):
            j = i + 1
            while j < len(codes):
                a_b.append([codes[i], codes[j]])
                j += 1
        return(a_b)