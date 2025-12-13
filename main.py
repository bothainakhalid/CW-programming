from encoding import encoding
from decoding import decoding

choice = input("if you want to ENCODE a secret message please enter '1'\n if you would like to DECODE a secret message please enter '2' " )
 
if choice == "1":
    encode()
elif choice == "2":
    decode()
else:
    print("please choose 1 or 2")

