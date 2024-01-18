import os
import sys
current_dir = os.getcwd()
sys.path.append(current_dir)

from selenium.webdriver.common.by import By
from utils.train_parse import TrainParse
from utils.database_csv_generator import CsvGenerator
import time
import csv

def main():
    cg = CsvGenerator()
    codes, names  = cg.nodes_loader(path="data/node_train.csv")
    a_b_list = cg.train_A_B()
    nums = len(codes)
    obj = TrainParse(parse_info_path="data/configurations.json")
    empty_list_of_lists = [[] for _ in range(nums)]
    count, add, code_count, price_index = 0, 0, 0, 0
    try:
        obj.open_train_hpmepage()
        for i in range(int(nums*nums)):
            if count == add:
                empty_list_of_lists[count].append(codes[code_count]+" "+names[code_count])
            elif count > add:
                # set up start
                obj.enter_text(by=By.XPATH, label="/html/body/div[5]/div[3]/form/div[2]/div[2]/div[2]/input", text=a_b_list[price_index][0])
                # set up end
                obj.enter_text(by=By.XPATH, label="/html/body/div[5]/div[3]/form/div[2]/div[3]/div[2]/input", text=a_b_list[price_index][1])
                obj.switch_to_shuttle()
                obj.confirm_search()
                price = obj.find_price()
                empty_list_of_lists[count].append(price)
                price_index += 1
            else:
                empty_list_of_lists[count].append(" ")
            count += 1
            if count == nums:
                add += 1
                count = 0
                code_count += 1
        with open("data/all_train.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(empty_list_of_lists)
    finally:
        obj.close_driver()


if __name__ == "__main__":
    main()