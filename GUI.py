import tkinter as tk
from main import post_to_tistory


def submit_post():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END)
    post_to_tistory(title, content)
window = tk.Tk()
window.title("blog write") #티스토리 글 작성 -> blog write (한글이 깨져서 출력됨)

title_label = tk.Label(window, text="title")
title_label.pack()
title_entry = tk.Entry(window)
title_entry.pack()

content_label = tk.Label(window, text="content")
content_label.pack()
content_text = tk.Text(window)
content_text.pack()

submit_button = tk.Button(window, text="write", command=submit_post)
submit_button.pack()

window.mainloop()
