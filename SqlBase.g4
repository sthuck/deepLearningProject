/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

grammar SqlBase;

tokens {
    DELIMITER
}

multiStatement
    : statement (SEMICOLON statement)* (SEMICOLON)? EOF
    ;

singleStatement
    : statement EOF
    ;

singleExpression
    : expression EOF
    ;

statement
    : query                                                            #statementDefault
    | USE schema=identifier                                            #use
    | USE catalog=identifier '.' schema=identifier                     #use
    | CREATE SCHEMA (IF NOT EXISTS)? qualifiedName
        (WITH tableProperties)?                                        #createSchema
    | DROP SCHEMA (IF EXISTS)? qualifiedName (CASCADE | RESTRICT)?     #dropSchema
    | ALTER SCHEMA qualifiedName RENAME TO identifier                  #renameSchema
    | CREATE TABLE (IF NOT EXISTS)? qualifiedName
        (WITH tableProperties)? AS_ query
        (WITH (NO)? DATA)?                                             #createTableAsSelect
    | CREATE TABLE (IF NOT EXISTS)? qualifiedName
        '(' tableElement (',' tableElement)* ')'
        (WITH tableProperties)?                                        #createTable
    | DROP TABLE (IF EXISTS)? qualifiedName                            #dropTable
    | INSERT INTO qualifiedName columnAliases? query                   #insertInto
    | DELETE FROM_ qualifiedName (WHERE booleanExpression)?             #delete
    | ALTER TABLE from_=qualifiedName RENAME TO to=qualifiedName        #renameTable
    | ALTER TABLE tableName=qualifiedName
        RENAME COLUMN from_=identifier TO to=identifier                 #renameColumn
    | ALTER TABLE tableName=qualifiedName
        ADD COLUMN column=columnDefinition                             #addColumn
    | CREATE (OR REPLACE)? VIEW qualifiedName AS_ query                 #createView
    | DROP VIEW (IF EXISTS)? qualifiedName                             #dropView
    | CALL qualifiedName '(' (callArgument (',' callArgument)*)? ')'   #call
    | GRANT
        (privilege (',' privilege)* | ALL PRIVILEGES)
        ON TABLE? qualifiedName TO grantee=identifier
        (WITH GRANT OPTION)?                                           #grant
    | REVOKE
        (GRANT OPTION FOR)?
        (privilege (',' privilege)* | ALL PRIVILEGES)
        ON TABLE? qualifiedName FROM_ grantee=identifier                #revoke
    | EXPLAIN ANALYZE?
        ('(' explainOption (',' explainOption)* ')')? statement        #explain
    | SHOW CREATE TABLE qualifiedName                                  #showCreateTable
    | SHOW CREATE VIEW qualifiedName                                   #showCreateView
    | SHOW TABLES ((FROM_ | IN) qualifiedName)? (LIKE pattern=STRING)?  #showTables
    | SHOW SCHEMAS ((FROM_ | IN) identifier)? (LIKE pattern=STRING)?    #showSchemas
    | SHOW CATALOGS (LIKE pattern=STRING)?                             #showCatalogs
    | SHOW COLUMNS (FROM_ | IN) qualifiedName                           #showColumns
    | DESCRIBE qualifiedName                                           #showColumns
    | DESC qualifiedName                                               #showColumns
    | SHOW FUNCTIONS                                                   #showFunctions
    | SHOW SESSION                                                     #showSession
    | SET SESSION qualifiedName EQ expression                          #setSession
    | RESET SESSION qualifiedName                                      #resetSession
    | START TRANSACTION (transactionMode (',' transactionMode)*)?      #startTransaction
    | COMMIT WORK?                                                     #commit
    | ROLLBACK WORK?                                                   #rollback
    | SHOW PARTITIONS (FROM_ | IN) qualifiedName
        (WHERE booleanExpression)?
        (ORDER BY sortItem (',' sortItem)*)?
        (LIMIT limit=(INTEGER_VALUE | ALL))?                           #showPartitions
    | PREPARE identifier FROM_ statement                                #prepare
    | DEALLOCATE PREPARE identifier                                    #deallocate
    | EXECUTE identifier (USING expression (',' expression)*)?         #execute
    | DESCRIBE INPUT identifier                                        #describeInput
    | DESCRIBE OUTPUT identifier                                       #describeOutput
    ;

query
    :  presto_with? queryNoWith
    ;

presto_with
    : WITH RECURSIVE? namedQuery (',' namedQuery)*
    ;

tableElement
    : columnDefinition
    | likeClause
    ;

columnDefinition
    : identifier type_
    ;

likeClause
    : LIKE qualifiedName (optionType=(INCLUDING | EXCLUDING) PROPERTIES)?
    ;

tableProperties
    : '(' tableProperty (',' tableProperty)* ')'
    ;

tableProperty
    : identifier EQ expression
    ;

queryNoWith:
      queryTerm
      (ORDER BY sortItem (',' sortItem)*)?
      (LIMIT limit=(INTEGER_VALUE | ALL))?
    ;

queryTerm
    : queryPrimary                                                             #queryTermDefault
    | left=queryTerm operator=INTERSECT setQuantifier? right=queryTerm         #setOperation
    | left=queryTerm operator=(UNION | EXCEPT) setQuantifier? right=queryTerm  #setOperation
    ;

queryPrimary
    : querySpecification                   #queryPrimaryDefault
    | TABLE qualifiedName                  #table
    | VALUES expression (',' expression)*  #inlineTable
    | '(' queryNoWith  ')'                 #subquery
    ;

sortItem
    : expression ordering=(ASC | DESC)? (NULLS nullOrdering=(FIRST | LAST))?
    ;

querySpecification
    : SELECT setQuantifier? selectItem (',' selectItem)*
      (FROM_ relation (',' relation)*)?
      (WHERE where=booleanExpression)?
      (GROUP BY groupBy)?
      (HAVING having=booleanExpression)?
    ;

groupBy
    : setQuantifier? groupingElement (',' groupingElement)*
    ;

groupingElement
    : groupingExpressions                                               #singleGroupingSet
    | ROLLUP '(' (qualifiedName (',' qualifiedName)*)? ')'              #rollup
    | CUBE '(' (qualifiedName (',' qualifiedName)*)? ')'                #cube
    | GROUPING SETS '(' groupingSet (',' groupingSet)* ')'              #multipleGroupingSets
    ;

groupingExpressions
    : '(' (expression (',' expression)*)? ')'
    | expression
    ;

groupingSet
    : '(' (qualifiedName (',' qualifiedName)*)? ')'
    | qualifiedName
    ;

namedQuery
    : name=identifier (columnAliases)? AS_ '(' query ')'
    ;

setQuantifier
    : DISTINCT
    | ALL
    ;

selectItem
    : expression (AS_? identifier)?  #selectSingle
    | qualifiedName '.' ASTERISK    #selectAll
    | ASTERISK                      #selectAll
    ;

relation
    : left=relation
      ( CROSS JOIN right=sampledRelation
      | joinType JOIN rightRelation=relation joinCriteria
      | NATURAL joinType JOIN right=sampledRelation
      )                                           #joinRelation
    | sampledRelation                             #relationDefault
    ;

joinType
    : INNER?
    | LEFT OUTER?
    | RIGHT OUTER?
    | FULL OUTER?
    ;

joinCriteria
    : ON booleanExpression
    | USING '(' identifier (',' identifier)* ')'
    ;

sampledRelation
    : aliasedRelation (
        TABLESAMPLE sampleType '(' percentage=expression ')'
      )?
    ;

sampleType
    : BERNOULLI
    | SYSTEM
    | POISSONIZED
    ;

aliasedRelation
    : relationP=relationPrimary (as_=AS_? alias=identifier columnAliases?)?
    ;

columnAliases
    : '(' identifier (',' identifier)* ')'
    ;

relationPrimary
    : qualifiedName                                                   #tableName
    | '(' query ')'                                                   #subqueryRelation
    | UNNEST '(' expression (',' expression)* ')' (WITH ORDINALITY)?  #unnest
    | '(' relation ')'                                                #parenthesizedRelation
    ;

expression
    : booleanExpression
    ;

booleanExpression
    : predicated                                                   #booleanDefault
    | NOT booleanExpression                                        #logicalNot
    | left=booleanExpression operator=AND right=booleanExpression  #logicalBinary
    | left=booleanExpression operator=OR right=booleanExpression   #logicalBinary
    ;

// workaround for:
//  https://github.com/antlr/antlr4/issues/780
//  https://github.com/antlr/antlr4/issues/781
predicated
    : valueExpression predicate[$valueExpression.ctx]?
    ;

predicate[ParserRuleContext value]
    : comparisonOperator right=valueExpression                            #comparison
    | comparisonOperator comparisonQuantifier '(' query ')'               #quantifiedComparison
    | NOT? BETWEEN lower=valueExpression AND upper=valueExpression        #between
    | NOT? IN '(' expression (',' expression)* ')'                        #inList
    | NOT? IN '(' query ')'                                               #inSubquery
    | NOT? LIKE pattern=valueExpression (ESCAPE escape=valueExpression)?  #like
    | IS NOT? NULL                                                        #nullPredicate
    | IS NOT? DISTINCT FROM_ right=valueExpression                         #distinctFrom
    ;

valueExpression
    : primaryExpression                                                                 #valueExpressionDefault
    | valueExpression AT timeZoneSpecifier                                              #atTimeZone
    | operator=(MINUS | PLUS) valueExpression                                           #arithmeticUnary
    | left=valueExpression operator=(ASTERISK | SLASH | PERCENT) right=valueExpression  #arithmeticBinary
    | left=valueExpression operator=(PLUS | MINUS) right=valueExpression                #arithmeticBinary
    | left=valueExpression CONCAT right=valueExpression                                 #concatenation
    ;

primaryExpression
    : NULL                                                                                #nullLiteral
    | interval                                                                            #intervalLiteral
    | identifier STRING                                                                   #typeConstructor
    | DOUBLE_PRECISION STRING                                                             #typeConstructor
    | number                                                                              #numericLiteral
    | booleanValue                                                                        #booleanLiteral
    | STRING                                                                              #stringLiteral
    | BINARY_LITERAL                                                                      #binaryLiteral
    | '?'                                                                                 #parameter
    | POSITION '(' valueExpression IN valueExpression ')'                                 #position
    // This case handles both an implicit row constructor or a simple parenthesized
    // expression. We can't make the two separate alternatives because it needs
    // unbounded look-ahead to figure out which one to take while it looks for the comma
    | '(' expression (',' expression)* ')'                                                #implicitRowConstructor
    | ROW '(' expression (',' expression)* ')'                                            #rowConstructor
    | qualifiedName '(' ASTERISK ')' filter_? over?                                        #functionCall
    | qualifiedName '(' (setQuantifier? expression (',' expression)*)? ')' filter_? over?  #functionCall
    | identifier '->' expression                                                          #lambda
    | '(' identifier (',' identifier)* ')' '->' expression                                #lambda
    | '(' query ')'                                                                       #subqueryExpression
    // This is an extension to ANSI SQL, which considers EXISTS to be a <boolean expression>
    | EXISTS '(' query ')'                                                                #exists
    | CASE valueExpression whenClause+ (ELSE elseExpression=expression)? END              #simpleCase
    | CASE whenClause+ (ELSE elseExpression=expression)? END                              #searchedCase
    | CAST '(' expression AS_ type_ ')'                                                     #cast
    | TRY_CAST '(' expression AS_ type_ ')'                                                 #cast
    | ARRAY '[' (expression (',' expression)*)? ']'                                       #arrayConstructor
    | value=primaryExpression '[' index=valueExpression ']'                               #subscript
    | identifier                                                                          #columnReference
    | base=primaryExpression '.' fieldName=identifier                                     #dereference
    | name=CURRENT_DATE                                                                   #specialDateTimeFunction
    | name=CURRENT_TIME ('(' precision=INTEGER_VALUE ')')?                                #specialDateTimeFunction
    | name=CURRENT_TIMESTAMP ('(' precision=INTEGER_VALUE ')')?                           #specialDateTimeFunction
    | name=LOCALTIME ('(' precision=INTEGER_VALUE ')')?                                   #specialDateTimeFunction
    | name=LOCALTIMESTAMP ('(' precision=INTEGER_VALUE ')')?                              #specialDateTimeFunction
    | SUBSTRING '(' valueExpression FROM_ valueExpression (FOR valueExpression)? ')'       #substring
    | NORMALIZE '(' valueExpression (',' normalForm)? ')'                                 #normalize
    | EXTRACT '(' identifier FROM_ valueExpression ')'                                     #extract
    ;

timeZoneSpecifier
    : TIME ZONE interval  #timeZoneInterval
    | TIME ZONE STRING    #timeZoneString
    ;

comparisonOperator
    : EQ | NEQ | LT | LTE | GT | GTE
    ;

comparisonQuantifier
    : ALL | SOME | ANY
    ;

booleanValue
    : TRUE | FALSE
    ;

interval
    : INTERVAL sign=(PLUS | MINUS)? STRING from_=intervalField (TO to=intervalField)?
    ;

intervalField
    : YEAR | MONTH | DAY | HOUR | MINUTE | SECOND
    ;

type_
    : type_ ARRAY
    | ARRAY '<' type_ '>'
    | MAP '<' type_ ',' type_ '>'
    | ROW '(' identifier type_ (',' identifier type_)* ')'
    | baseType ('(' typeParameter (',' typeParameter)* ')')?
    ;

typeParameter
    : INTEGER_VALUE | type_
    ;

baseType
    : TIME_WITH_TIME_ZONE
    | TIMESTAMP_WITH_TIME_ZONE
    | DOUBLE_PRECISION
    | identifier
    ;

whenClause
    : WHEN condition=expression THEN result=expression
    ;

filter_
    : FILTER_ '(' WHERE booleanExpression ')'
    ;

over
    : OVER '('
        (PARTITION BY partition+=expression (',' partition+=expression)*)?
        (ORDER BY sortItem (',' sortItem)*)?
        windowFrame?
      ')'
    ;

windowFrame
    : frameType=RANGE start=frameBound
    | frameType=ROWS start=frameBound
    | frameType=RANGE BETWEEN start=frameBound AND end=frameBound
    | frameType=ROWS BETWEEN start=frameBound AND end=frameBound
    ;

frameBound
    : UNBOUNDED boundType=PRECEDING                 #unboundedFrame
    | UNBOUNDED boundType=FOLLOWING                 #unboundedFrame
    | CURRENT ROW                                   #currentRowBound
    | expression boundType=(PRECEDING | FOLLOWING)  #boundedFrame // expression should be unsignedLiteral
    ;


explainOption
    : FORMAT value=(TEXT | GRAPHVIZ)         #explainFormat
    | TYPE value=(LOGICAL | DISTRIBUTED)     #explainType
    ;

transactionMode
    : ISOLATION LEVEL levelOfIsolation    #isolationLevel
    | READ accessMode=(ONLY | WRITE)      #transactionAccessMode
    ;

levelOfIsolation
    : READ UNCOMMITTED                    #readUncommitted
    | READ COMMITTED                      #readCommitted
    | REPEATABLE READ                     #repeatableRead
    | SERIALIZABLE                        #serializable
    ;

callArgument
    : expression                    #positionalArgument
    | identifier '=>' expression    #namedArgument
    ;

privilege
    : SELECT | DELETE | INSERT | identifier
    ;

qualifiedName
    : identifier ('.' identifier)*
    ;

identifier
    : IDENTIFIER             #unquotedIdentifier
    | quotedIdentifier       #quotedIdentifierAlternative
    | nonReserved            #unquotedIdentifier
    | BACKQUOTED_IDENTIFIER  #backQuotedIdentifier
    | DIGIT_IDENTIFIER       #digitIdentifier
    ;

quotedIdentifier
    : QUOTED_IDENTIFIER
    ;

number
    : DECIMAL_VALUE  #decimalLiteral
    | INTEGER_VALUE  #integerLiteral
    ;

nonReserved
    : SHOW | TABLES | COLUMNS | COLUMN | PARTITIONS | FUNCTIONS | SCHEMAS | CATALOGS | SESSION
    | ADD
    | FILTER_
    | OVER | PARTITION | RANGE | ROWS | PRECEDING | FOLLOWING | CURRENT | ROW | MAP | ARRAY
    | TINYINT | SMALLINT | INTEGER | DATE | TIME | TIMESTAMP | INTERVAL | ZONE
    | YEAR | MONTH | DAY | HOUR | MINUTE | SECOND
    | EXPLAIN | ANALYZE | FORMAT | TYPE | TEXT | GRAPHVIZ | LOGICAL | DISTRIBUTED
    | TABLESAMPLE | SYSTEM | BERNOULLI | POISSONIZED | USE | TO
    | SET | RESET
    | VIEW | REPLACE
    | IF | NULLIF | COALESCE
    | normalForm
    | POSITION
    | NO | DATA
    | START | TRANSACTION | COMMIT | ROLLBACK | WORK | ISOLATION | LEVEL
    | SERIALIZABLE | REPEATABLE | COMMITTED | UNCOMMITTED | READ | WRITE | ONLY
    | CALL
    | GRANT | REVOKE | PRIVILEGES | PUBLIC | OPTION
    | SUBSTRING
    | SCHEMA | CASCADE | RESTRICT
    | INPUT | OUTPUT
    | INCLUDING | EXCLUDING | PROPERTIES
    ;

normalForm
    : NFD | NFC | NFKD | NFKC
    ;

SELECT: 'SELECT' | 'select';
FROM_: 'FROM' | 'from';
ADD: 'ADD' | 'add';
AS_: 'AS' | 'as';
ALL: 'ALL' | 'all';
SOME: 'SOME' | 'some';
ANY: 'ANY' | 'any';
DISTINCT: 'DISTINCT' | 'distinct';
WHERE: 'WHERE' | 'where';
GROUP: 'GROUP' | 'group';
BY: 'BY' | 'by';
GROUPING: 'GROUPING' | 'grouping';
SETS: 'SETS' | 'sets';
CUBE: 'CUBE' | 'cube';
ROLLUP: 'ROLLUP' | 'rollup';
ORDER: 'ORDER' | 'order';
HAVING: 'HAVING' | 'having';
LIMIT: 'LIMIT' | 'limit';
AT: 'AT' | 'at';
OR: 'OR' | 'or';
AND: 'AND' | 'and';
IN: 'IN' | 'in';
NOT: 'NOT' | 'not';
NO: 'NO' | 'no';
EXISTS: 'EXISTS' | 'exists';
BETWEEN: 'BETWEEN' | 'between';
LIKE: 'LIKE' | 'like';
IS: 'IS' | 'is';
NULL: 'NULL' | 'null';
TRUE: 'TRUE' | 'true';
FALSE: 'FALSE' | 'false';
NULLS: 'NULLS' | 'nulls';
FIRST: 'FIRST' | 'first';
LAST: 'LAST' | 'last';
ESCAPE: 'ESCAPE' | 'escape';
ASC: 'ASC' | 'asc';
DESC: 'DESC' | 'desc';
SUBSTRING: 'SUBSTRING' | 'substring';
POSITION: 'POSITION' | 'position';
FOR: 'FOR' | 'for';
TINYINT: 'TINYINT' | 'tinyint';
SMALLINT: 'SMALLINT' | 'smallint';
INTEGER: 'INTEGER' | 'integer';
DATE: 'DATE' | 'date';
TIME: 'TIME' | 'time';
TIMESTAMP: 'TIMESTAMP' | 'timestamp';
INTERVAL: 'INTERVAL' | 'interval';
YEAR: 'YEAR' | 'year';
MONTH: 'MONTH' | 'month';
DAY: 'DAY' | 'day';
HOUR: 'HOUR' | 'hour';
MINUTE: 'MINUTE' | 'minute';
SECOND: 'SECOND' | 'second';
ZONE: 'ZONE' | 'zone';
CURRENT_DATE: 'CURRENT_DATE' | 'current_date';
CURRENT_TIME: 'CURRENT_TIME' | 'current_time';
CURRENT_TIMESTAMP: 'CURRENT_TIMESTAMP' | 'current_timestamp';
LOCALTIME: 'LOCALTIME' | 'localtime';
LOCALTIMESTAMP: 'LOCALTIMESTAMP' | 'localtimestamp';
EXTRACT: 'EXTRACT' | 'extract';
CASE: 'CASE' | 'case';
WHEN: 'WHEN' | 'when';
THEN: 'THEN' | 'then';
ELSE: 'ELSE' | 'else';
END: 'END' | 'end';
JOIN: 'JOIN' | 'join';
CROSS: 'CROSS' | 'cross';
OUTER: 'OUTER' | 'outer';
INNER: 'INNER' | 'inner';
LEFT: 'LEFT' | 'left';
RIGHT: 'RIGHT' | 'right';
FULL: 'FULL' | 'full';
NATURAL: 'NATURAL' | 'natural';
USING: 'USING' | 'using';
ON: 'ON' | 'on';
FILTER_: 'FILTER' | 'filter';
OVER: 'OVER' | 'over';
PARTITION: 'PARTITION' | 'partition';
RANGE: 'RANGE' | 'range';
ROWS: 'ROWS' | 'rows';
UNBOUNDED: 'UNBOUNDED' | 'unbounded';
PRECEDING: 'PRECEDING' | 'preceding';
FOLLOWING: 'FOLLOWING' | 'following';
CURRENT: 'CURRENT' | 'current';
ROW: 'ROW' | 'row';
WITH: 'WITH' | 'with';
RECURSIVE: 'RECURSIVE' | 'recursive';
VALUES: 'VALUES' | 'values';
CREATE: 'CREATE' | 'create';
SCHEMA: 'SCHEMA' | 'schema';
TABLE: 'TABLE' | 'table';
VIEW: 'VIEW' | 'view';
REPLACE: 'REPLACE' | 'replace';
INSERT: 'INSERT' | 'insert';
DELETE: 'DELETE' | 'delete';
INTO: 'INTO' | 'into';
CONSTRAINT: 'CONSTRAINT' | 'constraint';
DESCRIBE: 'DESCRIBE' | 'describe';
GRANT: 'GRANT' | 'grant';
REVOKE: 'REVOKE' | 'revoke';
PRIVILEGES: 'PRIVILEGES' | 'privileges';
PUBLIC: 'PUBLIC' | 'public';
OPTION: 'OPTION' | 'option';
EXPLAIN: 'EXPLAIN' | 'explain';
ANALYZE: 'ANALYZE' | 'analyze';
FORMAT: 'FORMAT' | 'format';
TYPE: 'TYPE' | 'type';
TEXT: 'TEXT' | 'text';
GRAPHVIZ: 'GRAPHVIZ' | 'graphviz';
LOGICAL: 'LOGICAL' | 'logical';
DISTRIBUTED: 'DISTRIBUTED' | 'distributed';
CAST: 'CAST' | 'cast';
TRY_CAST: 'TRY_CAST' | 'try_cast';
SHOW: 'SHOW' | 'show';
TABLES: 'TABLES' | 'tables';
SCHEMAS: 'SCHEMAS' | 'schemas';
CATALOGS: 'CATALOGS' | 'catalogs';
COLUMNS: 'COLUMNS' | 'columns';
COLUMN: 'COLUMN' | 'column';
USE: 'USE' | 'use';
PARTITIONS: 'PARTITIONS' | 'partitions';
FUNCTIONS: 'FUNCTIONS' | 'functions';
DROP: 'DROP' | 'drop';
UNION: 'UNION' | 'union';
EXCEPT: 'EXCEPT' | 'except';
INTERSECT: 'INTERSECT' | 'intersect';
TO: 'TO' | 'to';
SYSTEM: 'SYSTEM' | 'system';
BERNOULLI: 'BERNOULLI' | 'bernoulli';
POISSONIZED: 'POISSONIZED' | 'poissonized';
TABLESAMPLE: 'TABLESAMPLE' | 'tablesample';
ALTER: 'ALTER' | 'alter';
RENAME: 'RENAME' | 'rename';
UNNEST: 'UNNEST' | 'unnest';
ORDINALITY: 'ORDINALITY' | 'ordinality';
ARRAY: 'ARRAY' | 'array';
MAP: 'MAP' | 'map';
SET: 'SET' | 'set';
RESET: 'RESET' | 'reset';
SESSION: 'SESSION' | 'session';
DATA: 'DATA' | 'data';
START: 'START' | 'start';
TRANSACTION: 'TRANSACTION' | 'transaction';
COMMIT: 'COMMIT' | 'commit';
ROLLBACK: 'ROLLBACK' | 'rollback';
WORK: 'WORK' | 'work';
ISOLATION: 'ISOLATION' | 'isolation';
LEVEL: 'LEVEL' | 'level';
SERIALIZABLE: 'SERIALIZABLE' | 'serializable';
REPEATABLE: 'REPEATABLE' | 'repeatable';
COMMITTED: 'COMMITTED' | 'committed';
UNCOMMITTED: 'UNCOMMITTED' | 'uncommitted';
READ: 'READ' | 'read';
WRITE: 'WRITE' | 'write';
ONLY: 'ONLY' | 'only';
CALL: 'CALL' | 'call';
PREPARE: 'PREPARE' | 'prepare';
DEALLOCATE: 'DEALLOCATE' | 'deallocate';
EXECUTE: 'EXECUTE' | 'execute';
INPUT: 'INPUT' | 'input';
OUTPUT: 'OUTPUT' | 'output';
CASCADE: 'CASCADE' | 'cascade';
RESTRICT: 'RESTRICT' | 'restrict';
INCLUDING: 'INCLUDING' | 'including';
EXCLUDING: 'EXCLUDING' | 'excluding';
PROPERTIES: 'PROPERTIES' | 'properties';
NORMALIZE: 'NORMALIZE' | 'normalize';
NFD : 'NFD ' | 'nfd ';
NFC : 'NFC ' | 'nfc ';
NFKD : 'NFKD ' | 'nfkd ';
NFKC : 'NFKC ' | 'nfkc ';

IF: 'IF' | 'if';
NULLIF: 'NULLIF' | 'nullif';
COALESCE: 'COALESCE' | 'coalesce';

EQ  : '=';
NEQ : '<>' | '!=';
LT  : '<';
LTE : '<=';
GT  : '>';
GTE : '>=';

PLUS: '+';
MINUS: '-';
ASTERISK: '*';
SLASH: '/';
PERCENT: '%';
CONCAT: '||';

STRING
    : '\'' ( ~'\'' | '\'\'' )* '\''
    ;

// Note: we allow any character inside the binary literal and validate
// its a correct literal when the AST is being constructed. This
// allows us to provide more meaningful error messages to the user
BINARY_LITERAL
    :  'X\'' (~'\'')* '\''
    ;

INTEGER_VALUE
    : DIGIT+
    ;

DECIMAL_VALUE
    : DIGIT+ '.' DIGIT*
    | '.' DIGIT+
    | DIGIT+ ('.' DIGIT*)? EXPONENT
    | '.' DIGIT+ EXPONENT
    ;

IDENTIFIER
    : (LETTER | '_') (LETTER | DIGIT | '_' | '@' | ':')*
    ;

DIGIT_IDENTIFIER
    : DIGIT (LETTER | DIGIT | '_' | '@' | ':')+
    ;

QUOTED_IDENTIFIER
    : '"' ( ~'"' | '""' )* '"'
    ;

BACKQUOTED_IDENTIFIER
    : '`' ( ~'`' | '``' )* '`'
    ;

TIME_WITH_TIME_ZONE
    : 'TIME' WS 'WITH' WS 'TIME' WS 'ZONE'
    ;

TIMESTAMP_WITH_TIME_ZONE
    : 'TIMESTAMP' WS 'WITH' WS 'TIME' WS 'ZONE'
    ;

DOUBLE_PRECISION
    : 'DOUBLE' WS 'PRECISION'
    ;

fragment EXPONENT
    : 'E' [+-]? DIGIT+
    ;

fragment DIGIT
    : [0-9]
    ;

fragment LETTER
    : [A-Z] | [a-z]
    ;

SIMPLE_COMMENT
    : '--' ~[\r\n]* '\r'? '\n'? -> channel(HIDDEN)
    ;

BRACKETED_COMMENT
    : '/*' .*? '*/' -> channel(HIDDEN)
    ;

WS
    : [ \r\n\t]+ -> channel(HIDDEN)
    ;

SEMICOLON
    :';'
    ;

// Catch-all for anything we can't recognize.
// We use this to be able to ignore and recover all the text
// when splitting statements with DelimiterLexer
UNRECOGNIZED
    : .
    ;