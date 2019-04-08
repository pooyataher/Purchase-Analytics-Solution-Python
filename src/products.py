# Products table module

import csv


def remove_header(csvf):
    """Assumes csvf is a file object representing a CSV file
       Returns the same file object with any possible header removed"""
    if csv.Sniffer().has_header(csvf.read(1024)):
        csvf.seek(0)
        csvf.readline()
    else:
        csvf.seek(0)
    return csvf


class Products(object):
    """Keeps track of product_id and its associated dept_id for a collection
    of products"""
    # Represents a table of products by using a dictionary of
    # product_id: dept_id pairs so that we can find dept_id associated with a
    # particular product_id really fast

    def __init__(self):
        self.products = {}

    def load_products(self, filename):
        """Assumes filename is a CSV file containing a products table
        Returns a dictionary of product_id: dept_id pairs
        Be careful not to mutate the dictionary returned by this method"""
        with open(filename, newline='') as csvfile:
            csvfile = remove_header(csvfile)
            prod_reader = csv.reader(csvfile)
            for row in prod_reader:
                self.products[row[0]] = row[3]
        return self.products
