import matplotlib.pyplot as plt
import csv

#***Note: In order to use this code, all of the columns in the .csv file must have the same length. If your columns have
# different lengths, simply repeat the last value in each of the shorter columns until they are all the same size.

#Initialize arrays for x, y1, y2, y3
x = []
y1 = []
y2 = []
#y3 = []

##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('Thru-S21_Phase.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq [GHz]']!="END":
			x.append(float(row['Freq [GHz]'])*1e9)
			y1.append(float(row['deg(S(2,1))'])-180)#Adjusted Phase
#        	y2.append(float(row['y2']))
#        	y3.append(float(row['y3']))

#File 2#####################################################################
##Read .csv data file
#replace quoted text below with filepath to your .csv file
with open('S21_Thru_Phase.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
        #items in '' below need to exactly match the entry in the first row of the columns in the .csv file
        #edit/add additional lines as needed for each column of data
		if row['Freq(Hz)']!="END":
			y2.append(float(row['S21 Phase(deg)']))
#        	y2.append(float(row['y2']))



##Plotting
plt.figure(1) #initialize plot1
ax1 = plt.subplot(111) #create axes handle for plot1
ax1.plot(x, y1, '-b', label="Simulated") #plot y1 vs. x, solid-blue, add lable for legend

ax1.plot(x, y2, '-r', label="Measured") #plot y2 vs. x, solid-red, add lable for legend
#ax1.plot(x, y3, '--r', label="y3 Data") #plot y3 vs. x, dashed-red, add lable for legend

#ax2=ax1.twinx()

ax1.set_xlim(min(x), max(x)) #set x-axis limits
ax1.legend(loc=4) #add legend at location #4 (bottom-right corner)
ax1.set_ylim(-5,5)#Force y axis limits if necessary

plt.grid(b=True, which='both', color='0.65', linestyle='-') #add solid grey gridlines
plt.title('Thru S21 Phase') #add plot title
plt.xlabel('Frequency [GHz]') #add x-axis title

ax1.set_ylabel('S21 Phase [deg]') #add y-axis title
#ax2.set_ylabel('S21 Magnitude [dB]')
plt.show() #required to display plots
