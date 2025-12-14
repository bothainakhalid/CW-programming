from functions import read_picture_file,save_pic_info, len_to_bits,byte_to_bits

def encoding():
    picture_file = input("enter the name of your picture file")
    result = read_picture_file(picture_file)
    pixels = result[0]
    picture_width = result[1]
    picture_height = result[2]
    max_colour_intensity = result[3]
    error = result [4]

    if error:
        print(error)
        return

    input_method = input("choose your text input method \n1)type your secret message\n2)import your message using external file")
    if input_method == "1":
        message=input("enter the message you want to hide")
    
    elif input_method == "2":
        message_file = input("enter your message file name")
        try:
            file = open(message_file,"r")
            message = file.read()
            file.close()
        except:
            print("message file doesn't exist")
            return
    
    else:
        print("please choose 1 or 2 ")

    if message == "":
        print("message can't be empty")
        return

    message_bytes=[]

    for m in message:
        message_bytes.append(ord(m))
    
    message_length = len(message_bytes)

    bits_needed = 32 + message_length*8

    if bits_needed>len(pixels):
        print("message is too long")
        return

    bit_length = len_to_bits(message_length)

    message_bits = ""

    for b in message_bytes:
        message_bits+= byte_to_bits(b)

    all_bits = bit_length+message_bits

    pointer_bit = 0

    for i in range(len(pixels)):
        if pointer_bit>=len(all_bits):
            break

        if all_bits[pointer_bit] == "0":
            if pixels[i]%2 == 1:
                pixels[i]-=1
        else:
            if pixels[i]%2==0:
                if pixels[i] == max_colour_intensity:
                    pixels[i]-=1
                else:
                    pixels[i]+=1
        
        pointer_bit+=1

    final_picture = input("enter final modified picture name")

    save_pic_info(final_picture,pixels,picture_width,picture_height,max_colour_intensity)

    print("message has been hidden")

    