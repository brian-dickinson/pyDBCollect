# pyDBCollect
pyDBCollect is a python package with drop-in replacements for 
built-in python collections that persist to a database.

## DBSet
Create a DBSet in memory
```python
from pydbcollect import DBSet as set

a = set('stuffintheset')
a -= set('toremove')
print(a)
```

Create a DBSet
## Set Tests
As a drop-in replacement, DBSet should pass all reasonable
tests for the standard set in python stdlib. All objects in a set must not only
be hashable (requirement for standard set) but also pickleable.

### Summary:
Passed 432 out of 716 tests.

Suite | Test | DBSet Passes? | Explanation
---|------|---|---
TestJointOps | -(Category)- |failed | Not an actual test.
TestSet | -(Category)- |failed | 
TestSet |test_add |passed | 
TestSet |test_clear |passed | 
TestSet |test_c_api |ignored | 
TestSet |test_contains |passed | 
TestSet |test_copy |passed | 
TestSet |test_difference_update |passed | 
TestSet |test_difference |passed | 
TestSet |test_and |passed | 
TestSet |test_constructor_identity |passed | 
TestSet |test_badcmp |passed | 
TestSet |test_cyclical_repr |failed | 
TestSet |test_container_iterator |failed | 
TestSet |test_discard |passed | 
TestSet |test_gc |failed | 
TestSet |test_deepcopy |failed | 
TestSet |test_inplace_on_self |passed | 
TestSet |test_isdisjoint |passed | 
TestSet |test_do_not_rehash_dict_keys |failed | 
TestSet |test_hash |passed | 
TestSet |test_intersection |passed | 
TestSet |test_equality |passed | 
TestSet |test_iand |passed | 
TestSet |test_intersection_update |passed | 
TestSet |test_isub |passed | 
TestSet |test_new_or_init |passed | 
TestSet |test_remove |passed | 
TestSet |test_setOfFrozensets |passed | 
TestSet |test_sub |passed | 
TestSet |test_symmetric_difference_update |passed | 
TestSet |test_weakref |passed | 
TestSet |test_free_after_iterating |passed | 
TestSet |test_init |passed | 
TestSet |test_ior |passed | 
TestSet |test_ixor |passed | 
TestSet |test_pickling |passed | 
TestSet |test_remove_keyerror_unpacking |passed | 
TestSet |test_set_literal_evaluation_order |passed | 
TestSet |test_subclass_with_custom_hash |failed | 
TestSet |test_uniquification |passed | 
TestSet |test_iterator_pickling |failed | 
TestSet |test_or |passed | 
TestSet |test_remove_keyerror_set |failed | 
TestSet |test_set_literal |passed | 
TestSet |test_sub_and_super |passed | 
TestSet |test_union |passed | 
TestSet |test_xor |passed | 
TestSet |test_len |passed | 
TestSet |test_pop |passed | 
TestSet |test_rich_compare |passed | 
TestSet |test_set_literal_insertion_order |passed | 
TestSet |test_symmetric_difference |passed | 
TestSet |test_update |passed | 
TestSetSubclass | -(Category)- |failed | 
TestSetSubclass |test_badcmp |passed | 
TestSetSubclass |test_container_iterator |failed | 
TestSetSubclass |test_deepcopy |failed | 
TestSetSubclass |test_do_not_rehash_dict_keys |failed | 
TestSetSubclass |test_hash |passed | 
TestSetSubclass |test_intersection |passed | 
TestSetSubclass |test_add |passed | 
TestSetSubclass |test_clear |passed | 
TestSetSubclass |test_copy |passed | 
TestSetSubclass |test_difference_update |passed | 
TestSetSubclass |test_isub |passed | 
TestSetSubclass |test_len |passed | 
TestSetSubclass |test_pop |passed | 
TestSetSubclass |test_rich_compare |passed | 
TestSetSubclass |test_set_literal_insertion_order |passed | 
TestSetSubclass |test_symmetric_difference |passed | 
TestSetSubclass |test_update |passed | 
TestSetSubclass |test_c_api |ignored | 
TestSetSubclass |test_contains |passed | 
TestSetSubclass |test_difference |passed | 
TestSetSubclass |test_free_after_iterating |passed | 
TestSetSubclass |test_init |passed | 
TestSetSubclass |test_ior |passed | 
TestSetSubclass |test_ixor |passed | 
TestSetSubclass |test_or |passed | 
TestSetSubclass |test_remove_keyerror_set |failed | 
TestSetSubclass |test_set_literal |passed | 
TestSetSubclass |test_sub_and_super |passed | 
TestSetSubclass |test_union |passed | 
TestSetSubclass |test_equality |passed | 
TestSetSubclass |test_iand |passed | 
TestSetSubclass |test_intersection_update |passed | 
TestSetSubclass |test_xor |passed | 
TestSetSubclass |test_iterator_pickling |failed | 
TestSetSubclass |test_new_or_init |passed | 
TestSetSubclass |test_remove |passed | 
TestSetSubclass |test_setOfFrozensets |passed | 
TestSetSubclass |test_sub |passed | 
TestSetSubclass |test_symmetric_difference_update |passed | 
TestSetSubclass |test_weakref |passed | 
TestSetSubclass |test_and |passed | 
TestSetSubclass |test_constructor_identity |passed | 
TestSetSubclass |test_cyclical_repr |failed | 
TestSetSubclass |test_discard |passed | 
TestSetSubclass |test_gc |failed | 
TestSetSubclass |test_inplace_on_self |passed | 
TestSetSubclass |test_isdisjoint |passed | 
TestSetSubclass |test_keywords_in_subclass |failed | 
TestSetSubclass |test_pickling |failed | 
TestSetSubclass |test_remove_keyerror_unpacking |passed | 
TestSetSubclass |test_set_literal_evaluation_order |passed | 
TestSetSubclass |test_subclass_with_custom_hash |failed | 
TestSetSubclass |test_uniquification |passed | 
TestFrozenSet | -(Category)- |failed | No frozenset implementation.
TestFrozenSetSubclass | -(Category)- |failed | No frozenset implementation.
TestBasicOps | -(Category)- |failed | Not an actual test.
TestBasicOpsEmpty | -(Category)- |failed | 
TestBasicOpsEmpty |test_copy |passed | 
TestBasicOpsEmpty |test_empty_difference |passed | 
TestBasicOpsEmpty |test_empty_difference_rev |passed | 
TestBasicOpsEmpty |test_empty_intersection |passed | 
TestBasicOpsEmpty |test_empty_isdisjoint |passed | 
TestBasicOpsEmpty |test_empty_symmetric_difference |passed | 
TestBasicOpsEmpty |test_empty_union |passed | 
TestBasicOpsEmpty |test_equivalent_equality |passed | 
TestBasicOpsEmpty |test_intersection_empty |passed | 
TestBasicOpsEmpty |test_isdisjoint_empty |passed | 
TestBasicOpsEmpty |test_issue_37219 |passed | 
TestBasicOpsEmpty |test_iteration |passed | 
TestBasicOpsEmpty |test_length |passed | 
TestBasicOpsEmpty |test_pickling |passed | 
TestBasicOpsEmpty |test_repr |failed | 
TestBasicOpsEmpty |test_self_difference |passed | 
TestBasicOpsEmpty |test_self_equality |passed | 
TestBasicOpsEmpty |test_self_intersection |passed | 
TestBasicOpsEmpty |test_self_isdisjoint |passed | 
TestBasicOpsEmpty |test_self_symmetric_difference |passed | 
TestBasicOpsEmpty |test_self_union |passed | 
TestBasicOpsEmpty |test_union_empty |passed | 
TestBasicOpsTriple | -(Category)- |passed | 
TestBasicOpsTriple |test_pickling |passed | 
TestBasicOpsTriple |test_repr |passed | 
TestBasicOpsTriple |test_self_difference |passed | 
TestBasicOpsTriple |test_self_equality |passed | 
TestBasicOpsTriple |test_self_intersection |passed | 
TestBasicOpsTriple |test_self_isdisjoint |passed | 
TestBasicOpsTriple |test_self_symmetric_difference |passed | 
TestBasicOpsTriple |test_self_union |passed | 
TestBasicOpsTriple |test_union_empty |passed | 
TestBasicOpsTriple |test_copy |passed | 
TestBasicOpsTriple |test_empty_difference |passed | 
TestBasicOpsTriple |test_empty_difference_rev |passed | 
TestBasicOpsTriple |test_empty_intersection |passed | 
TestBasicOpsTriple |test_empty_isdisjoint |passed | 
TestBasicOpsTriple |test_empty_symmetric_difference |passed | 
TestBasicOpsTriple |test_empty_union |passed | 
TestBasicOpsTriple |test_equivalent_equality |passed | 
TestBasicOpsTriple |test_intersection_empty |passed | 
TestBasicOpsTriple |test_isdisjoint_empty |passed | 
TestBasicOpsTriple |test_issue_37219 |passed | 
TestBasicOpsTriple |test_iteration |passed | 
TestBasicOpsTriple |test_length |passed | 
TestBasicOpsString | -(Category)- |failed | 
TestBasicOpsString |test_copy |passed | 
TestBasicOpsString |test_empty_difference |passed | 
TestBasicOpsString |test_empty_difference_rev |passed | 
TestBasicOpsString |test_empty_intersection |passed | 
TestBasicOpsString |test_empty_isdisjoint |passed | 
TestBasicOpsString |test_empty_symmetric_difference |passed | 
TestBasicOpsString |test_empty_union |passed | 
TestBasicOpsString |test_equivalent_equality |passed | 
TestBasicOpsString |test_intersection_empty |passed | 
TestBasicOpsString |test_isdisjoint_empty |passed | 
TestBasicOpsString |test_issue_37219 |passed | 
TestBasicOpsString |test_iteration |passed | 
TestBasicOpsString |test_length |passed | 
TestBasicOpsString |test_pickling |passed | 
TestBasicOpsString |test_repr |failed | 
TestBasicOpsString |test_self_difference |passed | 
TestBasicOpsString |test_self_equality |passed | 
TestBasicOpsString |test_self_intersection |passed | 
TestBasicOpsString |test_self_isdisjoint |passed | 
TestBasicOpsString |test_self_symmetric_difference |passed | 
TestBasicOpsString |test_self_union |passed | 
TestBasicOpsString |test_union_empty |passed | 
TestBasicOpsBytes | -(Category)- |passed | 
TestBasicOpsBytes |test_copy |passed | 
TestBasicOpsBytes |test_empty_difference |passed | 
TestBasicOpsBytes |test_empty_difference_rev |passed | 
TestBasicOpsBytes |test_empty_intersection |passed | 
TestBasicOpsBytes |test_empty_isdisjoint |passed | 
TestBasicOpsBytes |test_empty_symmetric_difference |passed | 
TestBasicOpsBytes |test_empty_union |passed | 
TestBasicOpsBytes |test_equivalent_equality |passed | 
TestBasicOpsBytes |test_intersection_empty |passed | 
TestBasicOpsBytes |test_isdisjoint_empty |passed | 
TestBasicOpsBytes |test_issue_37219 |passed | 
TestBasicOpsBytes |test_iteration |passed | 
TestBasicOpsBytes |test_length |passed | 
TestBasicOpsBytes |test_pickling |passed | 
TestBasicOpsBytes |test_repr |passed | 
TestBasicOpsBytes |test_self_difference |passed | 
TestBasicOpsBytes |test_self_equality |passed | 
TestBasicOpsBytes |test_self_intersection |passed | 
TestBasicOpsBytes |test_self_isdisjoint |passed | 
TestBasicOpsBytes |test_self_symmetric_difference |passed | 
TestBasicOpsBytes |test_self_union |passed | 
TestBasicOpsBytes |test_union_empty |passed | 
TestBasicOpsTuple | -(Category)- |passed | 
TestBasicOpsTuple |test_empty_union |passed | 
TestBasicOpsTuple |test_equivalent_equality |passed | 
TestBasicOpsTuple |test_in |passed | 
TestBasicOpsTuple |test_intersection_empty |passed | 
TestBasicOpsTuple |test_isdisjoint_empty |passed | 
TestBasicOpsTuple |test_issue_37219 |passed | 
TestBasicOpsTuple |test_iteration |passed | 
TestBasicOpsTuple |test_length |passed | 
TestBasicOpsTuple |test_not_in |passed | 
TestBasicOpsTuple |test_pickling |passed | 
TestBasicOpsTuple |test_repr |passed | 
TestBasicOpsTuple |test_self_difference |passed | 
TestBasicOpsTuple |test_self_equality |passed | 
TestBasicOpsTuple |test_self_intersection |passed | 
TestBasicOpsTuple |test_self_isdisjoint |passed | 
TestBasicOpsTuple |test_self_symmetric_difference |passed | 
TestBasicOpsTuple |test_self_union |passed | 
TestBasicOpsTuple |test_union_empty |passed | 
TestBasicOpsTuple |test_copy |passed | 
TestBasicOpsTuple |test_empty_difference |passed | 
TestBasicOpsTuple |test_empty_difference_rev |passed | 
TestBasicOpsTuple |test_empty_intersection |passed | 
TestBasicOpsTuple |test_empty_isdisjoint |passed | 
TestBasicOpsTuple |test_empty_symmetric_difference |passed | 
TestBasicOpsMixedStringBytes | -(Category)- |failed | 
TestBasicOpsMixedStringBytes |test_copy |failed | 
TestBasicOpsMixedStringBytes |test_empty_difference |failed | 
TestBasicOpsMixedStringBytes |test_empty_difference_rev |failed | 
TestBasicOpsMixedStringBytes |test_empty_intersection |failed | 
TestBasicOpsMixedStringBytes |test_empty_isdisjoint |failed | 
TestBasicOpsMixedStringBytes |test_empty_symmetric_difference |failed | 
TestBasicOpsMixedStringBytes |test_empty_union |failed | 
TestBasicOpsMixedStringBytes |test_equivalent_equality |failed | 
TestBasicOpsMixedStringBytes |test_intersection_empty |failed | 
TestBasicOpsMixedStringBytes |test_isdisjoint_empty |failed | 
TestBasicOpsMixedStringBytes |test_issue_37219 |failed | 
TestBasicOpsMixedStringBytes |test_iteration |failed | 
TestBasicOpsMixedStringBytes |test_length |failed | 
TestBasicOpsMixedStringBytes |test_pickling |failed | 
TestBasicOpsMixedStringBytes |test_repr |failed | 
TestBasicOpsMixedStringBytes |test_self_difference |failed | 
TestBasicOpsMixedStringBytes |test_self_equality |failed | 
TestBasicOpsMixedStringBytes |test_self_intersection |failed | 
TestBasicOpsMixedStringBytes |test_self_isdisjoint |failed | 
TestBasicOpsMixedStringBytes |test_self_symmetric_difference |failed | 
TestBasicOpsMixedStringBytes |test_self_union |failed | 
TestBasicOpsMixedStringBytes |test_union_empty |failed | 
TestExceptionPropagation | -(Category)- |failed | 
TestExceptionPropagation |test_changingSizeWhileIterating |failed | 
TestExceptionPropagation |test_instanceWithException |passed | 
TestExceptionPropagation |test_instancesWithoutException |passed | 
TestSetOfSets | -(Category)- |passed | 
TestSetOfSets |test_constructor |passed | 
TestBinaryOps | -(Category)- |passed | 
TestBinaryOps |test_eq |passed | 
TestBinaryOps |test_intersection_non_overlap |passed | 
TestBinaryOps |test_intersection_overlap |passed | 
TestBinaryOps |test_intersection_subset |passed | 
TestBinaryOps |test_intersection_superset |passed | 
TestBinaryOps |test_isdisjoint_non_overlap |passed | 
TestBinaryOps |test_isdisjoint_overlap |passed | 
TestBinaryOps |test_isdisjoint_subset |passed | 
TestBinaryOps |test_isdisjoint_superset |passed | 
TestBinaryOps |test_sym_difference_non_overlap |passed | 
TestBinaryOps |test_sym_difference_overlap |passed | 
TestBinaryOps |test_sym_difference_subset |passed | 
TestBinaryOps |test_sym_difference_superset |passed | 
TestBinaryOps |test_union_non_overlap |passed | 
TestBinaryOps |test_union_overlap |passed | 
TestBinaryOps |test_union_subset |passed | 
TestBinaryOps |test_union_superset |passed | 
TestMutate | -(Category)- |passed | 
TestMutate |test_remove_absent |passed | 
TestMutate |test_remove_present |passed | 
TestMutate |test_remove_until_empty |passed | 
TestMutate |test_update_empty_tuple |passed | 
TestMutate |test_update_unit_tuple_non_overlap |passed | 
TestMutate |test_update_unit_tuple_overlap |passed | 
TestMutate |test_add_absent |passed | 
TestMutate |test_add_present |passed | 
TestMutate |test_add_until_full |passed | 
TestMutate |test_clear |passed | 
TestMutate |test_discard_absent |passed | 
TestMutate |test_discard_present |passed | 
TestMutate |test_pop |passed | 
TestSubsets | -(Category)- |failed | Not an actual test.
TestSubsetEqualEmpty | -(Category)- |passed | 
TestSubsetEqualEmpty |test_issubset |passed | 
TestSubsetEqualNonEmpty | -(Category)- |passed | 
TestSubsetEqualNonEmpty |test_issubset |passed | 
TestSubsetEmptyNonEmpty | -(Category)- |passed | 
TestSubsetEmptyNonEmpty |test_issubset |passed | 
TestSubsetPartial | -(Category)- |passed | 
TestSubsetPartial |test_issubset |passed | 
TestSubsetNonOverlap | -(Category)- |passed | 
TestSubsetNonOverlap |test_issubset |passed | 
TestOnlySetsInBinaryOps | -(Category)- |failed | Not an actual test.
TestUpdateOps | -(Category)- |passed | 
TestUpdateOps |test_difference_method_call |passed | 
TestUpdateOps |test_difference_non_overlap |passed | 
TestUpdateOps |test_difference_overlap |passed | 
TestUpdateOps |test_difference_subset |passed | 
TestUpdateOps |test_difference_superset |passed | 
TestUpdateOps |test_intersection_method_call |passed | 
TestUpdateOps |test_intersection_non_overlap |passed | 
TestUpdateOps |test_intersection_overlap |passed | 
TestUpdateOps |test_intersection_subset |passed | 
TestUpdateOps |test_intersection_superset |passed | 
TestUpdateOps |test_sym_difference_method_call |passed | 
TestUpdateOps |test_sym_difference_non_overlap |passed | 
TestUpdateOps |test_sym_difference_overlap |passed | 
TestUpdateOps |test_sym_difference_subset |passed | 
TestUpdateOps |test_sym_difference_superset |passed | 
TestUpdateOps |test_union_method_call |passed | 
TestUpdateOps |test_union_non_overlap |passed | 
TestUpdateOps |test_union_overlap |passed | 
TestUpdateOps |test_union_subset |passed | 
TestUpdateOps |test_union_superset |passed | 
TestOnlySetsNumeric | -(Category)- |passed | 
TestOnlySetsNumeric |test_difference |passed | 
TestOnlySetsNumeric |test_difference_update |passed | 
TestOnlySetsNumeric |test_difference_update_operator |passed | 
TestOnlySetsNumeric |test_eq_ne |passed | 
TestOnlySetsNumeric |test_ge_gt_le_lt |passed | 
TestOnlySetsNumeric |test_intersection |passed | 
TestOnlySetsNumeric |test_intersection_update |passed | 
TestOnlySetsNumeric |test_intersection_update_operator |passed | 
TestOnlySetsNumeric |test_sym_difference |passed | 
TestOnlySetsNumeric |test_sym_difference_update |passed | 
TestOnlySetsNumeric |test_sym_difference_update_operator |passed | 
TestOnlySetsNumeric |test_union |passed | 
TestOnlySetsNumeric |test_update |passed | 
TestOnlySetsNumeric |test_update_operator |passed | 
TestOnlySetsDict | -(Category)- |passed | 
TestOnlySetsDict |test_difference |passed | 
TestOnlySetsDict |test_difference_update |passed | 
TestOnlySetsDict |test_difference_update_operator |passed | 
TestOnlySetsDict |test_eq_ne |passed | 
TestOnlySetsDict |test_ge_gt_le_lt |passed | 
TestOnlySetsDict |test_intersection |passed | 
TestOnlySetsDict |test_intersection_update |passed | 
TestOnlySetsDict |test_intersection_update_operator |passed | 
TestOnlySetsDict |test_sym_difference |passed | 
TestOnlySetsDict |test_sym_difference_update |passed | 
TestOnlySetsDict |test_sym_difference_update_operator |passed | 
TestOnlySetsDict |test_union |passed | 
TestOnlySetsDict |test_update |passed | 
TestOnlySetsDict |test_update_operator |passed | 
TestOnlySetsOperator | -(Category)- |passed | 
TestOnlySetsOperator |test_difference |passed | 
TestOnlySetsOperator |test_difference_update |passed | 
TestOnlySetsOperator |test_difference_update_operator |passed | 
TestOnlySetsOperator |test_eq_ne |passed | 
TestOnlySetsOperator |test_ge_gt_le_lt |passed | 
TestOnlySetsOperator |test_intersection |passed | 
TestOnlySetsOperator |test_intersection_update |passed | 
TestOnlySetsOperator |test_intersection_update_operator |passed | 
TestOnlySetsOperator |test_sym_difference |passed | 
TestOnlySetsOperator |test_sym_difference_update |passed | 
TestOnlySetsOperator |test_sym_difference_update_operator |passed | 
TestOnlySetsOperator |test_union |passed | 
TestOnlySetsOperator |test_update |passed | 
TestOnlySetsOperator |test_update_operator |passed | 
TestOnlySetsTuple | -(Category)- |passed | 
TestOnlySetsTuple |test_difference |passed | 
TestOnlySetsTuple |test_difference_update |passed | 
TestOnlySetsTuple |test_difference_update_operator |passed | 
TestOnlySetsTuple |test_eq_ne |passed | 
TestOnlySetsTuple |test_ge_gt_le_lt |passed | 
TestOnlySetsTuple |test_intersection |passed | 
TestOnlySetsTuple |test_intersection_update |passed | 
TestOnlySetsTuple |test_intersection_update_operator |passed | 
TestOnlySetsTuple |test_sym_difference |passed | 
TestOnlySetsTuple |test_sym_difference_update |passed | 
TestOnlySetsTuple |test_sym_difference_update_operator |passed | 
TestOnlySetsTuple |test_union |passed | 
TestOnlySetsTuple |test_update |passed | 
TestOnlySetsTuple |test_update_operator |passed | 
TestOnlySetsGenerator | -(Category)- |passed | 
TestOnlySetsGenerator |test_difference_update |passed | 
TestOnlySetsGenerator |test_difference_update_operator |passed | 
TestOnlySetsGenerator |test_eq_ne |passed | 
TestOnlySetsGenerator |test_ge_gt_le_lt |passed | 
TestOnlySetsGenerator |test_intersection |passed | 
TestOnlySetsGenerator |test_intersection_update |passed | 
TestOnlySetsGenerator |test_intersection_update_operator |passed | 
TestOnlySetsGenerator |test_sym_difference |passed | 
TestOnlySetsGenerator |test_sym_difference_update |passed | 
TestOnlySetsGenerator |test_sym_difference_update_operator |passed | 
TestOnlySetsGenerator |test_union |passed | 
TestOnlySetsGenerator |test_update |passed | 
TestOnlySetsGenerator |test_update_operator |passed | 
TestOnlySetsGenerator |test_difference |passed | 
TestOnlySetsString | -(Category)- |passed | 
TestOnlySetsString |test_difference |passed | 
TestOnlySetsString |test_difference_update |passed | 
TestOnlySetsString |test_difference_update_operator |passed | 
TestOnlySetsString |test_eq_ne |passed | 
TestOnlySetsString |test_ge_gt_le_lt |passed | 
TestOnlySetsString |test_intersection |passed | 
TestOnlySetsString |test_intersection_update |passed | 
TestOnlySetsString |test_intersection_update_operator |passed | 
TestOnlySetsString |test_sym_difference |passed | 
TestOnlySetsString |test_sym_difference_update |passed | 
TestOnlySetsString |test_sym_difference_update_operator |passed | 
TestOnlySetsString |test_union |passed | 
TestOnlySetsString |test_update |passed | 
TestOnlySetsString |test_update_operator |passed | 
TestCopying | -(Category)- |failed | 
TestCopying |test_copy |failed | 
TestCopying |test_deep_copy |failed | 
TestCopyingEmpty | -(Category)- |passed | 
TestCopyingEmpty |test_copy |passed | 
TestCopyingEmpty |test_deep_copy |passed | 
TestCopyingSingleton | -(Category)- |failed | 
TestCopyingSingleton |test_copy |failed | 
TestCopyingSingleton |test_deep_copy |passed | 
TestCopyingTriple | -(Category)- |failed | 
TestCopyingTriple |test_deep_copy |passed | 
TestCopyingTriple |test_copy |failed | 
TestCopyingTuple | -(Category)- |failed | 
TestCopyingTuple |test_copy |failed | 
TestCopyingTuple |test_deep_copy |passed | 
TestWeirdBugs | -(Category)- |failed | 
TestWeirdBugs |test_iter_and_mutate |failed | 
TestWeirdBugs |test_merge_and_mutate |passed | 
TestWeirdBugs |test_8420_set_merge |passed | 
TestCopyingNested | -(Category)- |failed | 
TestCopyingNested |test_copy |failed | 
TestCopyingNested |test_deep_copy |passed | 
TestBinaryOpsMutating | -(Category)- |failed | Not an actual test.
TestIdentities | -(Category)- |passed | 
TestIdentities |test_binopsVsSubsets |passed | 
TestIdentities |test_commutativity |passed | 
TestIdentities |test_exclusion |passed | 
TestIdentities |test_summations |passed | 
TestBinaryOpsMutating_Set_Set | -(Category)- |failed | 
TestBinaryOpsMutating_Set_Set |test_and_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_eq_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_ge_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_gt_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_iadd_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_ior_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_isub_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_iteration_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_ixor_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_le_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_lt_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_ne_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_or_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_sub_with_mutation |failed | 
TestBinaryOpsMutating_Set_Set |test_xor_with_mutation |failed | 
TestVariousIteratorArgs | -(Category)- |failed | 
TestVariousIteratorArgs |test_constructor |passed | 
TestVariousIteratorArgs |test_inline_methods |failed | 
TestVariousIteratorArgs |test_inplace_methods |failed | 
TestBinaryOpsMutating_Subclass_Subclass | -(Category)- |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_and_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_eq_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_ge_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_gt_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_iadd_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_ior_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_isub_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_iteration_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_ixor_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_le_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_lt_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_ne_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_or_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_sub_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Subclass |test_xor_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass | -(Category)- |failed | 
TestBinaryOpsMutating_Set_Subclass |test_and_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_eq_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_ge_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_gt_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_iadd_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_ior_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_isub_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_iteration_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_ixor_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_le_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_lt_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_ne_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_or_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_sub_with_mutation |failed | 
TestBinaryOpsMutating_Set_Subclass |test_xor_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set | -(Category)- |failed | 
TestBinaryOpsMutating_Subclass_Set |test_and_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_eq_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_ge_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_gt_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_iadd_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_ior_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_isub_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_iteration_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_ixor_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_le_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_lt_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_ne_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_or_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_sub_with_mutation |failed | 
TestBinaryOpsMutating_Subclass_Set |test_xor_with_mutation |failed | 
TestMethodsMutating | -(Category)- |failed | Not an actual test.
TestMethodsMutating_Set_Set | -(Category)- |failed | 
TestMethodsMutating_Set_Set |test_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_difference_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_intersection_update_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_intersection_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_isdisjoint_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_issubset_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_issuperset_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_symmetric_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_symmetric_difference_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_union_with_mutation |failed | 
TestMethodsMutating_Set_Set |test_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass | -(Category)- |failed | 
TestMethodsMutating_Subclass_Subclass |test_difference_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_difference_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_intersection_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_intersection_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_isdisjoint_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_issubset_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_issuperset_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_symmetric_difference_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_symmetric_difference_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_union_with_mutation |failed | 
TestMethodsMutating_Subclass_Subclass |test_update_with_mutation |failed | 
TestMethodsMutating_Set_Subclass | -(Category)- |failed | 
TestMethodsMutating_Set_Subclass |test_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_difference_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_intersection_update_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_intersection_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_isdisjoint_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_issubset_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_issuperset_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_symmetric_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_symmetric_difference_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_union_with_mutation |failed | 
TestMethodsMutating_Set_Subclass |test_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Set | -(Category)- |failed | 
TestMethodsMutating_Subclass_Set |test_difference_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_difference_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_intersection_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_intersection_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_isdisjoint_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_issubset_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_issuperset_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_symmetric_difference_update_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_symmetric_difference_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_union_with_mutation |failed | 
TestMethodsMutating_Subclass_Set |test_update_with_mutation |failed | 
TestBasicOpsSingleton | -(Category)- |passed | 
TestBasicOpsSingleton |test_copy |passed | 
TestBasicOpsSingleton |test_empty_difference |passed | 
TestBasicOpsSingleton |test_empty_difference_rev |passed | 
TestBasicOpsSingleton |test_empty_intersection |passed | 
TestBasicOpsSingleton |test_empty_isdisjoint |passed | 
TestBasicOpsSingleton |test_empty_symmetric_difference |passed | 
TestBasicOpsSingleton |test_empty_union |passed | 
TestBasicOpsSingleton |test_equivalent_equality |passed | 
TestBasicOpsSingleton |test_in |passed | 
TestBasicOpsSingleton |test_intersection_empty |passed | 
TestBasicOpsSingleton |test_isdisjoint_empty |passed | 
TestBasicOpsSingleton |test_issue_37219 |passed | 
TestBasicOpsSingleton |test_iteration |passed | 
TestBasicOpsSingleton |test_length |passed | 
TestBasicOpsSingleton |test_not_in |passed | 
TestBasicOpsSingleton |test_pickling |passed | 
TestBasicOpsSingleton |test_repr |passed | 
TestBasicOpsSingleton |test_self_difference |passed | 
TestBasicOpsSingleton |test_self_equality |passed | 
TestBasicOpsSingleton |test_self_intersection |passed | 
TestBasicOpsSingleton |test_self_isdisjoint |passed | 
TestBasicOpsSingleton |test_self_symmetric_difference |passed | 
TestBasicOpsSingleton |test_self_union |passed | 
TestBasicOpsSingleton |test_union_empty |passed | 
TestMethodsMutating_Set_Dict | -(Category)- |failed | 
TestMethodsMutating_Set_Dict |test_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_difference_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_intersection_update_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_intersection_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_isdisjoint_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_issubset_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_issuperset_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_symmetric_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_symmetric_difference_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_union_with_mutation |failed | 
TestMethodsMutating_Set_Dict |test_update_with_mutation |failed | 
TestMethodsMutating_Set_List | -(Category)- |failed | 
TestMethodsMutating_Set_List |test_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_List |test_difference_with_mutation |failed | 
TestMethodsMutating_Set_List |test_intersection_update_with_mutation |failed | 
TestMethodsMutating_Set_List |test_intersection_with_mutation |failed | 
TestMethodsMutating_Set_List |test_isdisjoint_with_mutation |failed | 
TestMethodsMutating_Set_List |test_issubset_with_mutation |failed | 
TestMethodsMutating_Set_List |test_issuperset_with_mutation |failed | 
TestMethodsMutating_Set_List |test_symmetric_difference_update_with_mutation |failed | 
TestMethodsMutating_Set_List |test_symmetric_difference_with_mutation |failed | 
TestMethodsMutating_Set_List |test_union_with_mutation |failed | 
TestMethodsMutating_Set_List |test_update_with_mutation |failed | 
TestGraphs | -(Category)- |failed | 
TestGraphs |test_cube |failed | 
TestGraphs |test_cuboctahedron |failed | 
TestSetSubclassWithSlots | -(Category)- |failed | 
TestSetSubclassWithSlots |test_pickling |failed | 
TestFrozenSetSubclassWithSlots | -(Category)- |failed | 
TestFrozenSetSubclassWithSlots |test_pickling |failed | 