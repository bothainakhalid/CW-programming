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
        picture_width = int(info[1])
        picture_height = int(info[2])
    except:
        return None, None, None,None, "invalid dimensions"

    if picture_width<=0 or picture_height <=0:
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

    return pixels,picture_width, picture_height, max_colour_intensity, None

def save_pic_info(filename,pixels,picture_width,picture_height,max_colour_intensity):
    file = open(filename,"w")
    file.write("P3\n")
    file.write(str(picture_width) +"\n")
    file.write(str(picture_height) + "\n")
    file.write(str(max_colour_intensity)+"\n")

    for v in pixels:
        file.write(str(v) + "")
    
    file.close()

def len_to_bits(n):
    bits = ""
    for i in range(31,-1,-1):
        bits += str((n >> i) &1)
    return bits









    


