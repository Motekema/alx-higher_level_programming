st_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] != 0:
                    quotient = my_list_1[i] / my_list_2[i]
                else:
                    raise ZeroDivisionError
            else:
                raise TypeError("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError as e:
            print(e)
        finally:
            result.append(quotient)
    return (result)
