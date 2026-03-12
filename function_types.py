def calc_avg(data):
    return sum(data) / len(data)


def list_shift(data, shift):
    for i in range(len(data)):
        data[i] += shift


def print_normalized(data):
    avg = calc_avg(data)
    list_shift(data, -avg)
    print(data)