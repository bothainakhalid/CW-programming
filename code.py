def read_picture_file(picture_file):
    try: 
        file = open(picture_file, "r")
    except:
        return None,None,None,None, "this file does not exist"
    
    values = []

    for line in file:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("#"):
            continue
        if "#" in line:
            line = line.split("#")[0].strip()
        if line == "":
            continue

        separated = line.split()
        for s in separated:
            values.append(s)


