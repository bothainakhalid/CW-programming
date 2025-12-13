def read_picture_file(picture_file):
    try: 
        file = open(picture_file, "r")
    except:
        return None,None,None,None, "this file does not exist"
    
    info = []

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
            info.append(s)

    file.close()

    if len(info)<4:
        return None,None,None,None, "header is incomplete"

    if info[0] != "P3":
        return "your picture should be in P3 PPM format"

    try:
        width = int(info[1])
        height = int(info[2])
    except:
        return None, None, None,None, "invalid dimensions"

    if width<=0 or height <=0:
        return None,None,None,None, "invalid dimensions"

    try:
        max_colour_intensity = int(info[3])
    except:
        return None,None,None,None, "invalid maximum colour intensity"

    pixel_values = info[4:]
    pixels = []

    for v in pixel_values:
        if v.isdigit():
            pixels.append(int(v))

    if len(pixels) % 3 != 0:
        return None,None,None,None, "pixel values are incomplete"





    


