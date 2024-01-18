import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from neo4j import GraphDatabase
import json


class DatabaseNeo4j():
    def __init__(self, configuration_path) -> None:
        with open(configuration_path, 'r') as file:
            configs = json.load(file)
        self.configs = configs["cloud_neo4j_root"]
        self.driver = GraphDatabase.driver(self.configs["NEO4J_URI"],
                                           auth=(self.configs["NEO4J_USERNAME"],
                                                 self.configs["NEO4J_PASSWORD"]))
        self.session = self.driver.session()

    def close(self):
        self.driver.close()

    def set_database(self, database_name):
        self.session = self.driver.session(database=database_name)

    def show_sub_databases(self):
        with self.driver.session() as session:
            databases = session.run("SHOW DATABASES")
            for db in databases:
                print(db["name"])

    def get_TP_cost_between_stations(self, start_station, end_station, guest) -> float:
        query = f"""
        MATCH (a:Station {{code: $start_station}})-[r:CONNECTED]->(b:Station {{code: $end_station}})
        RETURN r.{guest} AS cost
        """
        result = self.session.run(query, start_station=start_station, end_station=end_station)
        return result.single()[0]
    
    def get_TY_cost_between_stations(self, start_station, end_station, guest) -> float:
        query = f"""
        MATCH (a:TYStation {{code: $start_station}})-[r:CONNECTED]->(b:TYStation {{code: $end_station}})
        RETURN r.{guest} AS cost
        """
        result = self.session.run(query, start_station=start_station, end_station=end_station)
        return result.single()[0]
    
    def get_DH_cost_between_stations(self, start_station, end_station, guest) -> float:
        query = f"""
        MATCH (a:DHtram {{code: $start_station}})-[r:CONNECTED]->(b:DHtram {{code: $end_station}})
        RETURN r.{guest} AS cost
        """
        result = self.session.run(query, start_station=start_station, end_station=end_station)
        return result.single()[0]
    
    def get_AK_cost_between_stations(self, start_station, end_station, guest) -> float:
        query = f"""
        MATCH (a:AKtram {{code: $start_station}})-[r:CONNECTED]->(b:AKtram {{code: $end_station}})
        RETURN r.{guest} AS cost
        """
        result = self.session.run(query, start_station=start_station, end_station=end_station)
        return result.single()[0]
    
    def get_train_cost_between_stations(self, start_station, end_station, guest) -> float:
        query = f"""
        MATCH (a:train {{code: $start_station}})-[r:CONNECTED]->(b:train {{code: $end_station}})
        RETURN r.{guest} AS cost
        """
        result = self.session.run(query, start_station=start_station, end_station=end_station)
        return result.single()[0]

    def get_TT_bus_cost_between_stations(self, guest_type, sections, is_roundtrip) -> float:
        price_table_Taipei_New_Taipei = [15, 12, 8]
        price = float(price_table_Taipei_New_Taipei[int(guest_type)] * int(sections))
        price = price * 2 if is_roundtrip else price
        return price

    def get_Keelung_bus_cost_between_stations(self, guest_type, sections, is_roundtrip, keelung_night_mode) -> float:
        price_table_keelung_day = [15, 9, 8]
        price_table_keelung_night = [18, 11, 10]
        if keelung_night_mode:
            price = float(price_table_keelung_night[int(guest_type)] * int(sections))
            price = price * 2 if is_roundtrip else price
        else:
            price = float(price_table_keelung_day[int(guest_type)] * int(sections))
            price = price * 2 if is_roundtrip else price
        return price

    def get_Taoyuan_bus_cost_between_stations(self, guest_type, TYbus_single_trip_cost, is_roundtrip, is_TY_citizen) -> float:
        price_table_taoyuan = [18, 9]
        # guest_type judged by the global variable in the app.py
        # it's stored as the user has selected in the first landing page
        # the TY
        if is_TY_citizen:
            price = float(TYbus_single_trip_cost) * 2 if is_roundtrip else float(TYbus_single_trip_cost)
            price = price - price_table_taoyuan[int(guest_type)]
        else:
            price = float(TYbus_single_trip_cost) * 2 if is_roundtrip else float(TYbus_single_trip_cost)
        return price

    def get_LongBus_cost_between_stations(self, LongBus_single_trip_cost, is_roundtrip) -> float:
        price = float(LongBus_single_trip_cost) * 2 if is_roundtrip else float(LongBus_single_trip_cost)
        return price

    def add_station_node(self, node_label, node_properties):
        query = f"CREATE (n:{node_label} {{ {node_properties} }}) RETURN n"
        result = self.session.run(query)
        return result.single()[0]

    def delete_all_nodes_and_relationships(self):
        confirm = input("Please enter confirm to delete all nodes: ")
        if confirm == "confirm":
            self.session.run("MATCH (n) DETACH DELETE n")
        else:
            return
        
    def create_price_relationships(self, price_list):
        # list -> dict
        headers = price_list[0][1:]
        price_matrix = {}
        for row in price_list[1:]:
            station = row[0]
            prices = row[1:]
            price_matrix[station] = {headers[i]: prices[i] for i in range(len(headers))}

        for start_station, destinations in price_matrix.items():
            for end_station, price in destinations.items():
                if start_station != end_station:
                    price = float(price)
                    nt_child_price = price * float(self.configs["NT_CHILD_RATIO"])
                    tp_child_price = price * float(self.configs["TP_CHILD_RATIO"])
                    old_price = price * float(self.configs["OLD_RATIO"])
                    query = f"""
                    MATCH (a:Station {{code: $start_station}}), (b:Station {{code: $end_station}})
                    MERGE (a)-[r:CONNECTED]->(b)
                    SET r.adult_price = {price}, 
                        r.nt_child_price = {nt_child_price}, 
                        r.tp_child_price = {tp_child_price}, 
                        r.old_price = {old_price}
                    """
                    self.session.run(query, start_station=start_station, end_station=end_station)
            print(f"Set up {start_station}")
        
    def create_TY_price_relationships(self, price_list):
        # list -> dict
        headers = price_list[0][1:]
        price_matrix = {}
        for row in price_list[1:]:
            station = row[0]
            prices = row[1:]
            price_matrix[station] = {headers[i]: prices[i] for i in range(len(headers))}

        for start_station, destinations in price_matrix.items():
            for end_station, price in destinations.items():
                if start_station != end_station:
                    price = float(price)
                    child_price = price * float(self.configs["TY_CHILD_RATIO"])
                    old_price = price * float(self.configs["TY_OLD_RATIO"])
                    query = f"""
                    MATCH (a:TYStation {{code: $start_station}}), (b:TYStation {{code: $end_station}})
                    MERGE (a)-[r:CONNECTED]->(b)
                    SET r.adult_price = {price}, 
                        r.child_price = {child_price},
                        r.old_price = {old_price}
                    """
                    self.session.run(query, start_station=start_station, end_station=end_station)
            print(f"Set up {start_station}")

    def DHcreate_tram_price_relationships(self, price_list):
            # list -> dict
            headers = price_list[0][1:]
            price_matrix = {}
            for row in price_list[1:]:
                station = row[0]
                prices = row[1:]
                price_matrix[station] = {headers[i]: prices[i] for i in range(len(headers))}

            for start_station, destinations in price_matrix.items():
                for end_station, price in destinations.items():
                    if start_station != end_station:
                        price = float(price)
                        nt_child_price = price * 0.4
                        tp_child_price = price * 0.6
                        old_price = price * 0.4
                        query = f"""
                        MATCH (a:DHtram {{code: $start_station}}), (b:DHtram {{code: $end_station}})
                        MERGE (a)-[r:CONNECTED]->(b)
                        SET r.adult_price = {price}, 
                            r.nt_child_price = {nt_child_price},
                            r.tp_child_price = {tp_child_price},
                            r.old_price = {old_price}
                        """
                        self.session.run(query, start_station=start_station, end_station=end_station)
                print(f"Set up {start_station}")
    
    def AKcreate_tram_price_relationships(self, price_list):
            # list -> dict
            headers = price_list[0][1:]
            price_matrix = {}
            for row in price_list[1:]:
                station = row[0]
                prices = row[1:]
                price_matrix[station] = {headers[i]: prices[i] for i in range(len(headers))}

            for start_station, destinations in price_matrix.items():
                for end_station, price in destinations.items():
                    if start_station != end_station:
                        price = float(price)
                        nt_child_price = price * 0.4
                        tp_child_price = price * 0.6
                        old_price = price * 0.4
                        query = f"""
                        MATCH (a:AKtram {{code: $start_station}}), (b:AKtram {{code: $end_station}})
                        MERGE (a)-[r:CONNECTED]->(b)
                        SET r.adult_price = {price}, 
                            r.nt_child_price = {nt_child_price},
                            r.tp_child_price = {tp_child_price},
                            r.old_price = {old_price}
                        """
                        self.session.run(query, start_station=start_station, end_station=end_station)
                print(f"Set up {start_station}")

    def train_price_relationships(self, price_list):
            # list -> dict
            headers = price_list[0][1:]
            price_matrix = {}
            for row in price_list[1:]:
                station = row[0]
                prices = row[1:]
                price_matrix[station] = {headers[i]: prices[i] for i in range(len(headers))}

            for start_station, destinations in price_matrix.items():
                for end_station, price in destinations.items():
                    if start_station != end_station:
                        price = float(price)
                        query = f"""
                        MATCH (a:train {{code: $start_station}}), (b:train {{code: $end_station}})
                        MERGE (a)-[r:CONNECTED]->(b)
                        SET r.adult_price = {price}
                        """
                        self.session.run(query, start_station=start_station, end_station=end_station)
                print(f"Set up {start_station}")

    def get_stations(self, n=25):
        query = f"""
        MATCH (n:Station) RETURN n LIMIT {n};
        """
        result = self.session.run(query)
        for i in result:
            print(i)

    def get_stations_and_relationships(self):
        query = """
        MATCH (a:Station)-[r:CONNECTED]->(b:Station)
        RETURN a.code AS station1, a.name AS title1, b.code AS station2, b.name AS title2, r.adult_cost AS Acost, r.child_cost AS Ccost
        """
        result = self.session.run(query)
        return [(record["station1"], record["title1"], record["station2"], record["title2"], record["Acost"], record["Ccost"]) for record in result]
    
    def print_stations_and_relationships(self):
        stations = self.get_stations_and_relationships()
        for station in stations:
            print(station)

    
    