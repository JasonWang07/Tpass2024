import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from utils.database_tools import DatabaseNeo4j


def demoTPmetro(start_station:str="R27", end_station:str="BR03", guest_tpye:str="adult_price") -> None:
    """
    Inputs:
        start_station: code of station
        end_station: code of station
        guest_tpye: adult_price, nt_child_price, tp_child_price, old_price
    """
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_TP_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_tpye)
    print(f"For {guest_tpye} in TPmetro from {start_station} to {end_station} this cost is {price}.")
    obj.close()

def demoTYmetro(start_station:str="A1", end_station:str="A13", guest_tpye:str="adult_price") -> None:
    """
    Inputs:
        start_station: code of station
        end_station: code of station
        guest_tpye: adult_price, child_price, old_price
    """
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_TY_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_tpye)
    print(f"For {guest_tpye} in TYmetro from {start_station} to {end_station} this cost is {price}.")
    obj.close()

def demoDHtram(start_station:str="V09", end_station:str="V28", guest_tpye:str="adult_price") -> None:
    """
    Inputs:
        start_station: code of station
        end_station: code of station
        guest_tpye: adult_price, nt_child_price, tp_child_price, old_price
    """
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_DH_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_tpye)
    print(f"For {guest_tpye} in TYmetro from {start_station} to {end_station} this cost is {price}.")
    obj.close()

def demoAKtram(start_station:str="K01", end_station:str="K09", guest_tpye:str="adult_price") -> None:
    """
    Inputs:
        start_station: code of station
        end_station: code of station
        guest_tpye: adult_price, nt_child_price, tp_child_price, old_price
    """
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_AK_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_tpye)
    print(f"For {guest_tpye} in TYmetro from {start_station} to {end_station} this cost is {price}.")
    obj.close()

def demoTrain(start_station:str="900", end_station:str="1010", guest_tpye:str="adult_price") -> None:
    """
    Inputs:
        start_station: code of station
        end_station: code of station
        guest_tpye: adult_price, nt_child_price, tp_child_price, old_price
    """
    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_train_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_tpye)
    print(f"For {guest_tpye} in train from {start_station} to {end_station} this cost is {price}.")
    obj.close()

if __name__ == "__main__":
    demoTPmetro()
    demoTYmetro()
    demoDHtram()
    demoAKtram()
    demoTrain()