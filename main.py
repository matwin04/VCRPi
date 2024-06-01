import customtkinter as tk

app = tk.CTk()
lbl1 = tk.CTkLabel(
    master=app,
    text="VCRPi Manager"
)
fra_1 = tk.CTkFrame(
    master=app,
    border_width=2,
    border_color='white',
)
fra1_lbl1 = tk.CTkLabel(
    master=fra_1,
    text="Server Controls"
)
fra1_btn1 = tk.CTkButton(
    master=fra_1,
    text="Start",
    fg_color="green",
    hover_color="yellow"
)
fra1_btn2 = tk.CTkButton(
    master=fra_1,
    text="Stop",
    fg_color="red",
    hover_color="yellow"
)
lbl1.pack(padx=10,pady=10)

fra_1.pack(padx=10,pady=10)
fra1_lbl1.pack()
fra1_btn1.pack(padx=5,pady=5)
fra1_btn2.pack(padx=5,pady=5)
app.mainloop()