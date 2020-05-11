from tkinter import *
# -initialisation- (some crucial parts initialised in clear_screen())
# list representing characters from 0-9, start char and end char in ITF format
char_list = [(0, 0, 1, 1, 0), (1, 0, 0, 0, 1), (0, 1, 0, 0, 1), (1, 1, 0, 0, 0,), (0, 0, 1, 0, 1), (1, 0, 1, 0, 0), (0, 1, 1, 0, 0), (0, 0, 0, 1, 1), (1, 0, 0, 1, 0), (0, 1, 0, 1, 0), (0, 0), (0, 0)]
# list of coords to place blackouts - constant
blackout_coords = []
for i in range(0, 10):
    blackout_coords.append([20, 10 + 50 * i])
for i in range(0, 10):
    blackout_coords.append([400, 10 + 50 * i])

root = Tk()
root.title("Barcode Generator 1.0 - Stephen Turley - April 2020")
root.geometry("800x600")
main_frame = Frame(root)
main_frame.pack()

bar_entry = Entry(main_frame, width=9)
bar_entry.grid(column=0, row=0)
bar_entry.focus_set()

barcode_canvas = Canvas()


# reset clears the screen so that images can be re-drawn
def reset_canvas():
    global barcode_canvas
    barcode_canvas.destroy()
    barcode_canvas = Canvas(main_frame, height=550, width=800)
    barcode_canvas.grid(column=0, row=3)


# clear screen resets initial variables and calls reset_canvas()
def clear_screen():
    global tpn_list
    global tpn_focus
    global tpn_quant
    tpn_list = []
    tpn_focus = 0
    tpn_quant = -1
    reset_canvas()


# first instance initialises
clear_screen()

clear_screen_btn = Button(main_frame, text='Clear Screen', command=clear_screen)
clear_screen_btn.grid(column=0, row=1)


# when valid input given by key_pressed func - or when focus is changed - draws barcode@focus and blackouts at other slots
def generate(quant, focus):
    global blackout_coords
    x = 0
    y = 0
    reset_canvas()
    for j in range(0, quant + 1):
        barcode_canvas.create_text(blackout_coords[j][0] + 185, blackout_coords[j][1] + 40, text=tpn_list[j])
    # create blackouts
    for j in range(0, focus):
        barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 212, 30, fill='black'), blackout_coords[j][0], blackout_coords[j][1])
    if focus < quant:
        for j in range(focus + 1, quant + 1):
            barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 212, 30, fill='black'), blackout_coords[j][0],
                                blackout_coords[j][1])
    # populate bar_chars (barcode at focus)
    bar_chars = []
    for j in range(0, 9):
        bar_chars.append(char_list[int((tpn_list[focus][j]))])
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

    # draw barcode at focus
    # start command part of barcode
    for _ in char_list[10]:
        barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 1, 30, fill='black'), x, y)
        x += 4
    # add barcode main body
    for j in range(0, len(bar_chars) - 1, 2):
        for k in range(0, 5):
            if bar_chars[j][k] == 0:
                # thin black
                barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 1, 30, fill='black'), x, y)
                x += 2
            else:
                # thick black
                barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 3, 30, fill='black'), x, y)
                x += 4
            if bar_chars[j + 1][k] == 0:
                # thin white
                x += 2
            else:
                # thick white
                x += 4
    # stop command part of barcode
    barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 3, 30, fill='black'), x, y)
    x += 6
    barcode_canvas.move(barcode_canvas.create_rectangle(0, 0, 1, 30, fill='black'), x, y)


def key_pressed(event):
    global tpn_quant
    global tpn_focus
    # key up and down changes focus
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
    # only allow first digit to be zero, input.isdigit and pulls entry after 9 digs
    elif repr(event.keysym).strip("'") == "BackSpace":
        return 0
    elif not repr(event.char).strip("'").isdigit():
        return 'break'
    elif len(bar_entry.get()) == 0 and repr(event.char).strip("'") != "0":
        return 'break'
    elif bar_entry.get() != "" and bar_entry.get()[0] == "0" and len(bar_entry.get()) == 8 and tpn_quant < 19:
        tpn = bar_entry.get() + str(repr(event.char))[1]
        tpn_list.append(tpn)
        tpn_quant += 1
        generate(tpn_quant, tpn_focus)
        # clear tpn entry widget
        bar_entry.delete(0, END)
        # prevents last input from being put in after clearing for some reason required
        return "break"


bar_entry.bind("<Key>", key_pressed)

root.mainloop()



