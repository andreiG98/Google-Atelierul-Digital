
def sum_numbers(*args, **kwargs):

    numbers = [param for param in args if str(param).lstrip("-").isdigit()]

    return sum(numbers)


def recursive_function(numbers_list):

    if len(numbers_list) == 0:

        return {
            'sum': 0,
            'even_sum': 0,
            'odd_sum': 0
        }

    return {
        'sum': numbers_list[0] + recursive_function(numbers_list=numbers_list[1:])['sum'],
        'even_sum': numbers_list[0] + recursive_function(numbers_list=numbers_list[1:])['even_sum'] if numbers_list[0] % 2 == 0 else recursive_function(numbers_list=numbers_list[1:])['even_sum'],
        'odd_sum': numbers_list[0] + recursive_function(numbers_list=numbers_list[1:])['odd_sum'] if numbers_list[0] % 2 != 0 else recursive_function(numbers_list=numbers_list[1:])['odd_sum']
    }

def is_int_number():

    number = float(input("Write the value: "))

    if int(number) == number:

        return number

    return 0

if __name__=="__main__":
    print(sum_numbers(1, 5, -3, "abc", [12, 56, "cad"]))
    print(sum_numbers())
    print(sum_numbers(2, 4, "abc", param_1=2))
    print(f"{'*' * 10}\n")

    print(recursive_function(numbers_list=[1, 2, 3, 4, 5]))
    print(f"{'*' * 10}\n")
    
    print(is_int_number())