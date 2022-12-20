def split_smart(string, separator):
    """
    Default split function does not split by empty string.
    This function executes string.split('') without throwing an error.
    :param string: any string
    :param separator: any string
    :return: given string split by given separator
    """
    if separator == '':
        return [*string]
    else:
        return string.split(separator)


def read(filename, separator=None, formatter=None):
    lines = open(filename, 'r')
    if separator is None:
        return [int(line.strip()) if formatter == 'i' else line.strip() for line in lines]
    elif formatter is None:
        return [split_smart(line.strip(), separator) for line in lines]
    else:
        return [
            [
                int(token) if formatter[index] == 'i' else token
                for index, token
                in enumerate(split_smart(line.strip(), separator))
            ]
            for line
            in lines
        ]
