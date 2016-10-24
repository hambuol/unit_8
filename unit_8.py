# written by Oliver Hamburger
# program incodes and decodes string with a grafical user interface

# imports needed modual for GUI
import tkinter


# string to decode users given string
n = "abcdefghijklmnopqrstuvwxyz"


def encodestr():
    """function gets users string, users key and shifted string. then it encodes the
    given string"""
    string = entry.get()
    key = entrykey.get()
    r = n[key:26] + n[0:key]
    encoded = ""
    for x in string:
        encoded += r[n.index(x)]

    answer.set(encoded)


def decodestr():
    """function gets users string, users key and shifted string. then it encodes the
        given string"""
    string = entry1.get()
    key = key1.get()
    r = n[key:26] + n[0:key]
    decoded = ""
    for x in string:
        decoded += n[r.index(x)]

    answer.set(decoded)

# creates blank window for GUI
root = tkinter.Tk()

# puts a title in the window
root.title("Encode/Decode Strings")

# adds a label saying "string to encode" and grids it
encode = tkinter.Label(root, text="string to encode:")
encode.grid(column=1, row=2)

# creates a entry box for the user to put their string to encode
entry = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable=entry)
entryfield.grid(column=2, row=2)

# adds a label saying "key to encode (0-25)
key = tkinter.Label(root, text="key to encode (0-25):")
key.grid(column=1, row=3)

# creates a entry box for the user to put their key to encode and grids it
entrykey = tkinter.IntVar()
entryfield = tkinter.Entry(root, textvariable=entrykey)
entryfield.grid(column=2, row=3)

# creates button that encodes string via encodestr function
encodebutton = tkinter.Button(root, text="encode", command=encodestr)
encodebutton.grid(column=2, row=4)

# adds label saying "string to decode" and grids it
decode = tkinter.Label(root, text="string to decode:")
decode.grid(column=3, row=2)

# creates a entry box for the user to put their key to decode and grids it
entry1 = tkinter.StringVar()
entryfield = tkinter.Entry(root, textvariable=entry1)
entryfield.grid(column=4, row=2)

# adds label saying "key to decode" and grids it
key = tkinter.Label(root, text="key to decode (0-25):")
key.grid(column=3, row=3)

# creates a entry box for the user to pu their key to decode and grids it
key1 = tkinter.IntVar()
entryfield = tkinter.Entry(root, textvariable=key1)
entryfield.grid(column=4, row=3)

# creates a button that decodes the given string via decodestr
decodebutton = tkinter.Button(root, text="decode", command=decodestr)
decodebutton.grid(column=4, row=4)

# adds label saying "encoded/decoded string"
finallable = tkinter.Label(root, text="encoded/decoded string:")
finallable.grid(column=1, row=5)

# creates label for encoded/decoded string to be displayed on
answer = tkinter.StringVar()
finallabelvalue = tkinter.Label(root, textvariable=answer)
finallabelvalue.grid(column=2, row=5)

# runs the main loop for tkinter
root.mainloop()
