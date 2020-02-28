import mysql.connector
import os
import re
import antlr4
from sql_parser.SqlBaseLexer import SqlBaseLexer
from sql_parser.SqlBaseParser import SqlBaseParser
import pandas as pd

CHECK_FOR_VALID_SQL = False
LIMIT = 0
MIN_QUERY_LENGTH = 20

if __name__ == '__main__':

    parsingErrorFlag = False

    def tokenToText(t):
        if t.type in [207, 208]:
            return ''
        if t.type == 209:
            return ' '
        return t.text

    class CustomErrorListener:
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            global parsingErrorFlag
            parsingErrorFlag = True

        def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
            pass

        def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
            pass

        def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
            pass


    customErrorListener = CustomErrorListener()

    mysql_psss = os.environ['MYSQL_PASS']
    cnx = mysql.connector.connect(user='aviad', password=mysql_psss,
                                  host='127.0.0.1',
                                  database='quix')
    cursor = cnx.cursor()
    cursor.execute("select text,dateUpdated,dateCreated from dataset" + (f"limit {LIMIT}" if LIMIT else ""))
    re1 = re.compile('\'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\'')

    counter = 0
    success_counter = 0
    error_counter = 0

    rows = []
    for (text, dateUpdated, dateCreated) in cursor:
        if counter % 200 == 0:
            print(f'processing row {counter}. success: {success_counter}, error: {error_counter}')
        counter += 1
        s: str = text[1:-1].lower().replace('\\r\\n', '\n').replace('\\n', '\n').replace('\\t', '\t')
        s = re1.sub("'GUID'", s)

        # using tokeninzer to remove string
        input_stream = antlr4.InputStream(s)
        lex = SqlBaseLexer(input_stream)
        tokens = lex.getAllTokens()
        newText = ''.join([tokenToText(t) for t in tokens])
        newText = newText.lstrip()

        if len(newText) > MIN_QUERY_LENGTH:
            # print(text)
            # print(newText)
            # print(dateCreated)
            if CHECK_FOR_VALID_SQL:
                input_stream = antlr4.InputStream(newText)
                lex = SqlBaseLexer(input_stream)
                token_stream = antlr4.CommonTokenStream(lex)
                parser = SqlBaseParser(token_stream)
                parser.addErrorListener(customErrorListener)
                parsingErrorFlag = False
                parser.multiStatement()

            if not parsingErrorFlag:
                rows.append((newText, int(dateCreated), int(dateUpdated)))
                success_counter += 1
            else:
                error_counter += 1

    sql_data = pd.DataFrame(rows)
    sql_data.columns = cursor.column_names

    cursor.close()
    cnx.close()
    sql_data.to_csv('dataset.csv', escapechar='\\')
