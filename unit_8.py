import tkinter
def encodestr():
    print("sup")


def decodestr():
    print("dude")


root = tkinter.Tk()

encode_decodelabel = tkinter.Label(root, text = "Encode/Decode")
encode_decodelabel.grid(column = 1, row = 1)

encode = tkinter.Label(root, text = "string to encode:")
encode.grid(column = 1, row = 2)


string = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable = string)
entryfield.grid(column = 2, row = 2)

key = tkinter.Label(root, text = "key to encode (0-25):")
key.grid(column = 1, row = 3)

key = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable = key)
entryfield.grid(column = 2, row = 3)

encodebutton = tkinter.Button(root, text = "encode", command = encodestr)
encodebutton.grid(column = 2, row = 4)

decode = tkinter.Label(root, text = "string to encode:")
decode.grid(column = 3, row = 2)

string = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable = string)
entryfield.grid(column = 4, row = 2)

key = tkinter.Label(root, text = "key to encode (0-25):")
key.grid(column = 3, row = 3)


key = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable = key)
entryfield.grid(column = 4, row = 3)

decodebutton = tkinter.Button(root, text = "decode", command = decodestr)
decodebutton.grid(column = 4, row = 4)




root.mainloop()