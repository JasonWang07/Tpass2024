import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from utils.database_tools import DatabaseNeo4j
from utils.database_csv_generator import CsvGenerator

def demo():
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    # print("__________Print all sub databases.__________")
    # obj.show_sub_databases()
    obj.set_database(database_name="neo4j")
    # print("__________Print all nodes in test databases.__________")
    # obj.get_stations()
    print("__________Print target cost.__________")
    print(obj.get_cost_between_stations(start_station="R27", end_station="BR01", guest="adult_price"))
    obj.close()

def nodes_creater():
    cg = CsvGenerator()
    codes, names = cg.nodes_loader()
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    for i in range(len(codes)):
        node_label = "Station"
        node_properties = f"code: '{codes[i]}', name: '{names[i]}'"
        obj.add_station_node(node_label, node_properties)

def relations_creater():
    cg = CsvGenerator()
    price_matrix = cg.result_loader()
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    obj.create_price_relationships(price_matrix)

def TY_nodes_creater():
    cg = CsvGenerator()
    codes, names = cg.nodes_loader(path="data/node_TYmetro.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    for i in range(len(codes)):
        node_label = "TYStation"
        node_properties = f"code: '{codes[i]}', name: '{names[i]}'"
        obj.add_station_node(node_label, node_properties)

def TY_relations_creater():
    cg = CsvGenerator()
    price_matrix = cg.result_loader(path="data/all_TYmetro_output.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    obj.create_TY_price_relationships(price_matrix)

def DHtram_nodes_creater():
    cg = CsvGenerator()
    codes, names = cg.nodes_loader(path="data/node_DHtram.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    for i in range(len(codes)):
        node_label = "DHtram"
        node_properties = f"code: '{codes[i]}', name: '{names[i]}'"
        obj.add_station_node(node_label, node_properties)

def AKtram_nodes_creater():
    cg = CsvGenerator()
    codes, names = cg.nodes_loader(path="data/node_AKtram.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    for i in range(len(codes)):
        node_label = "AKtram"
        node_properties = f"code: '{codes[i]}', name: '{names[i]}'"
        obj.add_station_node(node_label, node_properties)

def DHtram_relations_creater():
    cg = CsvGenerator()
    price_matrix = cg.result_loader(path="data/all_DHtram_output.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    obj.DHcreate_tram_price_relationships(price_matrix)

def AKtram_relations_creater():
    cg = CsvGenerator()
    price_matrix = cg.result_loader(path="data/all_AKtram_output.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    obj.AKcreate_tram_price_relationships(price_matrix)

def train_nodes_creater():
    cg = CsvGenerator()
    codes, names = cg.nodes_loader(path="data/node_train.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    for i in range(len(codes)):
        node_label = "train"
        node_properties = f"code: '{codes[i]}', name: '{names[i]}'"
        obj.add_station_node(node_label, node_properties)

def train_relations_creater():
    cg = CsvGenerator()
    price_matrix = cg.result_loader(path="data/all_train_output.csv")
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    obj.train_price_relationships(price_matrix)

if __name__ == "__main__":
    train_relations_creater()