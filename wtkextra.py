import tkinter as tk


def wtk_input_window(main_window, string_var, title, input_info, send_info):
    def send():
        input_window.destroy()

    input_window = tk.Toplevel(main_window)
    input_window.title(title)
    input_window.geometry("400x200")
    input_window.resizable(False, False)
    input_window.grab_set()

    input_info = tk.Label(input_window, text=input_info, font=("Arabic Transparent", 15, "bold"))
    input_info.grid(row=0, column=0, pady=40)

    input_box = tk.Entry(input_window, width=50, textvariable=string_var)
    input_box.grid(row=1, column=0, padx=20, ipady=3)

    send_button = tk.Button(input_window, text=send_info, height=1, width=10, command=send)
    send_button.grid(row=2, column=0, padx=20, pady=15, ipady=3)


window = tk.Tk()

hex_color = tk.StringVar()
hex_color.set("")

wtk_input_window(window, hex_color, "我是測試視窗", "請輸入文字", "送出")

btn = tk.Button(window, text="Show", height=1, width=10, command=lambda : print(hex_color.get()))
btn.grid(row=3, column=0, padx=20, pady=15)

window.mainloop()