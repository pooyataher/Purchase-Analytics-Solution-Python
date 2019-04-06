
def check_num_args(args):
    if len(args) != 3:
        raise ValueError('At least one of three required input arguments is\
        missing.')
