
def apply_all_func (data, *functions):
    result = {}
    for func in functions:
        if func.__name__ == "min":
            res = min(data)
            result[func.__name__] = res
        elif func.__name__ == "max":
            res = max(data)
            result[func.__name__] = res
        elif func.__name__ == "len":
            res = len(data)
            result[func.__name__] = res
        elif func.__name__ == "sum":
            res = sum(data)
            result[func.__name__] = res
        elif func.__name__ == "sorted":
            res = sorted(data)
            result[func.__name__] = res

    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
