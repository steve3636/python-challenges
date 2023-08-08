import csv

def analyze_budget_data(csv_file):
    with open(csv_file, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = list(csv_reader)

    total_months = len(data)
    net_total = sum(int(row['Profit/Losses']) for row in data)

    profit_loss_changes = [int(data[i]['Profit/Losses']) - int(data[i-1]['Profit/Losses'])
                           for i in range(1, total_months)]

    average_change = sum(profit_loss_changes) / len(profit_loss_changes)

    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)

    greatest_increase_date = data[profit_loss_changes.index(greatest_increase) + 1]['Date']
    greatest_decrease_date = data[profit_loss_changes.index(greatest_decrease) + 1]['Date']

    return total_months, net_total, average_change, {"date": greatest_increase_date, "$": greatest_increase}, {"date": greatest_decrease_date, "$": greatest_decrease}

csv_file_path = 'budget_data.csv'
total_months, net_total, average_change, greatest_increase, greatest_decrease = analyze_budget_data(csv_file_path)

# Write a text file
output_file_path = 'budget_data_output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("The total number of months included in the dataset: {}\n".format(total_months))
    output_file.write("The final net total $ of 'Profit/Losses': ${:.2f}\n".format(net_total))
    output_file.write("The average of the changes: {}\n".format(average_change))
    output_file.write("The greatest increase in profits (date and $): {} ${:.2f}\n".format(greatest_increase["date"], greatest_increase["$"]))
    output_file.write("The greatest decrease in profits (date and $): {} ${:.2f}\n".format(greatest_decrease["date"], greatest_decrease["$"]))

print("Election Result")
print("___________________________________")
print("Total number of months included in the dataset:", total_months)
print("The final net total $ of 'Profit/Losses': ${:.2f}".format(net_total))
print("The average of the changes:", average_change)
print("The greatest increase in profits (date and $):", greatest_increase["date"], "${:.2f}".format(greatest_increase["$"]))
print("The greatest decrease in profits (date and $):", greatest_decrease["date"], "${:.2f}".format(greatest_decrease["$"]))
print("___________________________________")
print("Output written to", output_file_path)




  