import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Text, END, StringVar, OptionMenu, Frame, Toplevel
from PIL import Image, ImageTk

# Metro Lines and Routes Data
metro_lines = {
    "Red Line": ["Shaheed Sthal", "Rithala"],
    "Yellow Line": ["Samaypur Badli", "Huda City Centre"],
    "Blue Line": ["Dwarka Sector 21", "Noida City Centre"],
    "Pink Line": ["Majlis Park", "Shiv Vihar"],
    "Magenta Line": ["Botanical Garden", "Janakpuri West"],
    "Green Line": ["Inderlok", "Brigadier Hoshiar Singh"],
    "Violet Line": ["Kashmere Gate", "Raja Nahar Singh"]
}

# Function for Scheduling Optimization
def scheduling_optimization(line, direction):
    start_station, end_station = metro_lines[line]
    trains = [
        f"{start_station} to {end_station}",
        f"{end_station} to {start_station}",
        f"{start_station} to {end_station}",
        f"{end_station} to {start_station}"
    ]
    data = {
        'Train': trains,
        'Start_Station': [start_station, end_station, start_station, end_station],
        'End_Station': [end_station, start_station, end_station, start_station],
        'Arrival_Time': ['08:00', '08:05', '08:10', '08:15'],
        'Departure_Time': ['08:02', '08:07', '08:12', '08:17']
    }
    schedule_df = pd.DataFrame(data)
    schedule_df['Arrival_Time'] = pd.to_datetime(schedule_df['Arrival_Time'])
    schedule_df['Departure_Time'] = pd.to_datetime(schedule_df['Departure_Time'])

    # Optimize schedule to minimize the waiting time between trains
    schedule_df['Next_Arrival'] = schedule_df['Arrival_Time'].shift(-1)
    schedule_df['Wait_Time'] = (schedule_df['Next_Arrival'] - schedule_df['Departure_Time']).dt.total_seconds() / 60
    average_wait_time = schedule_df['Wait_Time'].mean()

    result = f"Optimized Schedule for {line} ({direction}):\n{schedule_df}\nAverage Wait Time: {average_wait_time} minutes\n"
    return result

# Function for Predictive Maintenance Simulation
def predictive_maintenance_simulation(line):
    start_station, end_station = metro_lines[line]
    trains = [
        f"{start_station} to {end_station}",
        f"{end_station} to {start_station}",
        f"{start_station} to {end_station}",
        f"{end_station} to {start_station}"
    ]
    maintenance_data = {
        'Train': trains,
        'Last_Maintenance': ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04'],
        'Next_Maintenance_Due': ['2024-06-01', '2024-06-02', '2024-06-03', '2024-06-04']
    }
    maintenance_df = pd.DataFrame(maintenance_data)
    maintenance_df['Last_Maintenance'] = pd.to_datetime(maintenance_df['Last_Maintenance'])
    maintenance_df['Next_Maintenance_Due'] = pd.to_datetime(maintenance_df['Next_Maintenance_Due'])

    # Predict maintenance needs based on usage
    maintenance_df['Usage'] = np.random.randint(100, 1000, size=len(maintenance_df))  # Simulated usage data
    maintenance_threshold = 800

    maintenance_df['Maintenance_Needed'] = maintenance_df['Usage'] > maintenance_threshold

    result = f"Maintenance Schedule for {line}:\n{maintenance_df}\n"
    return result

# Function for Passenger Flow Management
def passenger_flow_management(line):
    time_intervals = pd.date_range(start='08:00', end='10:00', freq='10min')
    passenger_counts = np.random.poisson(lam=50, size=len(time_intervals))

    flow_df = pd.DataFrame({'Time': time_intervals, 'Passenger_Count': passenger_counts})

    # Plot passenger flow
    plt.figure(figsize=(10, 6))
    plt.plot(flow_df['Time'], flow_df['Passenger_Count'], marker='o')
    plt.title(f'Passenger Flow Over Time ({line})')
    plt.xlabel('Time')
    plt.ylabel('Number of Passengers')
    plt.grid(True)
    plt.show()

    # Identify peak hours
    peak_threshold = 70
    peak_hours = flow_df[flow_df['Passenger_Count'] > peak_threshold]

    result = f"Peak Hours with High Passenger Flow ({line}):\n{peak_hours}\n"
    return result

# Function to display results in the UI
def display_results(func, *args):
    result_text.delete(1.0, END)
    result = func(*args)
    result_text.insert(END, result)

# Function to show the route map
def show_route_map():
    top = Toplevel(root)
    top.title("Delhi Metro Route Map")
    img = Image.open("delhi_metro_route_map.png")  # Placeholder for the route map image
    img = img.resize((600, 400), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    panel = Label(top, image=img)
    panel.image = img  # Keep a reference to avoid garbage collection
    panel.pack()

# Tkinter UI Setup
root = Tk()
root.title("Delhi Metro Operations Optimization")
root.geometry("900x700")
root.configure(bg="#f0f0f0")

# Variables for OptionMenu
selected_line = StringVar(root)
selected_line.set(list(metro_lines.keys())[0])
selected_direction = StringVar(root)
selected_direction.set("Forward")

# Main frame
main_frame = Frame(root, bg="#f0f0f0")
main_frame.pack(pady=20)

# UI Components
Label(main_frame, text="Delhi Metro Operations Optimization", font=("Helvetica", 18, "bold"), bg="#f0f0f0").grid(row=0, columnspan=2, pady=10)

Label(main_frame, text="Select Metro Line:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=1, column=0, pady=5, sticky='e')
OptionMenu(main_frame, selected_line, *metro_lines.keys()).grid(row=1, column=1, pady=5, sticky='w')

Label(main_frame, text="Select Direction:", bg="#f0f0f0", font=("Helvetica", 12)).grid(row=2, column=0, pady=5, sticky='e')
OptionMenu(main_frame, selected_direction, "Forward", "Backward").grid(row=2, column=1, pady=5, sticky='w')

Button(main_frame, text="Optimize Scheduling", command=lambda: display_results(scheduling_optimization, selected_line.get(), selected_direction.get()), bg="#4CAF50", fg="white", font=("Helvetica", 12)).grid(row=3, columnspan=2, pady=10)

Button(main_frame, text="Predictive Maintenance", command=lambda: display_results(predictive_maintenance_simulation, selected_line.get()), bg="#2196F3", fg="white", font=("Helvetica", 12)).grid(row=4, columnspan=2, pady=10)

Button(main_frame, text="Passenger Flow Management", command=lambda: display_results(passenger_flow_management, selected_line.get()), bg="#FF9800", fg="white", font=("Helvetica", 12)).grid(row=5, columnspan=2, pady=10)

Button(main_frame, text="Show Route Map", command=show_route_map, bg="#9C27B0", fg="white", font=("Helvetica", 12)).grid(row=6, columnspan=2, pady=10)

result_text = Text(main_frame, height=15, width=80, font=("Helvetica", 10))
result_text.grid(row=7, columnspan=2, pady=20)

# Run the Tkinter event loop
root.mainloop()

