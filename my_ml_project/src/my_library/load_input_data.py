def load(input_path):
    sentence_arrays = []
    with open(input_path) as f:
        for line in f:
            if line != "":
                line = line.rstrip("\n")
                if "," in line:
                    line = line.split(",")
                else:
                    pass
                sentence_arrays.append(line)
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