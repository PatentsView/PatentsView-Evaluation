import os
# pip install python-dotenv
from dotenv import load_dotenv
from os import listdir
from os.path import isfile, join
import pandas as pd
import uuid
pd.options.mode.chained_assignment = None


load_dotenv()

def get_files():
    home_path = os.environ["home_path"]
    assignee_data_path = home_path + "/pv_evaluation" + "/data/assignee"
    assignee_label_list = [f for f in listdir(assignee_data_path + "/hand-labels") if isfile(join(assignee_data_path + "/hand-labels", f)) and ".csv" in f and "consolidated" not in f]
    return assignee_data_path, assignee_label_list

def consolidate_labels(assignee_data_path, assignee_label_list):
    appended_data = []
    for file in assignee_label_list:
        temp_data = pd.read_csv(assignee_data_path + "/hand-labels/" + file)
        rename = [i for i in temp_data.columns if "asass" in i]
        name_replace = rename[0].replace("asass", "ass")
        temp_data = temp_data.rename(columns={rename[0]: name_replace})
        # filtered_temp_data = temp_data[["assignee", 'assignee_individual_name_first', 'assignee_individual_name_last', 'assignee_organization']]
        temp_data = temp_data.dropna(how='all')
        temp_data["mention_id"] = "US" + temp_data.patent_id.astype(str) + "-" + temp_data.assignee_sequence.astype(str)
        temp_data["unique_id"] = str(uuid.uuid4())
        test_for_blank_rows(temp_data, "assignee")
        filtered_temp_data = temp_data[['unique_id', 'mention_id']]
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
    print(final_data)
    final_data.to_csv(assignee_data_path + "/consolidated_assignee_samples.csv")

def test_for_blank_rows(df, field_to_test):
    nulls = df[df[field_to_test].isna() == True]
    if not nulls.empty:
        Exception("Review File for NA")

def eval_consolidated(assignee_data_path):
    df = pd.read_csv(assignee_data_path + "/consolidated_assignee_samples.csv")
    df[df["assignee_individual_name_last"].isna()]

# QUESTIONS
# what to do with duplicate files?
# did we filter to organizations and exclude assignees that were individuals? Check this
# how did we time bound the random sample - does it make sense to pull performance metrics on the last few quarters? Check this
# Do we have an example of where we connect to s3 programmatically? [pv-utilities]

if __name__ == "__main__":
    assignee_data_path, assignee_label_list = get_files()
    consolidate_labels(assignee_data_path, assignee_label_list)
    # eval_consolidated(assignee_data_path)


