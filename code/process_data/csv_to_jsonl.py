import os
import pandas as pd
import json

def csv_to_jsonl(in_path, file_names, out_path):
    datas = []
    for file_name in file_names:
        test_df = pd.read_csv(os.path.join(in_path, file_name))

        # Loop through each row in the DataFrame
        for index, row in test_df.iterrows():
            data_dict = {}
            for col in test_df.columns:
                data_dict[col] = row[col]
            data_dict["id"] = f"{file_name}/{index}"
            
            datas.append(data_dict)

    if not os.path.exists(out_path):
        os.makedirs(out_path)

    # Writing the list of dictionaries to a JSONL file
    with open(os.path.join(out_path, 'output.jsonl'), 'w') as f:
        for data in datas:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')

if __name__ == "__main__":

    in_path = '/mnt/cache/luzimu/datasets_ch/C-Eval/dev'
    file_names = ['advanced_mathematics_dev.csv', 'high_school_mathematics_dev.csv', 'middle_school_mathematics_dev.csv']
    out_path = '/mnt/cache/luzimu/datasets_ch/ceval/outs/math_dev_processed'

    csv_to_jsonl(in_path, file_names, out_path)

    in_path = '/mnt/cache/luzimu/datasets_ch/C-Eval/val'
    file_names = ['advanced_mathematics_val.csv', 'high_school_mathematics_val.csv', 'middle_school_mathematics_val.csv']
    out_path = '/mnt/cache/luzimu/datasets_ch/ceval/outs/math_val_processed'

    csv_to_jsonl(in_path, file_names, out_path)
