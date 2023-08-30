import json
import os


def save_jsonl(datas, file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        for data in datas:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

def load_json(in_file):
    with open(in_file, "r", encoding="utf-8") as f:
        datas = [json.loads(line) for line in f]
    return datas

def generate_GPT_test(in_files, out_file):
    new_datas = []
    for in_file in in_files:
        datas = load_json(in_file)

        for data in datas:
            prompt = f"请回答以下问题：{data['question']} 选项A为{data['A']} 选项B为{data['B']} 选项C为{data['C']} 选项D为{data['D']}"
            answer = data["answer"]
            answer_val = data[data["answer"]]
            explanation = "" if "explanation" not in data else data["explanation"]

            new_data = {"text":[{"content":prompt}], "first_text_length":len(prompt), "extra":{"id":data["id"], "answer":answer, "answer_val":answer_val, "explanation":explanation}}
            new_datas.append(new_data)

    save_jsonl(new_datas, out_file)

def generate_Llama_test(in_files, out_file):
    new_datas = []
    for in_file in in_files:
        datas = load_json(in_file)

        for data in datas:
            system = {"role":"system", "content":[{"type":"text", "content":""}]}
            user = {"role":"user", "content":[{"type":"text", "content":f"请回答以下问题：{data['question']} 选项A为{data['A']} 选项B为{data['B']} 选项C为{data['C']} 选项D为{data['D']}"}]}
            answer = data["answer"]
            answer_val = data[data["answer"]]
            explanation = "" if "explanation" not in data else data["explanation"]
            extra = {"id":data["id"], "answer":answer, "answer_val":answer_val, "explanation":explanation}

            new_data = {"messages":[system, user], "extra":extra}
            new_datas.append(new_data)

    save_jsonl(new_datas, out_file)

if __name__ == "__main__":
    # in_files = [
    #     "/mnt/cache/luzimu/datasets_ch/ceval/outs/math_dev_processed/output.jsonl",
    #     "/mnt/cache/luzimu/datasets_ch/ceval/outs/math_val_processed/output.jsonl"
    # ]
    # out_file = "/mnt/cache/luzimu/datasets_ch/ceval/outs/test/gpt_test.jsonl"

    # generate_GPT_test(in_files, out_file)

    in_files = [
        "/mnt/cache/luzimu/datasets_ch/ceval/outs/math_dev_processed/output.jsonl",
        "/mnt/cache/luzimu/datasets_ch/ceval/outs/math_val_processed/output.jsonl"
    ]
    out_file = "/mnt/cache/luzimu/datasets_ch/ceval/outs/test/Llama_test.jsonl"

    generate_Llama_test(in_files, out_file)