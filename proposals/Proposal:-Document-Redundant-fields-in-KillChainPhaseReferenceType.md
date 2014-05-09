**Status**: Accepted  
**Comment Period Closes**: 1/3/2014  
**Affects Backwards Compatibility**: NO  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/41

#### Background Information
`KillChainPhaseReferenceType` contains several attributes that are redundant to the `KillChainPhaseType` that it references:

* `@name`
* `@ordinality`
* `@kill_chain_name`

Because these attributes exist both at the phase definition level and the phase reference level, consumers can avoid having to dereference the IDs to get to the name, ordinality, and kill chain name assuming the producer has populated those attributes:
```xml
<Kill_Chain_Phase phase_id="some-id" name="Scouting" />
<!-- As referenced elsewhere -->
<Kill_Chain_Phase_Reference phase_id="some-id" name="Scouting" />
```

Note that because the phase reference contains the name, the consumer does not have to look up the original definition to find that information.

On the other hand, this can lead to confusion because the information in the reference could conflict with the information in the definition:
```xml
<Kill_Chain_Phase phase_id="some-id" name="Recon" />
<!-- As referenced elsewhere -->
<Kill_Chain_Phase_Reference phase_id="some-id" name="Scouting" />
```

Note that the name is not consistent across the reference and the phase definition, which creates a conflict in the data: consumers that use the phase name from the reference will think the name is "Scouting" while those using the phase_id to look up the name in the definition will think the name is "Recon".

#### Proposal

One possible solution to this is to remove the name, ordinality, and kill_chain_name attributes from KillChainPhaseReferenceType. This would remove the shortcut to resolving the name, but would also remove the possibility of conflicts (and potentially resolve some confusion about the semantic meaning of including the name or other information in references).

The other issue with this change is that it would be a backwards-incompatible change with the potential to break existing content. Given that this issue isn't really a "bug" (when used correctly, it works fine) per our versioning policy we should not make this change in 1.1.

As an alternative, we can simply document the correct usage of those attributes to note that they should either be omitted from KillChainPhaseReferenceType or, if they are included, must match the referenced kill chain phase information. This would simply clarify the practices that make sense and would not break existing content.

In the absence of other feedback saying that this is a bug and is worth fixing in 1.1 despite the fact that it may break existing content, we will take the latter approach.

#### Impact
There is no compatibility impact expected to this change. It is a simple annotation change that will clarify existing practices. It will, however, not fully resolve the issue.

#### Requested Feedback

1. Is the KillChainPhaseReferenceType issue a bug that needs to be fixed in 1.1 or is our current approach to fixing it in documentation now and fully resolving it in the next major release acceptable?

#### Resolution

This proposal was accepted as-is: the inconsistency will not be corrected in schema for 1.1 but the expected behavior and suggested practices will be documented in the schema annotations.