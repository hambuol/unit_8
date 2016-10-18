import tkinter

root = tkinter.Tk()

encode_decodelabel = tkinter.Label(root, text = "Encode/Decode")
encode_decodelabel.grid(column = 1, row = 1)

encode = tkinter.Label(root, text = "encode:")
encode.grid(column = 1, row = 2)



root.mainloop()