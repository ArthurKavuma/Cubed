import csv
my_list= [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open('my_list.csv', 'w',newline='') as csvfile:
    new_list = csv.writer(csvfile, delimiter=',')
    new_list.writerows(my_list)


