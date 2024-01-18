import os
# pip install python-dotenv
from dotenv import load_dotenv
from os import listdir
from os.path import isfile, join
import pandas as pd
import uuid
pd.options.mode.chained_assignment = None
import cProfile
import json
import matplotlib
import matplotlib.pyplot as plt

load_dotenv()
matplotlib.use('TkAgg')

def get_files():
    home_path = os.environ["home_path"]
    assignee_data_path = home_path + "/pv_evaluation" + "/data/assignee"
    assignee_label_list = [f for f in listdir(assignee_data_path + "/hand-labels") if isfile(join(assignee_data_path + "/hand-labels", f)) and ".csv" in f and "consolidated" not in f]
    return assignee_data_path, assignee_label_list

def export_mention_id_data(assignee_label_list):
    # repeat_df = pd.DataFrame(columns=["mention_id", "file1", "file2"])
    mention_dict = {}
    for file in assignee_label_list:
        temp_data = pd.read_csv(assignee_data_path + "/hand-labels/" + file)
        rename = [i for i in temp_data.columns if "asass" in i]
        name_replace = rename[0].replace("asass", "ass")
        temp_data = temp_data.rename(columns={rename[0]: name_replace})
        temp_data["mention_id"] = "US" + temp_data.patent_id.astype(str) + "-" + temp_data.assignee_sequence.astype(str)
        rows, columns = temp_data.shape
        mentions = list(temp_data['mention_id'])
        for j in mentions:
            mention_exists = j in mention_dict
            if mention_exists:
                mention_dict[j].update({"file2": file, "file2_rows": rows})
            else:
                mention_dict[j] = {"file1": file, "file1_rows": rows}

        # print(f"finished processing file {file}")
    with open("mention_id.json", 'w') as json_file:
        json.dump(mention_dict, json_file)

def analyze_samples(mention_json):
    with open(mention_json, 'r') as json_file:
        data = json.load(json_file)
    df = pd.DataFrame.from_dict(data, orient='index')
    dupl_df = df[df["file2"].notna()]
    dupl_df.to_csv("dupl_df.csv")
    breakpoint()


def consolidate_labels(assignee_data_path, assignee_label_list):
    appended_data = []
    for file in assignee_label_list:
        temp_data = pd.read_csv(assignee_data_path + "/hand-labels/" + file)
        rename = [i for i in temp_data.columns if "asass" in i]
        name_replace = rename[0].replace("asass", "ass")
        temp_data = temp_data.rename(columns={rename[0]: name_replace})
        temp_data = temp_data.dropna(how='all')
        temp_data["mention_id"] = "US" + temp_data.patent_id.astype(str) + "-" + temp_data.assignee_sequence.astype(str)
        temp_data["unique_id"] = str(uuid.uuid4())
        temp_data["file"] = file
        test_for_blank_rows(temp_data, "unique_id")
        filtered_temp_data = temp_data[['unique_id', 'mention_id', 'file']]
        # filtered_temp_data = temp_data[['unique_id', 'mention_id']]
        appended_data.append(filtered_temp_data)
        print(f"added file: {file}")
    final_data = pd.concat(appended_data)
    print("DATA SHAPE ---------------------------------------------------------------------------")
    print(final_data.shape)
    print("--------------------------------------------------------------------------------------")
    final_data = final_data.drop_duplicates()
    print("DATA SHAPE AFTER DEDEUP --------------------------------------------------------------")
    print(final_data.shape)
    print("--------------------------------------------------------------------------------------")
    breakpoint()
    # REMOVE CANDIDATES FOR RELABELING FOR NOW
    rem = ['US4059131-0.csv',	'US7100827-0.csv',	'US7507211-0.csv',	'US8909968-0.csv',	'US8975348-0.csv',	'US9377726-0.csv',	'US9761552-0.csv',	'USD403363-0.csv',	'USD542763-0.csv',	'USD594508-0.csv',	'US7997327-0.csv',	'US4784030-0.csv',	'US4614515-0.csv',	'USD700602-0.csv',	'US6097140-0.csv',	'US9242814-0.csv',	'US9293014-0.csv',	'US8008251-0.csv',	'US11338586-0.csv']
    df = final_data[~final_data['file'].isin(rem)]
    df = df[['unique_id', 'mention_id']]
    df.to_csv(assignee_data_path + "/consolidated_assignee_samples.csv")
    #### QUALITY CHECKS IN TERMINAL
    # grouped_data = final_data.groupby('mention_id').count().sort_values(by="unique_id", ascending=False)

def test_for_blank_rows(df, field_to_test):
    nulls = df[df[field_to_test].isna() == True]
    if not nulls.empty:
        Exception("Review File for NA")

def eval_consolidated(assignee_data_path):
    df = pd.read_csv(assignee_data_path + "/consolidated_assignee_samples.csv")
    df[df["assignee_individual_name_last"].isna()]

def build_histogram_cluster_size(assignee_data_path, assignee_label_list):
    hist_df = []
    for file in assignee_label_list:
        data = pd.read_csv(assignee_data_path + "/hand-labels/" + file)
        r, c = data.shape
        hist_df.append([file, r])
    # REMOVE CANDIDATES FOR RELABELING FOR NOW
    rem = ['US4059131-0.csv',	'US7100827-0.csv',	'US7507211-0.csv',	'US8909968-0.csv',	'US8975348-0.csv',	'US9377726-0.csv',	'US9761552-0.csv',	'USD403363-0.csv',	'USD542763-0.csv',	'USD594508-0.csv',	'US7997327-0.csv',	'US4784030-0.csv',	'US4614515-0.csv',	'USD700602-0.csv',	'US6097140-0.csv',	'US9242814-0.csv',	'US9293014-0.csv',	'US8008251-0.csv',	'US11338586-0.csv']
    df = pd.DataFrame(hist_df, columns=['file', 'rows'])
    df = df[~df['file'].isin(rem)]
    print(df.shape)
    record_count = list(df["rows"])
    plt.hist(record_count, bins=range(min(record_count), max(record_count) + 1), edgecolor='blue')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Assignee Cluster Size Histogram')
    plt.show()
    breakpoint()



# QUESTIONS
# what to do with duplicate files?
# did we filter to organizations and exclude assignees that were individuals? Check this
# how did we time bound the random sample - does it make sense to pull performance metrics on the last few quarters? Check this
# Do we have an example of where we connect to s3 programmatically? [pv-utilities]

if __name__ == "__main__":
    assignee_data_path, assignee_label_list = get_files()
    # export_mention_id_data(assignee_label_list)
    # analyze_samples("mention_id.json")
    # cProfile.run("analyze_samples(assignee_label_list)")
    # build_histogram_cluster_size(assignee_data_path, assignee_label_list)
    consolidate_labels(assignee_data_path, assignee_label_list)
    # eval_consolidated(assignee_data_path)


