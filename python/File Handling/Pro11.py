# CSV : comma separate values

import csv

with open("mycsvfile.csv","w") as file:
    writer = csv.writer(file)

    writer.writerow(["id","name","subject","city"])
    writer.writerow([1,"Kumkum","python","ahm"])

