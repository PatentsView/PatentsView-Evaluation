import os
# pip install python-dotenv
from dotenv import load_dotenv
from os import listdir
from os.path import isfile, join
import pandas as pd

load_dotenv()

def get_files():
    home_path = os.environ["home_path"]
    assignee_data_path = home_path + "/pv_evaluation" + "/data/assignee/hand-labels"
    assignee_label_list = [f for f in listdir(assignee_data_path) if isfile(join(assignee_data_path, f))]
    return assignee_data_path, assignee_label_list

def consolidate_labels(assignee_data_path, assignee_label_list):
    appended_data = []
    for file in assignee_label_list:
        temp_data = pd.read_csv(assignee_data_path + "/" + file)
        try:
            filtered_temp_data = temp_data[["assignee",'assignee_individual_name_first','assignee_individual_name_last', 'assignee_organization']]
        except:
            filtered_temp_data = temp_data[
                ["assignee", 'assignee_individual_name_first', 'asassignee_individual_name_last',
                 'assignee_organization']]
        mention_id = file.split(".")[0]
        filtered_temp_data["mention_id"] = mention_id
        appended_data.append(filtered_temp_data)
        print(f"added file: {mention_id}")
    final_data = pd.concat(appended_data)
    final_data.to_csv(assignee_data_path + "/consolidated_assignee_samples.csv")


if __name__ == "__main__":
    assignee_data_path, assignee_label_list = get_files()
    consolidate_labels(assignee_data_path, assignee_label_list)

