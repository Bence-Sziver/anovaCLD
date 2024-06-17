from compactletterdisplay.pairwise_comp import anova_cld
import csv

def transpone(lines):
    newLines = []
    for i in range(len(lines[0])):
        row =[]
        for line in lines:
            row.append(line[i])
        newLines.append(row)
    return newLines

with open('data.txt', 'r') as in_file:
    stripped = list((line.strip() for line in in_file))
    print(stripped)
    headers = list(line.split(",")[0] for line in stripped if line)
    print(headers)
    lines = list(line.split(",")[1:] for line in stripped if line)
    print(lines)
    with open('data.csv', 'w+') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(headers)
        writer.writerows(transpone(lines))

filepath = "data.csv"
alpha = 0.05

result_df = anova_cld(filepath, alpha=alpha, method="FisherLSD", verbose = True)

print(result_df)

list_of_cld = result_df['CLD'].tolist()

print(list_of_cld)