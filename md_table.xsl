<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:lookup="lookup" exclude-result-prefixes="lookup">
    <lookup:suite>
        <row name="TestJointOps" reason="Not an actual test."/>
        <row name="TestFrozenSet" reason="No frozenset implementation."/>
        <row name="TestFrozenSetSubclass" reason="No frozenset implementation."/>
        <row name="TestBasicOps" reason="Not an actual test."/>
        <row name="TestBinaryOpsMutating" reason="Not an actual test."/>
        <row name="TestSubsets" reason="Not an actual test."/>
        <row name="TestOnlySetsInBinaryOps" reason="Not an actual test."/>
        <row name="TestMethodsMutating" reason="Not an actual test."/>
    </lookup:suite>
    <lookup:test>
        <row name="keyword_init" reason="Keywords are used in init."/>
        <row name="test_keywords_in_subclass" reason="Keywords are used in init."/>
        <row name="test_contains" reason="DBSet does not support &quot; containing &quot; other DBSets"/>
        <row name="test_iterator_pickling" reason="Cannot make iterator pickleable."/>
        <row name="test_deepcopy" reason="Unpickleable inner class."/>
        <row name="test_gc" reason="Unpickleable inner class."/>
        <row name="test_subclass_with_custom_hash" reason="Unpickleable inner class."/>
        <row name="test_cyclical_repr" reason="DBSet does not support self-referential sets."/>
        <row name="test_do_not_rehash_dict_keys" reason="Unnecessary optimization"/>
        <row name="test_container_iterator" reason="Unpickleable inner class."/>
        <row name="test_free_after_iterating" reason="Unpickleable inner class."/>
        <row name="test_remove" reason="DBSet does not support &quot; containing &quot; other DBSets."/>
        <row name="test_remove_keyerror_set"
             reason="DBSet does not support &quot; containing &quot; other DBSets."/>
        <row name="test_discard" reason="DBSet does not support &quot; containing &quot; other DBSets."/>
        <row name="test_copying" reason="database entries don't have memory addresses"/>
    </lookup:test>
    <xsl:template match="/testrun">
## Summary:
Passed
<xsl:value-of select="count[@name='passed']/@value"/>
out of
<xsl:value-of select="count[@name='total']/@value"/>
tests.

Suite | Test | DBSet Passes? | Explanation
---|------|---|---
<xsl:for-each select="suite[1]/suite">
<xsl:variable name="suiteName" select="@name"/>
<xsl:value-of select="@name"/> | -(Category)- |<xsl:value-of select="@status"/> | <xsl:value-of select="document('')//lookup:suite/row[@name= $suiteName]/@reason"/> <xsl:text>&#xa;</xsl:text>

<xsl:if test="not(boolean(document('')//lookup:suite/row[@name = $suiteName]))">
<xsl:for-each select="test">

<xsl:value-of select="$suiteName"/> |<xsl:value-of select="@name"/> |<xsl:value-of select="@status"/> | <xsl:value-of select="document('')//lookup:table/row[@name='$suiteName']/@reason"/><xsl:text>&#xa;</xsl:text>


</xsl:for-each>

</xsl:if>

</xsl:for-each>

</xsl:template>
</xsl:stylesheet>