# Generated from SqlBase.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SqlBaseParser import SqlBaseParser
else:
    from SqlBaseParser import SqlBaseParser

# This class defines a complete listener for a parse tree produced by SqlBaseParser.
class SqlBaseListener(ParseTreeListener):

    # Enter a parse tree produced by SqlBaseParser#multiStatement.
    def enterMultiStatement(self, ctx:SqlBaseParser.MultiStatementContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#multiStatement.
    def exitMultiStatement(self, ctx:SqlBaseParser.MultiStatementContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleStatement.
    def enterSingleStatement(self, ctx:SqlBaseParser.SingleStatementContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleStatement.
    def exitSingleStatement(self, ctx:SqlBaseParser.SingleStatementContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleExpression.
    def enterSingleExpression(self, ctx:SqlBaseParser.SingleExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleExpression.
    def exitSingleExpression(self, ctx:SqlBaseParser.SingleExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#statementDefault.
    def enterStatementDefault(self, ctx:SqlBaseParser.StatementDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#statementDefault.
    def exitStatementDefault(self, ctx:SqlBaseParser.StatementDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#use.
    def enterUse(self, ctx:SqlBaseParser.UseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#use.
    def exitUse(self, ctx:SqlBaseParser.UseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createSchema.
    def enterCreateSchema(self, ctx:SqlBaseParser.CreateSchemaContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createSchema.
    def exitCreateSchema(self, ctx:SqlBaseParser.CreateSchemaContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dropSchema.
    def enterDropSchema(self, ctx:SqlBaseParser.DropSchemaContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dropSchema.
    def exitDropSchema(self, ctx:SqlBaseParser.DropSchemaContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#renameSchema.
    def enterRenameSchema(self, ctx:SqlBaseParser.RenameSchemaContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#renameSchema.
    def exitRenameSchema(self, ctx:SqlBaseParser.RenameSchemaContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createTableAsSelect.
    def enterCreateTableAsSelect(self, ctx:SqlBaseParser.CreateTableAsSelectContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createTableAsSelect.
    def exitCreateTableAsSelect(self, ctx:SqlBaseParser.CreateTableAsSelectContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createTable.
    def enterCreateTable(self, ctx:SqlBaseParser.CreateTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createTable.
    def exitCreateTable(self, ctx:SqlBaseParser.CreateTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dropTable.
    def enterDropTable(self, ctx:SqlBaseParser.DropTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dropTable.
    def exitDropTable(self, ctx:SqlBaseParser.DropTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#insertInto.
    def enterInsertInto(self, ctx:SqlBaseParser.InsertIntoContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#insertInto.
    def exitInsertInto(self, ctx:SqlBaseParser.InsertIntoContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#delete.
    def enterDelete(self, ctx:SqlBaseParser.DeleteContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#delete.
    def exitDelete(self, ctx:SqlBaseParser.DeleteContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#renameTable.
    def enterRenameTable(self, ctx:SqlBaseParser.RenameTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#renameTable.
    def exitRenameTable(self, ctx:SqlBaseParser.RenameTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#renameColumn.
    def enterRenameColumn(self, ctx:SqlBaseParser.RenameColumnContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#renameColumn.
    def exitRenameColumn(self, ctx:SqlBaseParser.RenameColumnContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#addColumn.
    def enterAddColumn(self, ctx:SqlBaseParser.AddColumnContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#addColumn.
    def exitAddColumn(self, ctx:SqlBaseParser.AddColumnContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#createView.
    def enterCreateView(self, ctx:SqlBaseParser.CreateViewContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#createView.
    def exitCreateView(self, ctx:SqlBaseParser.CreateViewContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dropView.
    def enterDropView(self, ctx:SqlBaseParser.DropViewContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dropView.
    def exitDropView(self, ctx:SqlBaseParser.DropViewContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#call.
    def enterCall(self, ctx:SqlBaseParser.CallContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#call.
    def exitCall(self, ctx:SqlBaseParser.CallContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#grant.
    def enterGrant(self, ctx:SqlBaseParser.GrantContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#grant.
    def exitGrant(self, ctx:SqlBaseParser.GrantContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#revoke.
    def enterRevoke(self, ctx:SqlBaseParser.RevokeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#revoke.
    def exitRevoke(self, ctx:SqlBaseParser.RevokeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#explain.
    def enterExplain(self, ctx:SqlBaseParser.ExplainContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#explain.
    def exitExplain(self, ctx:SqlBaseParser.ExplainContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showCreateTable.
    def enterShowCreateTable(self, ctx:SqlBaseParser.ShowCreateTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showCreateTable.
    def exitShowCreateTable(self, ctx:SqlBaseParser.ShowCreateTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showCreateView.
    def enterShowCreateView(self, ctx:SqlBaseParser.ShowCreateViewContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showCreateView.
    def exitShowCreateView(self, ctx:SqlBaseParser.ShowCreateViewContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showTables.
    def enterShowTables(self, ctx:SqlBaseParser.ShowTablesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showTables.
    def exitShowTables(self, ctx:SqlBaseParser.ShowTablesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showSchemas.
    def enterShowSchemas(self, ctx:SqlBaseParser.ShowSchemasContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showSchemas.
    def exitShowSchemas(self, ctx:SqlBaseParser.ShowSchemasContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showCatalogs.
    def enterShowCatalogs(self, ctx:SqlBaseParser.ShowCatalogsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showCatalogs.
    def exitShowCatalogs(self, ctx:SqlBaseParser.ShowCatalogsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showColumns.
    def enterShowColumns(self, ctx:SqlBaseParser.ShowColumnsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showColumns.
    def exitShowColumns(self, ctx:SqlBaseParser.ShowColumnsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showFunctions.
    def enterShowFunctions(self, ctx:SqlBaseParser.ShowFunctionsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showFunctions.
    def exitShowFunctions(self, ctx:SqlBaseParser.ShowFunctionsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showSession.
    def enterShowSession(self, ctx:SqlBaseParser.ShowSessionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showSession.
    def exitShowSession(self, ctx:SqlBaseParser.ShowSessionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setSession.
    def enterSetSession(self, ctx:SqlBaseParser.SetSessionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setSession.
    def exitSetSession(self, ctx:SqlBaseParser.SetSessionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#resetSession.
    def enterResetSession(self, ctx:SqlBaseParser.ResetSessionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#resetSession.
    def exitResetSession(self, ctx:SqlBaseParser.ResetSessionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#startTransaction.
    def enterStartTransaction(self, ctx:SqlBaseParser.StartTransactionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#startTransaction.
    def exitStartTransaction(self, ctx:SqlBaseParser.StartTransactionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#commit.
    def enterCommit(self, ctx:SqlBaseParser.CommitContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#commit.
    def exitCommit(self, ctx:SqlBaseParser.CommitContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#rollback.
    def enterRollback(self, ctx:SqlBaseParser.RollbackContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#rollback.
    def exitRollback(self, ctx:SqlBaseParser.RollbackContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#showPartitions.
    def enterShowPartitions(self, ctx:SqlBaseParser.ShowPartitionsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#showPartitions.
    def exitShowPartitions(self, ctx:SqlBaseParser.ShowPartitionsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#prepare.
    def enterPrepare(self, ctx:SqlBaseParser.PrepareContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#prepare.
    def exitPrepare(self, ctx:SqlBaseParser.PrepareContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#deallocate.
    def enterDeallocate(self, ctx:SqlBaseParser.DeallocateContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#deallocate.
    def exitDeallocate(self, ctx:SqlBaseParser.DeallocateContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#execute.
    def enterExecute(self, ctx:SqlBaseParser.ExecuteContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#execute.
    def exitExecute(self, ctx:SqlBaseParser.ExecuteContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#describeInput.
    def enterDescribeInput(self, ctx:SqlBaseParser.DescribeInputContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#describeInput.
    def exitDescribeInput(self, ctx:SqlBaseParser.DescribeInputContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#describeOutput.
    def enterDescribeOutput(self, ctx:SqlBaseParser.DescribeOutputContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#describeOutput.
    def exitDescribeOutput(self, ctx:SqlBaseParser.DescribeOutputContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#query.
    def enterQuery(self, ctx:SqlBaseParser.QueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#query.
    def exitQuery(self, ctx:SqlBaseParser.QueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#presto_with.
    def enterPresto_with(self, ctx:SqlBaseParser.Presto_withContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#presto_with.
    def exitPresto_with(self, ctx:SqlBaseParser.Presto_withContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableElement.
    def enterTableElement(self, ctx:SqlBaseParser.TableElementContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableElement.
    def exitTableElement(self, ctx:SqlBaseParser.TableElementContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#columnDefinition.
    def enterColumnDefinition(self, ctx:SqlBaseParser.ColumnDefinitionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#columnDefinition.
    def exitColumnDefinition(self, ctx:SqlBaseParser.ColumnDefinitionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#likeClause.
    def enterLikeClause(self, ctx:SqlBaseParser.LikeClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#likeClause.
    def exitLikeClause(self, ctx:SqlBaseParser.LikeClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableProperties.
    def enterTableProperties(self, ctx:SqlBaseParser.TablePropertiesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableProperties.
    def exitTableProperties(self, ctx:SqlBaseParser.TablePropertiesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableProperty.
    def enterTableProperty(self, ctx:SqlBaseParser.TablePropertyContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableProperty.
    def exitTableProperty(self, ctx:SqlBaseParser.TablePropertyContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryNoWith.
    def enterQueryNoWith(self, ctx:SqlBaseParser.QueryNoWithContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryNoWith.
    def exitQueryNoWith(self, ctx:SqlBaseParser.QueryNoWithContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryTermDefault.
    def enterQueryTermDefault(self, ctx:SqlBaseParser.QueryTermDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryTermDefault.
    def exitQueryTermDefault(self, ctx:SqlBaseParser.QueryTermDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setOperation.
    def enterSetOperation(self, ctx:SqlBaseParser.SetOperationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setOperation.
    def exitSetOperation(self, ctx:SqlBaseParser.SetOperationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#queryPrimaryDefault.
    def enterQueryPrimaryDefault(self, ctx:SqlBaseParser.QueryPrimaryDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#queryPrimaryDefault.
    def exitQueryPrimaryDefault(self, ctx:SqlBaseParser.QueryPrimaryDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#table.
    def enterTable(self, ctx:SqlBaseParser.TableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#table.
    def exitTable(self, ctx:SqlBaseParser.TableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inlineTable.
    def enterInlineTable(self, ctx:SqlBaseParser.InlineTableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#inlineTable.
    def exitInlineTable(self, ctx:SqlBaseParser.InlineTableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subquery.
    def enterSubquery(self, ctx:SqlBaseParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subquery.
    def exitSubquery(self, ctx:SqlBaseParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#sortItem.
    def enterSortItem(self, ctx:SqlBaseParser.SortItemContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#sortItem.
    def exitSortItem(self, ctx:SqlBaseParser.SortItemContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#querySpecification.
    def enterQuerySpecification(self, ctx:SqlBaseParser.QuerySpecificationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#querySpecification.
    def exitQuerySpecification(self, ctx:SqlBaseParser.QuerySpecificationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#groupBy.
    def enterGroupBy(self, ctx:SqlBaseParser.GroupByContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#groupBy.
    def exitGroupBy(self, ctx:SqlBaseParser.GroupByContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#singleGroupingSet.
    def enterSingleGroupingSet(self, ctx:SqlBaseParser.SingleGroupingSetContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#singleGroupingSet.
    def exitSingleGroupingSet(self, ctx:SqlBaseParser.SingleGroupingSetContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#rollup.
    def enterRollup(self, ctx:SqlBaseParser.RollupContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#rollup.
    def exitRollup(self, ctx:SqlBaseParser.RollupContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#cube.
    def enterCube(self, ctx:SqlBaseParser.CubeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#cube.
    def exitCube(self, ctx:SqlBaseParser.CubeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#multipleGroupingSets.
    def enterMultipleGroupingSets(self, ctx:SqlBaseParser.MultipleGroupingSetsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#multipleGroupingSets.
    def exitMultipleGroupingSets(self, ctx:SqlBaseParser.MultipleGroupingSetsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#groupingExpressions.
    def enterGroupingExpressions(self, ctx:SqlBaseParser.GroupingExpressionsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#groupingExpressions.
    def exitGroupingExpressions(self, ctx:SqlBaseParser.GroupingExpressionsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#groupingSet.
    def enterGroupingSet(self, ctx:SqlBaseParser.GroupingSetContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#groupingSet.
    def exitGroupingSet(self, ctx:SqlBaseParser.GroupingSetContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#namedQuery.
    def enterNamedQuery(self, ctx:SqlBaseParser.NamedQueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#namedQuery.
    def exitNamedQuery(self, ctx:SqlBaseParser.NamedQueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#setQuantifier.
    def enterSetQuantifier(self, ctx:SqlBaseParser.SetQuantifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#setQuantifier.
    def exitSetQuantifier(self, ctx:SqlBaseParser.SetQuantifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#selectSingle.
    def enterSelectSingle(self, ctx:SqlBaseParser.SelectSingleContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#selectSingle.
    def exitSelectSingle(self, ctx:SqlBaseParser.SelectSingleContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#selectAll.
    def enterSelectAll(self, ctx:SqlBaseParser.SelectAllContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#selectAll.
    def exitSelectAll(self, ctx:SqlBaseParser.SelectAllContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#relationDefault.
    def enterRelationDefault(self, ctx:SqlBaseParser.RelationDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#relationDefault.
    def exitRelationDefault(self, ctx:SqlBaseParser.RelationDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinRelation.
    def enterJoinRelation(self, ctx:SqlBaseParser.JoinRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinRelation.
    def exitJoinRelation(self, ctx:SqlBaseParser.JoinRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinType.
    def enterJoinType(self, ctx:SqlBaseParser.JoinTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinType.
    def exitJoinType(self, ctx:SqlBaseParser.JoinTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#joinCriteria.
    def enterJoinCriteria(self, ctx:SqlBaseParser.JoinCriteriaContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#joinCriteria.
    def exitJoinCriteria(self, ctx:SqlBaseParser.JoinCriteriaContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#sampledRelation.
    def enterSampledRelation(self, ctx:SqlBaseParser.SampledRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#sampledRelation.
    def exitSampledRelation(self, ctx:SqlBaseParser.SampledRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#sampleType.
    def enterSampleType(self, ctx:SqlBaseParser.SampleTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#sampleType.
    def exitSampleType(self, ctx:SqlBaseParser.SampleTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#aliasedRelation.
    def enterAliasedRelation(self, ctx:SqlBaseParser.AliasedRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#aliasedRelation.
    def exitAliasedRelation(self, ctx:SqlBaseParser.AliasedRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#columnAliases.
    def enterColumnAliases(self, ctx:SqlBaseParser.ColumnAliasesContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#columnAliases.
    def exitColumnAliases(self, ctx:SqlBaseParser.ColumnAliasesContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#tableName.
    def enterTableName(self, ctx:SqlBaseParser.TableNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#tableName.
    def exitTableName(self, ctx:SqlBaseParser.TableNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subqueryRelation.
    def enterSubqueryRelation(self, ctx:SqlBaseParser.SubqueryRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subqueryRelation.
    def exitSubqueryRelation(self, ctx:SqlBaseParser.SubqueryRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unnest.
    def enterUnnest(self, ctx:SqlBaseParser.UnnestContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unnest.
    def exitUnnest(self, ctx:SqlBaseParser.UnnestContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#parenthesizedRelation.
    def enterParenthesizedRelation(self, ctx:SqlBaseParser.ParenthesizedRelationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#parenthesizedRelation.
    def exitParenthesizedRelation(self, ctx:SqlBaseParser.ParenthesizedRelationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#expression.
    def enterExpression(self, ctx:SqlBaseParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#expression.
    def exitExpression(self, ctx:SqlBaseParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#logicalNot.
    def enterLogicalNot(self, ctx:SqlBaseParser.LogicalNotContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#logicalNot.
    def exitLogicalNot(self, ctx:SqlBaseParser.LogicalNotContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanDefault.
    def enterBooleanDefault(self, ctx:SqlBaseParser.BooleanDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanDefault.
    def exitBooleanDefault(self, ctx:SqlBaseParser.BooleanDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#logicalBinary.
    def enterLogicalBinary(self, ctx:SqlBaseParser.LogicalBinaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#logicalBinary.
    def exitLogicalBinary(self, ctx:SqlBaseParser.LogicalBinaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#predicated.
    def enterPredicated(self, ctx:SqlBaseParser.PredicatedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#predicated.
    def exitPredicated(self, ctx:SqlBaseParser.PredicatedContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparison.
    def enterComparison(self, ctx:SqlBaseParser.ComparisonContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparison.
    def exitComparison(self, ctx:SqlBaseParser.ComparisonContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#quantifiedComparison.
    def enterQuantifiedComparison(self, ctx:SqlBaseParser.QuantifiedComparisonContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#quantifiedComparison.
    def exitQuantifiedComparison(self, ctx:SqlBaseParser.QuantifiedComparisonContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#between.
    def enterBetween(self, ctx:SqlBaseParser.BetweenContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#between.
    def exitBetween(self, ctx:SqlBaseParser.BetweenContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inList.
    def enterInList(self, ctx:SqlBaseParser.InListContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#inList.
    def exitInList(self, ctx:SqlBaseParser.InListContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#inSubquery.
    def enterInSubquery(self, ctx:SqlBaseParser.InSubqueryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#inSubquery.
    def exitInSubquery(self, ctx:SqlBaseParser.InSubqueryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#like.
    def enterLike(self, ctx:SqlBaseParser.LikeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#like.
    def exitLike(self, ctx:SqlBaseParser.LikeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nullPredicate.
    def enterNullPredicate(self, ctx:SqlBaseParser.NullPredicateContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nullPredicate.
    def exitNullPredicate(self, ctx:SqlBaseParser.NullPredicateContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#distinctFrom.
    def enterDistinctFrom(self, ctx:SqlBaseParser.DistinctFromContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#distinctFrom.
    def exitDistinctFrom(self, ctx:SqlBaseParser.DistinctFromContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#valueExpressionDefault.
    def enterValueExpressionDefault(self, ctx:SqlBaseParser.ValueExpressionDefaultContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#valueExpressionDefault.
    def exitValueExpressionDefault(self, ctx:SqlBaseParser.ValueExpressionDefaultContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#concatenation.
    def enterConcatenation(self, ctx:SqlBaseParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#concatenation.
    def exitConcatenation(self, ctx:SqlBaseParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arithmeticBinary.
    def enterArithmeticBinary(self, ctx:SqlBaseParser.ArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arithmeticBinary.
    def exitArithmeticBinary(self, ctx:SqlBaseParser.ArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arithmeticUnary.
    def enterArithmeticUnary(self, ctx:SqlBaseParser.ArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arithmeticUnary.
    def exitArithmeticUnary(self, ctx:SqlBaseParser.ArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#atTimeZone.
    def enterAtTimeZone(self, ctx:SqlBaseParser.AtTimeZoneContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#atTimeZone.
    def exitAtTimeZone(self, ctx:SqlBaseParser.AtTimeZoneContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#dereference.
    def enterDereference(self, ctx:SqlBaseParser.DereferenceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#dereference.
    def exitDereference(self, ctx:SqlBaseParser.DereferenceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#typeConstructor.
    def enterTypeConstructor(self, ctx:SqlBaseParser.TypeConstructorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#typeConstructor.
    def exitTypeConstructor(self, ctx:SqlBaseParser.TypeConstructorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#specialDateTimeFunction.
    def enterSpecialDateTimeFunction(self, ctx:SqlBaseParser.SpecialDateTimeFunctionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#specialDateTimeFunction.
    def exitSpecialDateTimeFunction(self, ctx:SqlBaseParser.SpecialDateTimeFunctionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#substring.
    def enterSubstring(self, ctx:SqlBaseParser.SubstringContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#substring.
    def exitSubstring(self, ctx:SqlBaseParser.SubstringContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#cast.
    def enterCast(self, ctx:SqlBaseParser.CastContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#cast.
    def exitCast(self, ctx:SqlBaseParser.CastContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#lambda.
    def enterLambda(self, ctx:SqlBaseParser.LambdaContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#lambda.
    def exitLambda(self, ctx:SqlBaseParser.LambdaContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#parameter.
    def enterParameter(self, ctx:SqlBaseParser.ParameterContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#parameter.
    def exitParameter(self, ctx:SqlBaseParser.ParameterContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#normalize.
    def enterNormalize(self, ctx:SqlBaseParser.NormalizeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#normalize.
    def exitNormalize(self, ctx:SqlBaseParser.NormalizeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#intervalLiteral.
    def enterIntervalLiteral(self, ctx:SqlBaseParser.IntervalLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#intervalLiteral.
    def exitIntervalLiteral(self, ctx:SqlBaseParser.IntervalLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#numericLiteral.
    def enterNumericLiteral(self, ctx:SqlBaseParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#numericLiteral.
    def exitNumericLiteral(self, ctx:SqlBaseParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:SqlBaseParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:SqlBaseParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#implicitRowConstructor.
    def enterImplicitRowConstructor(self, ctx:SqlBaseParser.ImplicitRowConstructorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#implicitRowConstructor.
    def exitImplicitRowConstructor(self, ctx:SqlBaseParser.ImplicitRowConstructorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#simpleCase.
    def enterSimpleCase(self, ctx:SqlBaseParser.SimpleCaseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#simpleCase.
    def exitSimpleCase(self, ctx:SqlBaseParser.SimpleCaseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#columnReference.
    def enterColumnReference(self, ctx:SqlBaseParser.ColumnReferenceContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#columnReference.
    def exitColumnReference(self, ctx:SqlBaseParser.ColumnReferenceContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nullLiteral.
    def enterNullLiteral(self, ctx:SqlBaseParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nullLiteral.
    def exitNullLiteral(self, ctx:SqlBaseParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#rowConstructor.
    def enterRowConstructor(self, ctx:SqlBaseParser.RowConstructorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#rowConstructor.
    def exitRowConstructor(self, ctx:SqlBaseParser.RowConstructorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subscript.
    def enterSubscript(self, ctx:SqlBaseParser.SubscriptContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subscript.
    def exitSubscript(self, ctx:SqlBaseParser.SubscriptContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#subqueryExpression.
    def enterSubqueryExpression(self, ctx:SqlBaseParser.SubqueryExpressionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#subqueryExpression.
    def exitSubqueryExpression(self, ctx:SqlBaseParser.SubqueryExpressionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#binaryLiteral.
    def enterBinaryLiteral(self, ctx:SqlBaseParser.BinaryLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#binaryLiteral.
    def exitBinaryLiteral(self, ctx:SqlBaseParser.BinaryLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#extract.
    def enterExtract(self, ctx:SqlBaseParser.ExtractContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#extract.
    def exitExtract(self, ctx:SqlBaseParser.ExtractContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#stringLiteral.
    def enterStringLiteral(self, ctx:SqlBaseParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#stringLiteral.
    def exitStringLiteral(self, ctx:SqlBaseParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#arrayConstructor.
    def enterArrayConstructor(self, ctx:SqlBaseParser.ArrayConstructorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#arrayConstructor.
    def exitArrayConstructor(self, ctx:SqlBaseParser.ArrayConstructorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#functionCall.
    def enterFunctionCall(self, ctx:SqlBaseParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#functionCall.
    def exitFunctionCall(self, ctx:SqlBaseParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#exists.
    def enterExists(self, ctx:SqlBaseParser.ExistsContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#exists.
    def exitExists(self, ctx:SqlBaseParser.ExistsContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#position.
    def enterPosition(self, ctx:SqlBaseParser.PositionContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#position.
    def exitPosition(self, ctx:SqlBaseParser.PositionContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#searchedCase.
    def enterSearchedCase(self, ctx:SqlBaseParser.SearchedCaseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#searchedCase.
    def exitSearchedCase(self, ctx:SqlBaseParser.SearchedCaseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#timeZoneInterval.
    def enterTimeZoneInterval(self, ctx:SqlBaseParser.TimeZoneIntervalContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#timeZoneInterval.
    def exitTimeZoneInterval(self, ctx:SqlBaseParser.TimeZoneIntervalContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#timeZoneString.
    def enterTimeZoneString(self, ctx:SqlBaseParser.TimeZoneStringContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#timeZoneString.
    def exitTimeZoneString(self, ctx:SqlBaseParser.TimeZoneStringContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:SqlBaseParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:SqlBaseParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#comparisonQuantifier.
    def enterComparisonQuantifier(self, ctx:SqlBaseParser.ComparisonQuantifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#comparisonQuantifier.
    def exitComparisonQuantifier(self, ctx:SqlBaseParser.ComparisonQuantifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#booleanValue.
    def enterBooleanValue(self, ctx:SqlBaseParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#booleanValue.
    def exitBooleanValue(self, ctx:SqlBaseParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#interval.
    def enterInterval(self, ctx:SqlBaseParser.IntervalContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#interval.
    def exitInterval(self, ctx:SqlBaseParser.IntervalContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#intervalField.
    def enterIntervalField(self, ctx:SqlBaseParser.IntervalFieldContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#intervalField.
    def exitIntervalField(self, ctx:SqlBaseParser.IntervalFieldContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#type_.
    def enterType_(self, ctx:SqlBaseParser.Type_Context):
        pass

    # Exit a parse tree produced by SqlBaseParser#type_.
    def exitType_(self, ctx:SqlBaseParser.Type_Context):
        pass


    # Enter a parse tree produced by SqlBaseParser#typeParameter.
    def enterTypeParameter(self, ctx:SqlBaseParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#typeParameter.
    def exitTypeParameter(self, ctx:SqlBaseParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#baseType.
    def enterBaseType(self, ctx:SqlBaseParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#baseType.
    def exitBaseType(self, ctx:SqlBaseParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#whenClause.
    def enterWhenClause(self, ctx:SqlBaseParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#whenClause.
    def exitWhenClause(self, ctx:SqlBaseParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#filter_.
    def enterFilter_(self, ctx:SqlBaseParser.Filter_Context):
        pass

    # Exit a parse tree produced by SqlBaseParser#filter_.
    def exitFilter_(self, ctx:SqlBaseParser.Filter_Context):
        pass


    # Enter a parse tree produced by SqlBaseParser#over.
    def enterOver(self, ctx:SqlBaseParser.OverContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#over.
    def exitOver(self, ctx:SqlBaseParser.OverContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#windowFrame.
    def enterWindowFrame(self, ctx:SqlBaseParser.WindowFrameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#windowFrame.
    def exitWindowFrame(self, ctx:SqlBaseParser.WindowFrameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unboundedFrame.
    def enterUnboundedFrame(self, ctx:SqlBaseParser.UnboundedFrameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unboundedFrame.
    def exitUnboundedFrame(self, ctx:SqlBaseParser.UnboundedFrameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#currentRowBound.
    def enterCurrentRowBound(self, ctx:SqlBaseParser.CurrentRowBoundContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#currentRowBound.
    def exitCurrentRowBound(self, ctx:SqlBaseParser.CurrentRowBoundContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#boundedFrame.
    def enterBoundedFrame(self, ctx:SqlBaseParser.BoundedFrameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#boundedFrame.
    def exitBoundedFrame(self, ctx:SqlBaseParser.BoundedFrameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#explainFormat.
    def enterExplainFormat(self, ctx:SqlBaseParser.ExplainFormatContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#explainFormat.
    def exitExplainFormat(self, ctx:SqlBaseParser.ExplainFormatContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#explainType.
    def enterExplainType(self, ctx:SqlBaseParser.ExplainTypeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#explainType.
    def exitExplainType(self, ctx:SqlBaseParser.ExplainTypeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#isolationLevel.
    def enterIsolationLevel(self, ctx:SqlBaseParser.IsolationLevelContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#isolationLevel.
    def exitIsolationLevel(self, ctx:SqlBaseParser.IsolationLevelContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#transactionAccessMode.
    def enterTransactionAccessMode(self, ctx:SqlBaseParser.TransactionAccessModeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#transactionAccessMode.
    def exitTransactionAccessMode(self, ctx:SqlBaseParser.TransactionAccessModeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#readUncommitted.
    def enterReadUncommitted(self, ctx:SqlBaseParser.ReadUncommittedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#readUncommitted.
    def exitReadUncommitted(self, ctx:SqlBaseParser.ReadUncommittedContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#readCommitted.
    def enterReadCommitted(self, ctx:SqlBaseParser.ReadCommittedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#readCommitted.
    def exitReadCommitted(self, ctx:SqlBaseParser.ReadCommittedContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#repeatableRead.
    def enterRepeatableRead(self, ctx:SqlBaseParser.RepeatableReadContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#repeatableRead.
    def exitRepeatableRead(self, ctx:SqlBaseParser.RepeatableReadContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#serializable.
    def enterSerializable(self, ctx:SqlBaseParser.SerializableContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#serializable.
    def exitSerializable(self, ctx:SqlBaseParser.SerializableContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#positionalArgument.
    def enterPositionalArgument(self, ctx:SqlBaseParser.PositionalArgumentContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#positionalArgument.
    def exitPositionalArgument(self, ctx:SqlBaseParser.PositionalArgumentContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#namedArgument.
    def enterNamedArgument(self, ctx:SqlBaseParser.NamedArgumentContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#namedArgument.
    def exitNamedArgument(self, ctx:SqlBaseParser.NamedArgumentContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#privilege.
    def enterPrivilege(self, ctx:SqlBaseParser.PrivilegeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#privilege.
    def exitPrivilege(self, ctx:SqlBaseParser.PrivilegeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#qualifiedName.
    def enterQualifiedName(self, ctx:SqlBaseParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#qualifiedName.
    def exitQualifiedName(self, ctx:SqlBaseParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#unquotedIdentifier.
    def enterUnquotedIdentifier(self, ctx:SqlBaseParser.UnquotedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#unquotedIdentifier.
    def exitUnquotedIdentifier(self, ctx:SqlBaseParser.UnquotedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#quotedIdentifierAlternative.
    def enterQuotedIdentifierAlternative(self, ctx:SqlBaseParser.QuotedIdentifierAlternativeContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#quotedIdentifierAlternative.
    def exitQuotedIdentifierAlternative(self, ctx:SqlBaseParser.QuotedIdentifierAlternativeContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#backQuotedIdentifier.
    def enterBackQuotedIdentifier(self, ctx:SqlBaseParser.BackQuotedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#backQuotedIdentifier.
    def exitBackQuotedIdentifier(self, ctx:SqlBaseParser.BackQuotedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#digitIdentifier.
    def enterDigitIdentifier(self, ctx:SqlBaseParser.DigitIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#digitIdentifier.
    def exitDigitIdentifier(self, ctx:SqlBaseParser.DigitIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#quotedIdentifier.
    def enterQuotedIdentifier(self, ctx:SqlBaseParser.QuotedIdentifierContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#quotedIdentifier.
    def exitQuotedIdentifier(self, ctx:SqlBaseParser.QuotedIdentifierContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:SqlBaseParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:SqlBaseParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:SqlBaseParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:SqlBaseParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#nonReserved.
    def enterNonReserved(self, ctx:SqlBaseParser.NonReservedContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#nonReserved.
    def exitNonReserved(self, ctx:SqlBaseParser.NonReservedContext):
        pass


    # Enter a parse tree produced by SqlBaseParser#normalForm.
    def enterNormalForm(self, ctx:SqlBaseParser.NormalFormContext):
        pass

    # Exit a parse tree produced by SqlBaseParser#normalForm.
    def exitNormalForm(self, ctx:SqlBaseParser.NormalFormContext):
        pass



del SqlBaseParser