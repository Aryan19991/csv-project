"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Student ID: w2083972
 4. Date: 
****************************************************************************

"""

# The required imports for this coursework-----------------------------------------------------------
from graphics import *
import csv

# Function to get the date from the user--------------------------------------------------------------
def get_date():
    while True:
        try:
            specific_day = int(input('Enter the day of the survey in the order DD: '))
            if specific_day < 1 or specific_day > 31:
                print('The values are out of range, Please have valid input.')
                continue

            specific_month = int(input('Enter the month in which the survey is done in the order MM: '))
            if specific_month < 1 or specific_month > 12:
                print('The values are out of range, Please have valid input in the range 1 to 12.')
                continue

            specific_year = int(input('Enter the year in which the survey is done in the order of YY: '))
            if specific_year < 2000 or specific_year > 2024:
                print('The values are out of range, Please have the year from 2000 to 2024: ')
                continue

            return f"{specific_day:02d}{specific_month:02d}{specific_year:02d}"
        #If date input is wrong, this error occurs
        except ValueError:
            print("Please enter an integer!!!!")

# Function to open, read and analyze the data----------------------------------------------------------------
def analyze_the_data(filename):
    # Initialize vehicle count per hour for each junction---------------------------------------------------
    with open(filename, 'r') as file:
        csv_data = csv.reader(file)
        header = next(csv_data)
# Converting the remaining row into a list after the header reads the header row----------------------------
        data_as_list = list(csv_data)

# Initializing the vehicle count per hour for each junction after reading the data---------------------------
        vehicle_count_per_hour = {
            "Elm Avenue/Rabbit Road": {},
            "Hanley Highway/Westway": {}
        }

# Initializing vehicle counters--------------------------------------------------------------------------------
        total_vehicle = 0
        total_truck = 0
        total_electric_vehicle = 0
        total_two_wheeled = 0
        total_bicycle = 0
        number_of_vehicles_peak_hour = 0

        # Initialize bus counters
        buses_heading_north = 0
        buses_heading_straight = 0    

        # Initialize percentages
        percentage_of_truck = 0
        percentage_of_scooters_ElmAvenue_RabbitRoad = 0

        # Initialize other counters
        vehicles_over_the_speed_limit = 0
        vehicles_passing_through_ElmAvenue_RabbitRoad = 0
        vehicles_passing_through_HanleyHighway_Westway = 0
        number_of_scooters_ElmAvenue_RabbitRoad = 0
        number_of_hours_rained = 0

# Analyzing the data and updating the initializers--------------------------------------------------------------
        for data in data_as_list:
            total_vehicle += 1

            # To count the vehicle types
            if data[8] == 'Truck':
                total_truck += 1

            if data[9] == "True":
                total_electric_vehicle += 1

            if data[8] in ('Bicycle', 'Motorcycle', 'Scooter'):
                total_two_wheeled += 1

            # Calculating total percentage and average
            if data[8] == 'Truck':
                percentage_of_truck = round((total_truck / total_vehicle) * 100)

            if data[8] == 'Bicycle':
                total_bicycle += 1
                average_bicycle_per_hour = round(total_bicycle / 24)

            # To count the buses
            if data[0] == 'Elm Avenue/Rabbit Road':
                vehicles_passing_through_ElmAvenue_RabbitRoad += 1

            if data[4] == 'N' and data[0] == 'Elm Avenue/Rabbit Road'and data[8] == 'Buss' :
                buses_heading_north += 1

            if data[3] == data[4]:
                buses_heading_straight += 1
                
            #Calculating data pasing through a certain junction
            if data[0] == 'Hanley Highway/Westway':
                vehicles_passing_through_HanleyHighway_Westway += 1

            # Count the speed limit violations by the vehicles
            # Convert vehicle speed to float and Convert speed limit to float
            vehicle_speed = float(data[7])  
            speed_limit = float(data[6])     
            if vehicle_speed > speed_limit:
                        vehicles_over_the_speed_limit += 1

            # Count scooters at Elm Avenue/Rabbit Road and find the  percentage
            if data[0] == 'Elm Avenue/Rabbit Road' and data[8] == 'Scooter':
                number_of_scooters_ElmAvenue_RabbitRoad += 1

            percentage_of_scooters_ElmAvenue_RabbitRoad = round(
                    (number_of_scooters_ElmAvenue_RabbitRoad / vehicles_passing_through_ElmAvenue_RabbitRoad) * 100
                )

            # Updating vehicle count per hour for each junction
            junction = data[0]
            # Extracting the hour from the timestamp
            hour = data[2][0:2] 
            if junction in vehicle_count_per_hour:
                if hour not in vehicle_count_per_hour[junction]:
                    vehicle_count_per_hour[junction][hour] = 0
                vehicle_count_per_hour[junction][hour] += 1

        # Calculating the peak hour vehicle count as it takes the highest from vehicle count per hour
        number_of_vehicles_peak_hour = max(
            max(junction_data.values(), default=0) 
            for junction_data in vehicle_count_per_hour.values()
        )
        # Calculating the peak hour vehicle count and identifying peak hours for Hanley Highway/Westway
        hanley_junction_hours = vehicle_count_per_hour["Hanley Highway/Westway"]
        max_vehicle_count = max(hanley_junction_hours.values(), default=0)

        ## Identifying all the peak hours with the maximum vehicle count for Hanley Highway/Westway
        peak_hours_hanley = [
            f"Between {hour}:00 and {int(hour)+1:02d}:00" 
            for hour, count in hanley_junction_hours.items() 
            if count == max_vehicle_count
        ]
        # Total rainy hours
        for data in data_as_list:
            if data[5] in ['Light Rain', 'Heavy Rain']:
                number_of_hours_rained += 1

# Initialize results list correctly----------------------------------------------------------------------------- 
    try:
        results = []
        results.extend([
            f"The total number of vehicles is: {total_vehicle}",
            f"The total number of trucks recorded for this date is: {total_truck}",
            f"The total number of electric vehicles for this date is: {total_electric_vehicle}",
            f"The total number of two-wheeled vehicles for this date is: {total_two_wheeled}",
            f"The total number of buses leaving Elm Avenue/Rabbit Road heading north is: {buses_heading_north}",
            f"The total vehicles through both junctions (not turning left or right): {buses_heading_straight}",
            f"The percentage of total vehicles recorded that are trucks for this date is: {percentage_of_truck}%",
            f"The average number of bikes per hour for this date is: {average_bicycle_per_hour}",
            f"The total number of vehicles recorded as over the speed limit for this date is: {vehicles_over_the_speed_limit}",
            f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is: {vehicles_passing_through_ElmAvenue_RabbitRoad}",
            f"The total number of vehicles recorded through Hanley Highway/Westway junction is: {vehicles_passing_through_HanleyHighway_Westway}",
            f"{percentage_of_scooters_ElmAvenue_RabbitRoad}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters",
            f"The highest number of vehicles in an hour: {number_of_vehicles_peak_hour}",
            f"Peak traffic hour(s) for Hanley Highway/Westway: {', '.join(peak_hours_hanley)}",
            f"The number of hours of rain for this date is: {number_of_hours_rained}"
        ])

        # To return the results we got and the vehicle count per hour
        return results, vehicle_count_per_hour
    except Exception as e:
            print(f"An error occurred while generating results: {e}")
            # Return empty results and vehicle count if an error occurs 
            return [], {}  


# Saving the list of results to a specified text file------------------------------------------------------------
def save_results_to_file(results):
    try:
        with open('results.txt', 'a') as file:
            for result in results:
                file.write(result + "\n")
    except Exception as e:
       print(f"Error writing to file: {e}")

#Creating a function for the histogram---------------------------------------------------------------------------
def create_histogram(vehicle_count_per_hour, date):
    # Create the graphics window
    win = GraphWin(f"Histogram of Vehicle Frequency per Hour ({date})", 1200, 600)
    win.setBackground("lightgray")

    #Setting up the axis dimensions
    x_start, y_start = 100, 500  # Bottom-left corner of the axis
    x_end, y_end = 1100, 100  # Top-right corner of the axis
    bar_width = 15  # Width of each bar
    bar_gap = 10  # Gap between bars
    y_axis_height = y_start - y_end
    x_axis_width = x_end - x_start

    #Defining the colors
    elm_color = "black"
    hanley_color = "brown"

    #Extracting the data 
    hours = [f"{hour:02d}" for hour in range(24)]  # List of hour strings (00 to 23)
    elm_counts = [vehicle_count_per_hour["Elm Avenue/Rabbit Road"].get(hour, 0) for hour in hours]
    hanley_counts = [vehicle_count_per_hour["Hanley Highway/Westway"].get(hour, 0) for hour in hours]

    #Find maximum count for scaling
    max_count = max(max(elm_counts), max(hanley_counts), 1) #Avoid division by zero

    #Scale factor for bars to fit in the y-axis
    scale_factor = y_axis_height / max_count

    #Draw the axes
    Line(Point(x_start, y_start), Point(x_end, y_start)).draw(win) #X-axis
    Line(Point(x_start, y_start), Point(x_start, y_end)).draw(win) #Y-axis

    #Draw axis labels and ticks
    for i, hour in enumerate(hours):
        x_pos = x_start + i * (2 * bar_width + bar_gap)
        label = Text(Point(x_pos + bar_width / 2, y_start + 20), hour) #Hour labels
        label.setSize(8)
        label.draw(win)
    
    for i in range(0, max_count + 1, max(1, max_count // 10)):
        y_pos = y_start - i * scale_factor
        label = Text(Point(x_start - 20, y_pos), str(i)) #Count labels
        label.setSize(8)
        label.draw(win)

    #Drawing bars
    for i, hour in enumerate(hours):
        x_pos = x_start + i * (2 * bar_width + bar_gap)

        #Elm Avenue/Rabbit Road bar
        elm_height = elm_counts[i] * scale_factor
        elm_bar = Rectangle(
            Point(x_pos, y_start), Point(x_pos + bar_width, y_start - elm_height)
        )
        elm_bar.setFill(elm_color)
        elm_bar.setOutline(elm_color)
        elm_bar.draw(win)
        elm_label = Text(Point(x_pos + bar_width / 2, y_start - elm_height - 10), str(elm_counts[i]))
        elm_label.setSize(8)
        elm_label.draw(win)
        # Hanley Highway/Westway bar
        hanley_height = hanley_counts[i] * scale_factor
        hanley_bar = Rectangle(
            Point(x_pos + bar_width, y_start), Point(x_pos + 2 * bar_width, y_start - hanley_height)
        )
        hanley_bar.setFill(hanley_color)
        hanley_bar.setOutline(hanley_color)
        hanley_bar.draw(win)
        hanley_label = Text(Point(x_pos + 1.5 * bar_width, y_start - hanley_height - 10), str(hanley_counts[i]))
        hanley_label.setSize(8)
        hanley_label.draw(win)


    #Animate the growth of the bars
        for step in range(1, 21): #Increase in 20 steps
            elm_bar.undraw()
            hanley_bar.undraw()

            current_elm_height = elm_height * (step / 20)
            current_hanley_height = hanley_height * (step / 20)

            elm_bar = Rectangle(
                Point(x_pos, y_start), Point(x_pos + bar_width, y_start - current_elm_height)
            )
            hanley_bar = Rectangle(
                Point(x_pos + bar_width, y_start), Point(x_pos + 2 * bar_width, y_start - current_hanley_height)
            )

            elm_bar.setFill(elm_color)
            elm_bar.setOutline(elm_color)
            hanley_bar.setFill(hanley_color)
            hanley_bar.setOutline(hanley_color)

            elm_bar.draw(win)
            hanley_bar.draw(win)
            #Delay for smooth animation
            time.sleep(0.01) 

        #Add labels after animation
        elm_label = Text(Point(x_pos + bar_width / 2, y_start - elm_height - 10), str(elm_counts[i]))
        elm_label.setSize(8)
        elm_label.draw(win)

        hanley_label = Text(Point(x_pos + 1.5 * bar_width, y_start - hanley_height - 10), str(hanley_counts[i]))
        hanley_label.setSize(8)
        hanley_label.draw(win)

    #Draw title and legend
    title = Text(Point((x_start + x_end) / 2, y_end - 30), f"Histogram of Vehicle Frequency per Hour ({date})")
    title.setSize(14)
    title.setStyle("bold")
    title.draw(win)

    legend_elm = Text(Point(x_end - 50, y_end + 20), "Elm Avenue/Rabbit Road")
    legend_elm.setSize(10)
    legend_elm.setTextColor(elm_color)
    legend_elm.draw(win)

    legend_hanley = Text(Point(x_end - 50, y_end + 40), "Hanley Highway/Westway")
    legend_hanley.setSize(10)
    legend_hanley.setTextColor(hanley_color)
    legend_hanley.draw(win)

    #Add label below the graph (Hours)
    hours_label = Text(Point((x_start + x_end) / 2, y_start + 40), "Hours (00:00 to 24:00)")
    hours_label.setSize(12)
    hours_label.setStyle("bold")
    hours_label.draw(win)

    #Wait for user to close
    win.getMouse()
    win.close()

#Calls for main function----------------------------------------------------------------------------------------
def main():
    while True:
        try:
            date = get_date()
            print(f"The data file selected is traffic_data{date}.csv")
            filename = f"traffic_data{date}.csv"
            results, vehicle_count_per_hour = analyze_the_data(filename)
            #save results to file
            print("\n".join(results))
            save_results_to_file(results)  
            create_histogram(vehicle_count_per_hour, date)

        # Exit the program on keyboard interrupt
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break
        # Handles any unexpected errors, such as missing file ot data format issues
        except Exception as E:
            print(f"An error occurred: {E}")

#Ask user again if user wants to enter another date-------------------------------------------------------------------
        do_it_again = input("Do you want to select another data file for a different date? (Y/N): ").strip().lower()

        if do_it_again != 'y':
            print("The program was exited")
            break

#Ensuring blocks of code only run when 'main' is called directly, not imported elsewhere as a module.
if __name__ == "__main__":
    main()