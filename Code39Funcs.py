from tkinter import *


def initialise_dict():
    # code list-all integers 0-9 (1=black line, 0=blank line
    code_list = ['101001101101', '110100101011', '101100101011', '110110010101', '101001101011', '110100110101',
                 '101100110101',
                 '101001011011', '110100101101', '101100101101']
    # '*' represents start and stop command for code39 barcodes
    di = {'*': '100101101101'}
    # create dictionary to read values from
    for i in range(0, 10):
        di[str(i)] = code_list[i]
    return di


class Tpn:
    def __init__(self, widget, tpn_li, tpn_foc, root_tk, canvas, di):
        self.widget = widget
        self.tpn_li = tpn_li
        self.tpn_foc = tpn_foc
        self.canvas = canvas
        self.root_tk = root_tk
        self.di = di

    def generate(self):
        self.canvas.destroy()
        self.canvas = Canvas(self.root_tk)
        self.canvas.pack(fill=BOTH, expand=True)

        def draw_bar(posn):
            x = color = None  # gets rid of annoying "referenced before assignment" weak warning
            if posn < 10:
                x = 20
            elif posn < 20:
                x = 496
                posn = posn - 10
            y = 20 + (45 * posn)
            # start command symbol (*)
            for starter_line in self.di["*"]:
                if starter_line == "0":
                    color = "white"
                elif starter_line == "1":
                    color = "black"
                self.canvas.create_line(x, y, x, y + 30, width=2, fill=color)
                x += 2
            x += 2
            # main body of bar code
            for number in self.tpn_li[self.tpn_foc]:
                for line in self.di[str(number)]:
                    if line == "0":
                        color = "white"
                    elif line == "1":
                        color = "black"
                    self.canvas.create_line(x, y, x, y + 30, width=2, fill=color)
                    x += 2
                x += 2
            # end command (*) again(could have been cleverer with this(added in with start but dif coords)
            # but reads better
            for end_line in self.di["*"]:
                if end_line == "0":
                    color = "white"
                elif end_line == "1":
                    color = "black"
                self.canvas.create_line(x, y, x, y + 30, width=2, fill=color)
                x += 2

        def draw_rect(posn):
            x = None
            if posn < 10:
                x = 20
            elif posn < 20:
                x = 496
                posn = posn - 10
            self.canvas.create_rectangle(x, 20 + (45 * posn), x + 284, 50 + (45 * posn), fill='black')

        def draw_text(posn):
            x = None
            if posn < 10:
                x = 277
            elif posn < 20:
                x = 753
                posn = posn - 10
            self.canvas.create_text(x, 57 + (45 * posn), text=self.tpn_li[posn])

        for i in range(0, len(self.tpn_li)):  # draw text for tpns
            draw_text(i)
            if i == self.tpn_foc:
                draw_bar(i)
            else:
                draw_rect(i)

    def key_pressed(self, event):
        # only allows up, down, backspace and digits (only if the first one is "0")
        # only allowing 0 as first as company numbers always starts 0
        # therefore prevents mistakes when typing while not screen-watching
        char = repr(event.char).strip("'")
        sym = repr(event.keysym).strip("'")
        entry_get = self.widget.get()
        if sym == "Up":
            self.widget.delete(0, END)
            if self.tpn_foc > 0:
                self.tpn_foc -= 1
                self.generate()
                return 'break'
        elif sym == "Down":
            self.widget.delete(0, END)
            if self.tpn_foc < len(self.tpn_li) - 1:
                self.tpn_foc += 1
                self.generate()
                return 'break'
        elif entry_get == "" and char != "0":
            return 'break'
        elif char.isdigit() and len(entry_get) == 8:
            self.tpn_li.append(entry_get + char)
            self.widget.delete(0, END)
            self.generate()
            return 'break'

    def clear_screen(self):
        self.tpn_foc = 0
        self.tpn_li = []
        self.generate()


if __name__ == '__main__':
    pass





