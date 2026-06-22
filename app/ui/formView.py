import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import csv
import os

class FormView:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        title_label = ttk.Label(root, text="ABQ Data Entry Application", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)
        
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        rec_frame = ttk.LabelFrame(main_frame, text="Record Information", padding="10")
        rec_frame.pack(fill=tk.X, pady=5)
        rec_frame.columnconfigure((0, 1, 2), weight=1)
        
        ttk.Label(rec_frame, text="Date", anchor="center").grid(row=0, column=0, sticky="ew")
        ttk.Label(rec_frame, text="Time", anchor="center").grid(row=0, column=1, sticky="ew")
        ttk.Label(rec_frame, text="Technician", anchor="center").grid(row=0, column=2, sticky="ew")
        
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.date_entry = ttk.Entry(rec_frame, textvariable=self.date_var)
        self.date_entry.grid(row=1, column=0, padx=5, pady=2, sticky="ew")
        
        self.time_var = tk.StringVar()
        self.time_cb = ttk.Combobox(rec_frame, textvariable=self.time_var, values=["08:00", "12:00", "16:00", "20:00"])
        self.time_cb.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        
        self.tech_var = tk.StringVar()
        self.tech_entry = ttk.Entry(rec_frame, textvariable=self.tech_var)
        self.tech_entry.grid(row=1, column=2, padx=5, pady=2, sticky="ew")
        
        ttk.Label(rec_frame, text="Lab", anchor="center").grid(row=2, column=0, sticky="ew")
        ttk.Label(rec_frame, text="Plot", anchor="center").grid(row=2, column=1, sticky="ew")
        ttk.Label(rec_frame, text="Seed Sample", anchor="center").grid(row=2, column=2, sticky="ew")
        
        self.lab_var = tk.StringVar(value="A")
        lab_radio_frame = ttk.Frame(rec_frame)
        lab_radio_frame.grid(row=3, column=0, padx=5, pady=2)
        ttk.Radiobutton(lab_radio_frame, text="A", variable=self.lab_var, value="A").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(lab_radio_frame, text="B", variable=self.lab_var, value="B").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(lab_radio_frame, text="C", variable=self.lab_var, value="C").pack(side=tk.LEFT, padx=5)
        
        self.plot_var = tk.StringVar()
        self.plot_cb = ttk.Combobox(rec_frame, textvariable=self.plot_var, values=["1", "2", "3", "4", "5"])
        self.plot_cb.grid(row=3, column=1, padx=5, pady=2, sticky="ew")
        
        self.seed_var = tk.StringVar()
        self.seed_entry = ttk.Entry(rec_frame, textvariable=self.seed_var)
        self.seed_entry.grid(row=3, column=2, padx=5, pady=2, sticky="ew")

        env_frame = ttk.LabelFrame(main_frame, text="Environment Data", padding="10")
        env_frame.pack(fill=tk.X, pady=5)
        env_frame.columnconfigure((0, 1, 2), weight=1)
        
        ttk.Label(env_frame, text="Humidity (g/m³)", anchor="center").grid(row=0, column=0, sticky="ew")
        ttk.Label(env_frame, text="Light (klx)", anchor="center").grid(row=0, column=1, sticky="ew")
        ttk.Label(env_frame, text="Temperature (°C)", anchor="center").grid(row=0, column=2, sticky="ew")
        
        self.humidity_var = tk.DoubleVar(value=0.0)
        self.humidity_sp = ttk.Spinbox(env_frame, from_=0.0, to=100.0, increment=0.1, textvariable=self.humidity_var)
        self.humidity_sp.grid(row=1, column=0, padx=5, pady=2, sticky="ew")
        
        self.light_var = tk.DoubleVar(value=0.0)
        self.light_sp = ttk.Spinbox(env_frame, from_=0.0, to=100.0, increment=0.1, textvariable=self.light_var)
        self.light_sp.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        
        self.temp_var = tk.DoubleVar(value=0.0)
        self.temp_sp = ttk.Spinbox(env_frame, from_=-50.0, to=100.0, increment=0.1, textvariable=self.temp_var)
        self.temp_sp.grid(row=1, column=2, padx=5, pady=2, sticky="ew")
        
        self.fault_var = tk.BooleanVar(value=False)
        self.fault_check = ttk.Checkbutton(env_frame, text="Equipment Fault", variable=self.fault_var)
        self.fault_check.grid(row=2, column=0, columnspan=3, sticky="w", padx=5, pady=5)

        plant_frame = ttk.LabelFrame(main_frame, text="Plant Data", padding="10")
        plant_frame.pack(fill=tk.X, pady=5)
        plant_frame.columnconfigure((0, 1, 2), weight=1)
        
        ttk.Label(plant_frame, text="Plants", anchor="center").grid(row=0, column=0, sticky="ew")
        ttk.Label(plant_frame, text="Blossoms", anchor="center").grid(row=0, column=1, sticky="ew")
        ttk.Label(plant_frame, text="Fruit", anchor="center").grid(row=0, column=2, sticky="ew")
        
        self.plants_var = tk.IntVar(value=0)
        self.plants_sp = ttk.Spinbox(plant_frame, from_=0, to=1000, increment=1, textvariable=self.plants_var)
        self.plants_sp.grid(row=1, column=0, padx=5, pady=2, sticky="ew")
        
        self.blossoms_var = tk.IntVar(value=0)
        self.blossoms_sp = ttk.Spinbox(plant_frame, from_=0, to=1000, increment=1, textvariable=self.blossoms_var)
        self.blossoms_sp.grid(row=1, column=1, padx=5, pady=2, sticky="ew")
        
        self.fruit_var = tk.IntVar(value=0)
        self.fruit_sp = ttk.Spinbox(plant_frame, from_=0, to=1000, increment=1, textvariable=self.fruit_var)
        self.fruit_sp.grid(row=1, column=2, padx=5, pady=2, sticky="ew")
        
        ttk.Label(plant_frame, text="Min Height (cm)", anchor="center").grid(row=2, column=0, sticky="ew")
        ttk.Label(plant_frame, text="Max Height (cm)", anchor="center").grid(row=2, column=1, sticky="ew")
        ttk.Label(plant_frame, text="Median Height (cm)", anchor="center").grid(row=2, column=2, sticky="ew")
        
        self.min_h_var = tk.DoubleVar(value=0.0)
        self.min_h_sp = ttk.Spinbox(plant_frame, from_=0.0, to=500.0, increment=0.1, textvariable=self.min_h_var)
        self.min_h_sp.grid(row=3, column=0, padx=5, pady=2, sticky="ew")
        
        self.max_h_var = tk.DoubleVar(value=0.0)
        self.max_h_sp = ttk.Spinbox(plant_frame, from_=0.0, to=500.0, increment=0.1, textvariable=self.max_h_var)
        self.max_h_sp.grid(row=3, column=1, padx=5, pady=2, sticky="ew")
        
        self.med_h_var = tk.DoubleVar(value=0.0)
        self.med_h_sp = ttk.Spinbox(plant_frame, from_=0.0, to=500.0, increment=0.1, textvariable=self.med_h_var)
        self.med_h_sp.grid(row=3, column=2, padx=5, pady=2, sticky="ew")

        notes_frame = ttk.Frame(main_frame, padding="5")
        notes_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        ttk.Label(notes_frame, text="Notes", anchor="center").pack(fill=tk.X)
        self.notes_text = tk.Text(notes_frame, height=6, wrap=tk.WORD)
        self.notes_text.pack(fill=tk.BOTH, expand=True, pady=2)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, side=tk.BOTTOM, pady=5)
        
        btn_frame.columnconfigure(0, weight=1) 
        
        self.reset_btn = ttk.Button(btn_frame, text="Reset", command=self.reset_fields)
        self.reset_btn.grid(row=0, column=1, padx=5)
        
        self.save_btn = ttk.Button(btn_frame, text="Save", command=self.save_data)
        self.save_btn.grid(row=0, column=2, padx=5)

    def save_data(self):
        notes_content = self.notes_text.get("1.0", tk.END).strip()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print("current_dir =>", current_dir)
        ui_dir = os.path.dirname(current_dir)
        root_dir = os.path.dirname(ui_dir)
        
        today_str = datetime.now().strftime('%Y-%m-%d')
        folder_path = os.path.join(root_dir, f"postpix-{today_str}")
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, f"data-{today_str}.csv")
        
        headers = [
            "Timestamp", "Date", "Time", "Technician", "Lab", "Plot", "Seed Sample",
            "Humidity (g/m³)", "Light (klx)", "Temperature (°C)", "Equipment Fault",
            "Plants", "Blossoms", "Fruit", "Min Height (cm)", "Max Height (cm)", "Median Height (cm)", "Notes"
        ]
        
        row_data = [
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            self.date_var.get(),
            self.time_var.get(),
            self.tech_var.get(),
            self.lab_var.get(),
            self.plot_var.get(),
            self.seed_var.get(),
            self.humidity_var.get(),
            self.light_var.get(),
            self.temp_var.get(),
            self.fault_var.get(),
            self.plants_var.get(),
            self.blossoms_var.get(),
            self.fruit_var.get(),
            self.min_h_var.get(),
            self.max_h_var.get(),
            self.med_h_var.get(),
            notes_content
        ]
        
        file_exists = os.path.isfile(file_path)
        
        try:
            with open(file_path, mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(headers)
                writer.writerow(row_data)
            messagebox.showinfo("Success", f"Data saved successfully inside root folder:\n{file_path}!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")
            
    def reset_fields(self):
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
        self.time_var.set("")
        self.time_cb.set("")
        self.tech_var.set("")
        self.lab_var.set("A")
        self.plot_var.set("")
        self.plot_cb.set("")
        self.seed_var.set("")
        
        self.humidity_var.set(0.0)
        self.light_var.set(0.0)
        self.temp_var.set(0.0)
        self.fault_var.set(False)
        
        self.plants_var.set(0)
        self.blossoms_var.set(0)
        self.fruit_var.set(0)
        self.min_h_var.set(0.0)
        self.max_h_var.set(0.0)
        self.med_h_var.set(0.0)
        
        self.notes_text.delete("1.0", tk.END)