class Products(object):
    """keeps track of product_id and its associated dept_id for a collection
of products"""

    def __init__(self):
        self.products = {}

    def load_products(self, filename):
        with open('../input/products.csv', 'r') as pfile:
            for line in pfile:
                2
