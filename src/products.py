# Utilities for loading CSV files

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


def load_csv(fname, left, right):
    """Assumes fname is a CSV file name, left is index of first field of
    interest, and right is the second filed of interest
    Returns a dictionary of product_id: dept_id pairs
    Be careful not to mutate the dictionary returned by this method"""
    # Notice that str keys are the fastest, according to Python wiki:
    # https://wiki.python.org/moin/TimeComplexity
    depts = {}
    with open(fname, newline='') as csvfile:
        csvfile = remove_header(csvfile)
        prod_reader = csv.reader(csvfile)
        for row in prod_reader:
            depts[row[left]] = row[right]  # str keys are the fastest
        if depts == {}:
            raise ValueError('The file is either empty or not in CSV format: '
                             + fname)
    return depts


def load_prod_table(csv_fname):
    """wrapper function for load_csv when reading the product.csv"""
    left_col, right_col = 0, 3
    return load_csv(csv_fname, left_col, right_col)
