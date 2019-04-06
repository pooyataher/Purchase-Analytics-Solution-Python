
# For each row in order-products table:
#     Read the product-id and `reordered` value
#     In products table, find the department-id associated with the product-id
#     In report table, find the row associated with the department-id
#         If department-id doesn't exist, create a row for it
#         Increment number-of-orders
#         If `reordered` is 0
#             Increment number-of-first-orders
# Compute ratio for each row in report table
# Sort report table based on department-id


from optparse import OptionParser

parser = OptionParser()
(options, args) = parser.parse_args()
check_num_args(args)

# print('first argument:', args[0])

# # open order_products.csv
