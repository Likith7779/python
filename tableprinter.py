print('Name:Likith raj,USN:1AY24AI061')
#table printer.py
def print_table(table_data):
#find the maximum width of each column
col_widths=[max(len(str(item))
for item in col) for col in zip(*table_data)]
#print each row in aligned columns for row in table_data:
for i,item in enumerate(row): print(str(item).rjust(col_widths[i]), end=' ')
print() table=[["name", "age", "city"], ["BhuVee", 23, "Bengaluru"], ["Luciffer", 20, "Bengaluru"], ["Charlie", 18, "Bengaluru"] ] 
print_table(table)
