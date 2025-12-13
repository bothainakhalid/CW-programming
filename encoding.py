from functions import read_picture_file,save_pic_info, len_to_bits,byte_to_bits

def encoding():
    picture_file = input("enter the name of your picture file")
    result = read_picture_file(picture_file)
    pixels = result[0]
    picture_width = result[1]
    picture_height = result[2]
    max_colour_intensity = result[3]
    error = result [4]
    

