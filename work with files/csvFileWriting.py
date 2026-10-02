import csv
path = "output.csv"
data = [["Name","age","role"],
        ["Nani",20,"Student"],
        ["Maha",25,"IAS"],
        ["Nagur",30,"IPS"]]


with open (path,"w",newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
    print("Successfully updated")