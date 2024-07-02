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