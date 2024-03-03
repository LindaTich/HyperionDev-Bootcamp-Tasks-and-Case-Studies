'''Start
Create a file named Iteration Physics Experiment.
Save it as python in VS Code.
Create a dictionary called locations with key values.
Create variable locations to store both keys.
Create a variable called levels to store the values.
Create a for loop to calculate average radiation level per location.
Use enumerate function as a counter for list.
Create measurements variable and initialise it.
Use while loop and break when requested info entered stops.
Use try and except ValueError in while loop.
Use print function to output.
End'''

locations = {
   'Urban': [26, 39, 43],
   'Forest': [37, 51, 69]
}

locations = ["Urban", "Forest"]

levels = [[26, 39, 43],[37, 51, 69]]

for i, location in enumerate(locations):
    print(f"Debug: Processing  location {location} with levels{levels[i]}")
    average = sum(levels[i]) / len(levels[i])
    print(f"{location} Average Radiation Level :{average}")

measurements = []

print("Begin entering the new radiation levels. Type 'done' to finish.")

while True:
    level = input("Enter radiation level or 'done' to finish: ")
    if level.lower() == 'done':
        print(f"Debug: Exiting input loop.")
        break
    try:
        new_level = int(level)
        measurements.append(new_level)
        print("Debug: Added level {new_level}")
    except ValueError:
        print("invalid input. Please enter a valid number or 'done'.")

if measurements:
      average = sum(measurements) / len(measurements)
      print(f"New Measurements Average Radiation Level: (average)")
else:
      print("Debug : No new measurements were entered.")





