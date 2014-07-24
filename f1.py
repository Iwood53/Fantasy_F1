import Tkinter
import tkMessageBox
import gen_pick_list


def clk_gen_list():
    pick_list = gen_pick_list.go(entry.get())
    pick_list_str = ''
    for driver in pick_list:
        pick_list_str += str(driver[0]) + ' - ' + driver[1] + '\n'

    top = Tkinter.Toplevel()
    top.title('Pick List')
    msg = Tkinter.Message(top, text=pick_list_str)
    msg.pack()


root = Tkinter.Tk()
root.title("Fantasy F1")
label = Tkinter.Label(root, text='Enter URL of PaddyPower Page').pack()
entry = Tkinter.Entry(root)
entry.pack()
button = Tkinter.Button(root, text='Generate Pick List', command=clk_gen_list).pack()
root.mainloop()
