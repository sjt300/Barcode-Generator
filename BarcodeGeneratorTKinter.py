from tkinter import *
char_list = [(0, 0, 1, 1, 0), (1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (1, 1, 0, 0, 0,), (0, 0, 1, 0, 1), (1, 0, 1, 0, 0), (0, 1, 1, 0, 0), (0, 0, 0, 1, 1), (1, 0, 0, 1, 0), (0, 1, 0, 1, 0), (0, 0), (1, 0)]
tpn_quant = -1
tpn_focus = 0
tpn_list = []
blackout_coords = []

root = Tk()
root.title("Barcode Generator 1.0 - Stephen Turley - April 2020")
root.geometry("800x600")
main_frame = Frame(root)
main_frame.pack()

bar_entry = Entry(main_frame, width=9)
bar_entry.grid(column=0, row=0)
bar_entry.focus_set()

barcode_canvas = Canvas()


def reset_canvas():
    global barcode_canvas
    barcode_canvas.destroy()
    barcode_canvas = Canvas(main_frame, height=550, width=800)
    barcode_canvas.grid(column=0, row=3)


reset_canvas()
clear_screen_btn = Button(main_frame, text='Clear Screen', command=reset_canvas)
clear_screen_btn.grid(column=0, row=1)

for i in range(0, 10):
    blackout_coords.append([20, 10 + 50 * i])
for i in range(0, 10):
    blackout_coords.append([400, 10 + 50 * i])


# create barcode @ focus, create blackout@rest
def generate(quant, focus):
    global blackout_coords
    x = 0
    y = 0
    reset_canvas()
    for j in range(0, quant + 1):
        barcode_canvas.create_text(blackout_coords[j][0] + 270, blackout_coords[j][1] + 40, text=tpn_list[j])
    # create blackouts
    for j in range(0, focus):
        barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 295, 30, fill='black'), blackout_coords[j][0], blackout_coords[j][1])
    if focus < quant:
        for j in range(focus + 1, quant + 1):
            barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 295, 30, fill='black'), blackout_coords[j][0],
                                blackout_coords[j][1])
    # draw barcode at focus
    bar_chars = []
    for j in range(0, 9):
        bar_chars.append(char_list[int((tpn_list[focus][j]))])
        # bar_chars.append(char_list[tpn_list[tpn_focus][j]])
    # add 5 zeroes to the end to make tpn 14digs long(normally case size but case size is not required)
    for j in range(0, 5):
        bar_chars.append(char_list[0])
    # add start characters as rectangle
    if tpn_focus < 10:
        x = 20
        y = 10 + (50 * focus)
    elif focus < 20:
        x = 400
        y = 10 + (50 * (focus - 10))
    for _ in char_list[10]:
        barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 1, 30, fill='black'), x, y)
        x += 4
    # add barcode
    for j in range(0, len(bar_chars) - 1, 2):
        for k in range(0, 5):
            if bar_chars[j][k] == 0:
                # thin black
                barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 1, 30, fill='black'), x, y)
                x += 2
            else:
                # thick black
                barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 4, 30, fill='black'), x, y)
                x += 5
            if bar_chars[j + 1][k] == 0:
                x += 2
            # thin white
            else:
                x += 6
                # thickwhite
        # stop
        barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 4, 30, fill='black'), x, y)
        x += 7
        barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 1, 30, fill='black'), x, y)


def key_pressed(event):  # todo if bar_entry[0] == "0", so shit, otherwise don't if tpn_quant > 19 don't do shit
    global tpn_quant
    global tpn_focus
    if repr(event.keysym).strip("'") == "Down":
        bar_entry.delete(0, END)
        if tpn_focus < tpn_quant:
            tpn_focus += 1
            generate(tpn_quant, tpn_focus)
    elif repr(event.keysym).strip("'") == "Up":
        bar_entry.delete(0, END)
        if tpn_focus > 0:
            tpn_focus -= 1
            generate(tpn_quant, tpn_focus)
    # allows only digits to be input
    elif repr(event.keysym).strip("'") == "BackSpace":
        return 0
    elif not repr(event.char).strip("'").isdigit():
        return 'break'
    elif bar_entry.get() != "" and bar_entry.get()[0] == "0" and len(bar_entry.get()) == 8 and tpn_quant < 19:
        tpn = bar_entry.get() + str(repr(event.char))[1]
        tpn_list.append(tpn)
        tpn_quant += 1
        print(tpn_quant)
        generate(tpn_quant, tpn_focus)
        # clear tpn entry widget
        bar_entry.delete(0, END)
        # prevents last input from being put in after clearing for some reason required
        return "break"
    else:
        return 0


bar_entry.bind("<Key>", key_pressed)

root.mainloop()



