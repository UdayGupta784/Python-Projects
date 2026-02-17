import requests
import tkinter as tk
from tkinter import messagebox
API_KEY = "c3297cee0a8b6fe6a8643c4bae459fd8"

search_history = []

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    
    para = {"q":city,"appid": API_KEY, "units": "metric"}
    response = requests.get(url,params=para)
    data = response.json()
    return data

def show():
    city = city_enter.get()
    if city=="":
        messagebox.showwarning("Error! Enter a Valid City Name")
        return
    if city not in search_history:
        search_history.append(city)
        history.insert(tk.END, city)

    try:
        data = get_weather(city)
        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found")
            return
        #Needed Data
        temp = data["main"]["temp"]
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        result_label.config(
            text=f"Temperature: {temp} °C\n"
                 f"Humidity: {humidity}%\n"
                 f"Condition: {description}"
        )

    except:
        messagebox.showerror("Error", "Something went wrong")
def load_history(a):
    selected = history.curselection()
    if selected:
        city = history.get(selected[0])
        city_enter.delete(0, tk.END)
        city_enter.insert(0, city)
        show()

def clear():
    city_enter.delete(0, tk.END)
    result_label.config(text="")

#Tkinter GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("500x500")
root.config(bg="#1e1e2f")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

title =tk.Label(root, text="Weather App", font=("Time New Roman", 22,'bold'),bg="#1e1e2f",fg='white')
title.grid(row=0, column=0, columnspan=2, pady=20)

city_enter = tk.Entry(root,font=("Arial", 15),width=25,bd=0,justify="center")
city_enter.grid(row=1, column=0, columnspan=2, pady=10)
history_title = tk.Label(root,text="Search History",font=("Arial", 14, "bold"),bg="#1e1e2f",fg="white")
history_title.grid(row=4, column=0, columnspan=2, pady=(10, 0))

history = tk.Listbox(root, height=5)
history.grid(row=5, column=0, columnspan=2, pady=10)
history.bind("<<ListboxSelect>>", load_history)

search_bt = tk.Button(root,text="Get Weather",font=("Arial", 12, "bold"),bg="#4CAF70",fg="white",activebackground="#45a049",padx=10,pady=5,command=show)
search_bt.grid(row=2, column=0, padx=10, pady=10)

# Clear Button
clear_bt = tk.Button(root,text="Clear",font=("Arial", 12),bg="#f44636",fg="white",padx=10,pady=5,command=clear)
clear_bt.grid(row=2, column=1, padx=10, pady=10)

# Result Frame 
result_frame = tk.Frame(root, bg="#332c3e", bd=0)
result_frame.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")

result_label = tk.Label(result_frame,text="",font=("Arial", 14),bg="#332c3e",fg="white",justify="center")
result_label.pack(pady=20)


root.mainloop()

