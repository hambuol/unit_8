import tkinter
n = "abcdefghijklmnopqrstuvwxyz"
def encodestr():
    string = entry.get()
    key = entrykey.get()
    r = n[key:26] + n[0:key]
    encoded = ""
    for x in string:
        encoded += r[n.index(x)]

    answer.set(encoded)


    



def decodestr():
    string = entry1.get()
    key = key1.get()
    r = n[key:26] + n[0:key]
    decoded = ""
    for x in string:
        decoded += n[r.index(x)]

    answer.set(decoded)



root = tkinter.Tk()

encode_decodelabel = tkinter.Label(root, text = "Encode/Decode")
encode_decodelabel.grid(column = 1, row = 1)

encode = tkinter.Label(root, text = "string to encode:")
encode.grid(column = 1, row = 2)


entry = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable = entry)
entryfield.grid(column = 2, row = 2)

key = tkinter.Label(root, text = "key to encode (0-25):")
key.grid(column = 1, row = 3)

entrykey = tkinter.IntVar()
entryfield = tkinter.Entry(root, textvariable = entrykey)
entryfield.grid(column = 2, row = 3)

encodebutton = tkinter.Button(root, text = "encode", command = encodestr)
encodebutton.grid(column = 2, row = 4)

decode = tkinter.Label(root, text = "string to decode:")
decode.grid(column = 3, row = 2)

entry1 = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable = entry1)
entryfield.grid(column = 4, row = 2)

key = tkinter.Label(root, text = "key to decode (0-25):")
key.grid(column = 3, row = 3)


key1 = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable = key1)
entryfield.grid(column = 4, row = 3)

decodebutton = tkinter.Button(root, text = "decode", command = decodestr)
decodebutton.grid(column = 4, row = 4)

finallable = tkinter.Label(root, text = "encoded/decoded string:")
finallable.grid(column = 1, row = 5)

answer = tkinter.StringVar()
finallabelvalue = tkinter.Label(root, textvariable = answer)
finallabelvalue.grid(column = 2, row = 5)


root.mainloop()