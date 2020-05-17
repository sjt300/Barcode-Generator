from Code39Funcs import *

tpn_list = []
tpn_focus = 0
code_dict = initialise_dict()

root = Tk()
root.geometry("800x600")
root.title("Barcode Generator(Code39) 1.0 - -Stephen Turley")
title_frame = Frame(root)
title_frame.pack()
tpn_entry = Entry(title_frame, width=9)
tpn_entry.grid(row=0, column=0)
bar_canvas = Canvas(root)

tpn = Tpn(tpn_entry, tpn_list, tpn_focus, root, bar_canvas, code_dict)

cls_btn = Button(title_frame, text="Clear Screen", command=tpn.clear_screen)
cls_btn.grid(row=0, column=1)
tpn_entry.focus_set()

tpn_entry.bind("<Key>", tpn.key_pressed)

root.mainloop()
