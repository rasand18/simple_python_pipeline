def bin_number_to_tens(input_value: float) -> str:
    if input_value < 0:
        raise NotImplementedError("Not implemented for values below zero!")
    elif input_value < 10:
        return "[0-10)"
    elif input_value < 20:
        return "[10-20)"
    elif input_value < 30:
        return "[20-30)"
    else:
        raise NotImplementedError("Not implemented for values above 30!")
