import matplotlib.pyplot as plt
import csv

# Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

# Initialize arrays for x, y1, y2, y3
x = []
y1 = []
y2 = []
y3 = []

# Read .csv data file
# replace quoted text below with filepath to your .csv file
with open('S21_dB.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        # edit/add additional lines as needed for each column of data
        x.append(float(row['Freq [GHz]']))
        y1.append(float(row['S21_Analytical']))
        y2.append(float(row['S21_HFSS']))
        y3.append(float(row['S21_Z0lver']))

# Plotting
plt.figure(1)  # initialize plot1
ax1 = plt.subplot(111)  # create axes handle for plot1
ax1.plot(x, y1, '-b', label="S21 Analytical")  # plot y1 vs. x, solid-blue, add label for legend
ax1.plot(x, y2, '-r', label="S21 HFSS")  # plot y2 vs. x, solid-red, add label for legend
ax1.plot(x, y3, '--r', label="S21 Z0lver")  # plot y3 vs. x, dashed-red, add label for legend
ax1.set_xlim(min(x), max(x))  # set x-axis limits
ax1.set_ylim(-5, 0)  # set x-axis limits
ax1.legend(loc=4)  # add legend at location #4 (bottom-right corner)
plt.grid(b=True, which='both', color='0.65', linestyle='-')  # add solid grey grid-lines
plt.title('Comparison of S21')  # add plot title
plt.xlabel('Freq [GHz]')  # add x-axis title
plt.ylabel('dB')  # add y-axis title

plt.show()  # required to display plots
