import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from utils.database_csv_generator import CsvGenerator

def main():
    obj = CsvGenerator()
    codes, names = obj.nodes_loader()
    ALL_DATA = obj.metro_loader()
    # process each station code
    obj.result_saver(obj.TPmetro_extractor(codes, names, ALL_DATA))

def TYmetro():
    obj = CsvGenerator()
    codes, names = obj.nodes_loader(path="data/node_TYmetro.csv")
    ALL_DATA = obj.metro_loader(path="data/all_TYmetro.csv")
    # process each station code
    obj.result_saver(obj.TPmetro_extractor(codes, names, ALL_DATA), path="data/all_TYmetro_output.csv")
    
def DHtram():
    obj = CsvGenerator()
    codes, names = obj.nodes_loader(path="data/node_DHtram.csv")
    ALL_DATA = obj.metro_loader(path="data/all_DHtram.csv")
    # process each station code
    obj.result_saver(obj.TPmetro_extractor(codes, names, ALL_DATA), path="data/all_DHtram_output.csv")

def AKtram():
    obj = CsvGenerator()
    codes, names = obj.nodes_loader(path="data/node_AKtram.csv")
    ALL_DATA = obj.metro_loader(path="data/all_AKtram.csv")
    # process each station code
    obj.result_saver(obj.TPmetro_extractor(codes, names, ALL_DATA), path="data/all_AKtram_output.csv")

def train():
    obj = CsvGenerator()
    codes, names = obj.nodes_loader(path="data/node_train.csv")
    ALL_DATA = obj.metro_loader(path="data/all_train.csv")
    # process each station code
    obj.result_saver(obj.TPmetro_extractor(codes, names, ALL_DATA), path="data/all_train_output.csv")         

def train_A_B() -> list:
    obj = CsvGenerator()
    ab_list = obj.train_A_B()
    print(ab_list)

if __name__ == "__main__":
    train()