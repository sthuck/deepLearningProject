import pandas as pd
import mysql.connector
import os
import re
import antlr4
from sql_parser.SqlBaseLexer import SqlBaseLexer
import pandas as pd

if __name__ == '__main__':

    def tokenToText(t):
        if t.type in [207, 208]:
            return ''
        if t.type == 209:
            return ' '
        return t.text

    mysql_psss = os.environ['MYSQL_PASS']
    cnx = mysql.connector.connect(user='aviad', password=mysql_psss,
                                  host='127.0.0.1',
                                  database='quix')
    cursor = cnx.cursor()
    cursor.execute("select text,dateUpdated,dateCreated from dataset")
    re1 = re.compile('^"')
    re2 = re.compile('"$')

    rows = []
    for (text, dateUpdated, dateCreated) in cursor:
        s: str = text[1:-1].lower().replace('\\n', '\n')

        input_stream = antlr4.InputStream(s)
        lex = SqlBaseLexer(input_stream)
        tokens = lex.getAllTokens()
        newText = ''.join([tokenToText(t) for t in tokens])
        newText = newText.lstrip()
        if len(newText) > 20:
            rows.append((newText, int(dateCreated), int(dateUpdated)))

    sql_data = pd.DataFrame(rows)
    sql_data.columns = cursor.column_names

    cursor.close()
    cnx.close()
    sql_data.to_csv('dataset.csv', escapechar='\\')

