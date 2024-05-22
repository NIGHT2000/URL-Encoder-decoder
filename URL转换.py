import tkinter as tk
from urllib.parse import quote, unquote

def encode_text():
    input_text = entry.get()
    encoded_text = quote(input_text)
    result_label.config(text=encoded_text)

def decode_text():
    input_text = entry.get()
    try:
        decoded_text = unquote(input_text)
        result_label.config(text=decoded_text)
    except Exception as e:
        result_label.config(text="请输入正确的URL编码内容")

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))

root = tk.Tk()
root.title("URL编码器")
root.configure(bg="#EEE0E5")

entry = tk.Entry(root, width=50, bg="#FFE4C4")
entry.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(side="right", padx=10)

encode_button = tk.Button(buttons_frame, text="编码", command=encode_text)
encode_button.pack(pady=5)

decode_button = tk.Button(buttons_frame, text="解码", command=decode_text)
decode_button.pack(pady=5)

copy_button = tk.Button(buttons_frame, text="复制", command=copy_text)
copy_button.pack(pady=5)

result_label = tk.Label(root, text="", bg="#B0E0E6")
result_label.pack(pady=10)

root.mainloop()
