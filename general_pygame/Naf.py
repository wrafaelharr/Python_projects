import csv

#stuff
x = "I fuck with the fit"

# open the file in the write mode
f = open('path/to/csv_file', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(row)

# close the file
f.close()