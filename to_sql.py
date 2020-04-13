import pdb
import json


def read_coeffs(coeffs_dict_file):
    file = open(coeffs_dict_file, "rb")
    coeffs = json.load(file)

    return coeffs


def to_sql():
    coefficients_dict = read_coeffs('coefficients_dict.json')

    query = """DROP TABLE IF EXISTS TMP_1;\nCREATE TABLE TMP_1 AS\nSELECT DF.*,\n"""

    for key in coefficients_dict.keys():
        for element in coefficients_dict[key]:
            if element == 'intercept':
                query += "  " + str(round(coefficients_dict[key][element], 4)) + " AS `linear`\n"
            else:
                query += "  `" + element + '` * ' + str(round(coefficients_dict[key][element], 4)) + " +\n"
        query += "FROM DF;\n\n"

    text_file = open("ca_query.sql", "a")
    n = text_file.write(query)
    text_file.close()

    query = """DROP TABLE IF EXISTS TMP_2;\nCREATE TABLE TMP_2 AS\nSELECT TMP_1.*,
  1 / (1 + exp(-1 * `linear`)) AS `probability`\nFROM TMP_1;\n\n"""

    text_file = open("ca_query.sql", "a")
    n = text_file.write(query)
    text_file.close()

to_sql()