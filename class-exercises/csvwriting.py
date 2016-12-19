import csv

csvfile = open("csvfile.csv", "w")

csvwriter = csv.writer(csvfile, delimiter = ",")

csvwriter.writerow(["1", "2", "3", "4", "5"])
csvwriter.writerow(["10", "20", "30", "40", "50"])
csvwriter.writerow(["15", "25", "35", "45", "55"])

csvfile.close()