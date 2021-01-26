import pandas

sku = [1, 2, 3]
name = ["Hammer", "Screwdriver", "Drill"]
inventory = [10, 1, 2]

df = pandas.DataFrame(list(zip(sku, name, inventory)), columns = ['SKU', 'Name', 'Inventory'])

total_items = df['Inventory'].sum()
print(f"Total number of items in warehouse: {total_items}")