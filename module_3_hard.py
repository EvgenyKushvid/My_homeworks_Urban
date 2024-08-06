data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]


def calculate_data_sum (*args):
    total_sum = 0

    for arg in args:
        if isinstance(arg, (int, float)):
            total_sum += arg
        elif isinstance(arg,str):
            total_sum += len(arg)
        elif isinstance(arg, (list, set, tuple)):
            total_sum += calculate_data_sum(*arg)
        elif isinstance(arg, dict):
            total_sum += calculate_data_sum(*arg.items())




    return total_sum




print(f' и вот что получилось :{calculate_data_sum(data_structure)}')