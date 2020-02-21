from collections import namedtuple
import argparse

FP = namedtuple('FP', 'e, m')
            
def significand(frac_field):
    return int(frac_field, 2) / (2**len(frac_field))

def exponent(exp_field):
    return int(exp_field, 2)

def exponent_bias(e):
    return 2 ** (e - 1) - 1

def zero(fp):
    exp_field  = '0' * fp.e
    exp_bias   = exponent_bias(fp.e)
    frac_field = '0' * fp.m

    M = significand(frac_field)
    E = 1 - exp_bias

    return M * (2 ** E)

def min_denorm(fp):
    exp_field  = '0' * fp.e
    exp_bias   = exponent_bias(fp.e)
    frac_field = '0' * (fp.m - 1) + '1'

    M = significand(frac_field)
    E = 1 - exp_bias

    return M * (2 ** E)
    

def max_denorm(fp):
    exp_field  = '0' * fp.e
    exp_bias   = exponent_bias(fp.e)
    frac_field = '1' * (fp.m)

    M = significand(frac_field)
    E = 1 - exp_bias

    return M * (2 ** E)

def min_norm(fp):
    exp_field  = '0' * (fp.e - 1) + '1'
    exp_bias   = exponent_bias(fp.e)
    frac_field = '0' * fp.m

    M = 1 + significand(frac_field) # implicit leading 1
    E = exponent(exp_field) - exp_bias

    return M * (2 ** E)
    

def one(fp):
    exp_field  = '0' + '1' * (fp.e - 1) # The unsigned exp that exp_field represented exactly equals the exp_bias
    exp_bias   = exponent_bias(fp.e)
    frac_field = '0' * fp.m

    M = 1 + significand(frac_field)    # implicit leading 1
    E = exponent(exp_field) - exp_bias

    return M * (2 ** E)

def max_norm(fp):
    exp_field  = '1' * (fp.e - 1) + '0'
    exp_bias   = exponent_bias(fp.e)
    frac_field = '1' * fp.m

    M = 1 + significand(frac_field)    # implicit leading 1
    E = exponent(exp_field) - exp_bias

    return M * (2 ** E)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', required=True, type=int)
    parser.add_argument('-m', required=True, type=int)

    args = parser.parse_args()
    fp = FP(args.e, args.m)
    
    # print(zero(fp))
    print("{:.2e}".format(min_denorm(fp)))
    print("{:.2e}".format(max_denorm(fp)))
    print("{:.2e}".format(min_norm(fp)))
    # print(one(fp))
    print("{:.2e}".format(max_norm(fp)))
    
