
import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

def main(filename, filename_new):
    data = read_csv_to_dict(filename)
    data_new = read_csv_to_dict(filename_new)
    #itera lista batch
    for row_new in data_new:
        found = False
        #itera lista original
        for row in data:
            #coincidencia, suma cantidades
            if row['SKU'] == row_new['SKU']:
                row['Quantity'] = int(row['Quantity']) + int(row_new['Quantity'])
                found = True
                break
        #sin coincidencia, agrega
        if not found:
            data.append(row_new)
    #guardar en archivo
    write_list_of_dicts_to_csv('grocery_db.csv', data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('sample_grocery.csv', 'grocery_batch_1.csv')
