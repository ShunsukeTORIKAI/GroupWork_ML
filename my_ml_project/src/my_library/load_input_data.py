def load(input_path):   #train.txtの情報を要素に持つリストを要素に持つリスト
    sentence_arrays = []
    with open(input_path) as f:
        for line in f:
            if line != "":
                line = line.rstrip("\n")
                if "\t" in line:
                    line_arrays = line.split("\t")
                else:
                    pass
                sentence_arrays.append(line_arrays)
            else:
                pass
    return sentence_arrays

def load_raw_data(input_path):  #data.txtの一文を要素に持つリストを返す
    sentence_arrays = []
    with open(input_path) as f:
        for line in f:
            if line != "":
                line = line.rstrip("\n")
                sentence_arrays.append(line)
            else:
                pass
    return sentence_arrays