from functions import read_picture_file,bin_to_int

def decoding():
    picture_file = input("enter the name of the picture file you want to decode")
    result = read_picture_file(picture_file)
    pixels = result [0]
    picture_width=result[1]
    picture_height=result[2]
    max_colour_intensity = result[3]
    error=result[4]

    if error:
        print(error)
        return
    
    if len(pixels)<32:
        print("there is no hidden message ")
        return

    bit_length = ""

    for i in range(32):
        bit_length += str(pixels[i]%2)

    message_length = bin_to_int(bit_length)
    bits_needed = message_length*8

    if 32+bits_needed>len(pixels):
        print("message is not complete")
        return

    message_bits=""

    for i in range(32,32+bits_needed):
        message_bits += str(pixel[i]%2)

    message = ""

    for i in range(message_length):
        byte_bits = message_bits[i*8 : i*8+8]
        message += chr(bin_to_int(byte_bits))

    print(f"the hidden message is:", {message})



