def dict2csv(dictionary, csv_file, separator=';'):
    """
    Transform a double dictionary (dict of same type dictionaries) in a CSV file.
    Each line corresponds to an entity from the primary dictionary (with key in first position)
    Each column corresponds to each keys of the secondary dictionaries

    :param dictionary: double dictionary to be exported
    :param csv_file: path of output csv file
    :param separator: csv separator ';' (default value) or ','
    :return: No return, only create a csv file
    """

    with open(csv_file, "w") as file:
        headerLine = dict2header(list(dictionary.values())[0], separator)

        file.write(headerLine)

        for primaryKey in dictionary:
            newLine = dict2line(dictionary[primaryKey], primaryKey, separator)
            file.write(newLine)


def csv2dict(csv_file, separator=";"):
    """
    Read a csv file and import it in a double dictionary (dict of same type dictionaries)
    The first line is interpreted as secondary keys
    The first column is interpreted as primary keys

    :param csv_file: path of input csv file
    :param separator: csv separator ';' (default value) or ','
    :return: double dictionary containing data from input csv file
    """

    dictionary = {}

    with open(csv_file, "r") as file:
        headerLine = file.readline().split(separator)
        headerLine[-1] = headerLine[-1][:-1]
        nb_col = len(headerLine)

        while True:
            newLine = file.readline()
            if not newLine:
                break
            dataLine = newLine[:-1].split(separator)

            dictionary[dataLine[0]] = {}
            for i in range(1, nb_col):
                dictionary[dataLine[0]][headerLine[i]] = dataLine[i]

    return dictionary


def dict2header(dictionary, separator=";"):
    """
    Serialize the keys of a dictionary with a str separator in order to create the header line of a csv file
    A blank cells is let at the beginning to handle the first column of the csv file containing the primary keys
    :param dictionary: input secondary dictionary of a double dictionary
    :param separator: csv separator ';' (default value) or ','
    :return:  string line containing the serialized header of an input dictionary
    """

    newHeaderLine = separator
    newHeaderLine += separator.join(dictionary)
    newHeaderLine += '\n'
    return newHeaderLine


def dict2line(dictionary, dict_name, separator=";"):
    """
    Serialize dictionary into a string line using separator
    The line starts by the title given in input
    :param dictionary: dictionary to be serialized
    :param dict_name: name of the dictionary to be serialized
    :param separator: csv separator ';' (default value) or ','
    :return: string line containing the serialized input dictionary
    """

    newDataLine = dict_name
    for key in dictionary:
        newDataLine += separator + str(dictionary[key])
    newDataLine += '\n'
    return newDataLine


if __name__ == '__main__':
    """
    Example of use
    """

    input_dictionary = {'A': {'X': 1, 'Y': 8, 'Z': 4}, 'B': {'X': 2, 'Y': 6, 'Z': 2}, 'C': {'X': 7, 'Y': 7, 'Z': 7},
                        'D': {'X': 4, 'Y': 0, 'Z': 2}}

    dict2csv(input_dictionary, 'test.csv')
    output_dictionary = csv2dict('test.csv', )

    print(output_dictionary)
