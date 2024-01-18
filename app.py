import os
import sys
from flask import Flask, render_template, request, redirect, jsonify, url_for
import sqlite3
from utils.database_tools import DatabaseNeo4j
from flask_cors import CORS


app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
CORS(app, supports_credentials=True, allow_headers=["Content-Type"])

current_dir = os.getcwd()
sys.path.append(current_dir)

def get_db_connection():
    return sqlite3.connect('Tpass.db')

TRANSPORT_KINDS = {'TPmetro':'北捷',
                   'TYmetro':'機捷',
                   'TT_bus':'台北新北公車',
                   'Keelung_bus':'基隆公車',
                   'Taoyuan_bus':'桃園公車',
                   'LongBus':'客運',
                   'DH_tram':'淡海輕軌',
                   'AK_tram':'安坑輕軌',
                   'Train':'台鐵'}
USER_GUEST = 'adult_price' #default 全票

@app.route("/")
def index():
    GUEST_KINDS = ['全票', '敬老優待', '台北兒童', '新北兒童']
    return render_template('index.html', guest_kinds = GUEST_KINDS)

@app.route("/planner", methods=["GET","POST"])
def planner():
    guest_type = request.form.get("guest_type")
    USER_GUEST = guest_type
    return render_template("planner.html", transport_kinds = TRANSPORT_KINDS)


@app.route("/TPmetro_calculation", methods=["POST"])
def TPmetro_calculation():
    """
    Inputs:
        start_station: code of station
        end_station: code of station
        guest_type: adult_price, nt_child_price, tp_child_price, old_price
    """
    # use JSON POST in JS thus not using request.form.get here in route
    data = request.get_json()
    start_station = data.get("startStation")
    end_station = data.get("endStation")
    is_roundtrip = data.get("isRoundtrip")
    guest_type = USER_GUEST

    if start_station == end_station:
        price = 20
    else:
        obj = DatabaseNeo4j(configuration_path="data/configurations.json")
        obj.set_database(database_name="neo4j")
        price = obj.get_TP_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_type)
        if is_roundtrip:
            price = price*2

    return jsonify({'price': price})

@app.route("/TYmetro_calculation", methods=["POST"])
def TYmetro_calculation():
    """
    Inputs:
        start_station: code of station
        end_station: code of station
        guest_tpye: adult_price, child_price, old_price
    """
    data = request.get_json()
    start_station = data.get("startStation")
    end_station = data.get("endStation")
    is_roundtrip = data.get("isRoundtrip")
    guest_type = USER_GUEST

    if guest_type == 'nt_child_price' or 'tp_child_price':
        guest_type = 'child_price'

    if start_station == end_station:
        price = 20

    else:
        obj = DatabaseNeo4j(configuration_path="data/configurations.json")
        obj.set_database(database_name="neo4j")
        price = obj.get_TY_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_type)

        if is_roundtrip:
            price = price * 2

    return jsonify({'price': price})

@app.route("/DHtram_calculation", methods=["POST"])
def DHtram_calculation():
    """
     Inputs:
         start_station: code of station
         end_station: code of station
         guest_type: adult_price, nt_child_price, tp_child_price, old_price
     """
    data = request.get_json()
    start_station = data.get("startStation")
    end_station = data.get("endStation")
    is_roundtrip = data.get("isRoundtrip")
    guest_type = USER_GUEST

    if start_station == end_station:
        price = 20

    else:
        obj = DatabaseNeo4j(configuration_path="data/configurations.json")
        obj.set_database(database_name="neo4j")
        price = obj.get_DH_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_type)

        if is_roundtrip:
            price = price * 2
    return jsonify({'price': price})

@app.route("/AKtram_calculation", methods=["POST"])
def AKtram_calculation():
    """
     Inputs:
         start_station: code of station
         end_station: code of station
         guest_type: adult_price, nt_child_price, tp_child_price, old_price
     """
    data = request.get_json()
    start_station = data.get("startStation")
    end_station = data.get("endStation")
    is_roundtrip = data.get("isRoundtrip")
    guest_type = USER_GUEST

    if start_station == end_station:
        price = 20

    else:
        obj = DatabaseNeo4j(configuration_path="data/configurations.json")
        obj.set_database(database_name="neo4j")
        price = obj.get_AK_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_type)

        if is_roundtrip:
            price = price * 2
    return jsonify({'price': price})

@app.route("/Train_calculation", methods=["POST"])
def Train_calculation():
    """
     Inputs:
         start_station: code of station
         end_station: code of station
         guest_type: adult_price, nt_child_price, tp_child_price, old_price
     """
    data = request.get_json()
    start_station = data.get("startStation")
    end_station = data.get("endStation")
    is_roundtrip = data.get("isRoundtrip")
    guest_type = USER_GUEST

    if start_station == end_station:
        price = 14

    else:
        obj = DatabaseNeo4j(configuration_path="data/configurations.json")
        obj.set_database(database_name="neo4j")
        price = obj.get_train_cost_between_stations(start_station=start_station, end_station=end_station, guest=guest_type)

        if is_roundtrip:
            price = price * 2
    return jsonify({'price': price})

@app.route("/TT_bus_calculation", methods=["POST"])
def TT_bus_calculation():
    data = request.get_json()
    guest_type = data.get("guest_Type")
    sections = data.get("sections")
    is_roundtrip = data.get("isRoundtrip")

    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_TT_bus_cost_between_stations(guest_type, sections, is_roundtrip)
    return jsonify({'price': price})


@app.route("/Keelung_bus_calculation", methods=["POST"])
def Keelung_bus_calculation():
    data = request.get_json()
    guest_type = data.get("guest_Type")
    sections = data.get("sections")
    is_roundtrip = data.get("isRoundtrip")
    keelung_night_mode = data.get("keelung_night_mode")

    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_Keelung_bus_cost_between_stations(guest_type, sections, is_roundtrip, keelung_night_mode)
    return jsonify({'price': price})

@app.route("/TY_bus_calculation", methods=["POST"])
def TY_bus_calculation():
    data = request.get_json()
    guest_type = data.get("guest_Type")
    TYbus_single_trip_cost = data.get("TYbus_single_trip_cost")
    is_roundtrip = data.get("isRoundtrip")
    is_TY_citizen = data.get("is_TY_citizen")

    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_Taoyuan_bus_cost_between_stations(guest_type, TYbus_single_trip_cost, is_roundtrip, is_TY_citizen)
    return jsonify({'price': price})

@app.route("/Long_Bus_calculation", methods=["POST"])
def Long_Bus_calculation():
    data = request.get_json()
    LongBus_single_trio_cost = data.get("LongBus_single_trip_cost")
    is_roundtrip = data.get("isRoundtrip")

    obj = DatabaseNeo4j(configuration_path="data/configurations.json")
    obj.set_database(database_name="neo4j")
    price = obj.get_LongBus_cost_between_stations(LongBus_single_trio_cost, is_roundtrip)
    return jsonify({'price': price})

