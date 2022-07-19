import tkinter as t

def Calculation():
    mile = float(input_mile.get())
    km = mile * 1.609
    lable_0.config(text=f"{km}")
    

window = t.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)
# window.minsize(width=300, height=100)

input_mile = t.Entry(width=10)
input_mile.grid(row=0, column=1)

lable_Miles = t.Label(text="Miles")
lable_Miles.grid(row=0, column=2)

lable_is_eq = t.Label(text="is equal to")
lable_is_eq.grid(row=1, column=0)

lable_0 = t.Label(text="0")
lable_0.grid(row=1, column=1)

lable_km = t.Label(text="Km")
lable_km.grid(row=1, column=2)

calculate_button = t.Button(text="Calculate", command=Calculation)
calculate_button.grid(row=2, column=1)


window.mainloop()