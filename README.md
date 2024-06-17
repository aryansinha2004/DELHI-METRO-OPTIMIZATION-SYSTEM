# DELHI-METRO-OPTIMIZATION-SYSTEM
This project is a Delhi Metro Operations Optimization system implemented using Python and Tkinter. The application provides functionalities for scheduling optimization, predictive maintenance simulation, and passenger flow management for various metro lines.

## Features

1. **Scheduling Optimization**: Optimizes train schedules to minimize waiting time.
2. **Predictive Maintenance**: Simulates and predicts maintenance needs based on train usage.
3. **Passenger Flow Management**: Analyzes and visualizes passenger flow to identify peak hours.
4. **Route Map Display**: Displays the route map of the Delhi Metro.

Features Available:

Select the metro line and direction.
Click on "Optimize Scheduling" to get an optimized schedule.
Click on "Predictive Maintenance" to view maintenance schedules and needs.
Click on "Passenger Flow Management" to visualize passenger flow data.
Click on "Show Route Map" to view the Delhi Metro route map.
Code Overview
Metro Lines and Routes Data
The metro_lines dictionary holds the start and end stations for each metro line.

Functions
scheduling_optimization(line, direction): Optimizes train schedules.
predictive_maintenance_simulation(line): Simulates and predicts maintenance needs.
passenger_flow_management(line): Analyzes and visualizes passenger flow data.
display_results(func, *args): Displays the results in the UI.
show_route_map(): Displays the route map.
Tkinter UI Components
The Tkinter window is created with a gradient background from blue to purple. Various UI components such as buttons, labels, and text widgets are added to interact with the application functionalities.

Gradient Background
The create_gradient_background(canvas, color1, color2) function creates a gradient background for the Tkinter window.

