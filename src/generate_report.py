# For each row in order_products table:
#     Read the prod_id and `reordered` value
#     In products table, find the dept_id associated with the prod_id
#     In report table, find the row associated with the dept_id
#         If dept_id exists, just increment number_of_orders
#         Otherwise, create a row for it and set number_of_orders to 1
#         If `reordered` is 0
#             Increment number_of_first_orders
# Compute ratio for each row in report table
# Sort report table based on dept_id


from optparse import OptionParser
import products
import checks
import csv

parser = OptionParser()
(options, args) = parser.parse_args()
checks.check_num_args(args)
order_prod_filename, prod_filename, report_filename = args

# load products table
# try:
prod_table = products.load_prod_table(prod_filename)
# except TypeError:

report_table = {}
num_removed_lines = 0

with open(order_prod_filename, newline='') as ord_file:
    ord_file = products.remove_header(ord_file)
    ord_table = csv.reader(ord_file)
    for row in ord_table:
        prod_id = row[1]
        reordered = row[3]
        dept_id = int(prod_table[prod_id])

        if reordered != '0' and reordered != '1':
            num_removed_lines += 1
            continue

        # Two lookups in the dictionary for each key
        if dept_id in report_table:  # first lookup for all cases
            dept_spec = report_table[dept_id]  # second lookup
            dept_spec[0] += 1
        else:
            dept_spec = [1, 0, 0.0]
            report_table[dept_id] = dept_spec  # second lookup

        if reordered == '0':
            dept_spec[1] += 1

with open(report_filename, 'w') as report:
    report.write('department_id,number_of_orders,\
number_of_first_orders,percentage\n')
    for key in sorted(report_table):
        dept_row = report_table[key]
        num_orders, num_first_orders = dept_row[0], dept_row[1]
        percent = num_first_orders / num_orders
        report.write(str(key) + ',' + str(num_orders) + ',' +
                     str(num_first_orders) + ',' + format(percent, '.2f') +
                     '\n')

print(num_removed_lines, 'lines removed from order_products table.')
