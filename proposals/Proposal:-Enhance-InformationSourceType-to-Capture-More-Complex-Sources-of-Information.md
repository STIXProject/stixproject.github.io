**Status**: Accepted  
**Comment Period Closes**: 01/20/2014  
**Affects Backwards Compatibility**: YES  
**Relevant Issue**: https://github.com/STIXProject/schemas/issues/26

#### Background Information
The source of information content in STIX is captured using the `InformationSourceType`. This type is leveraged by `Information_Source` fields in the `STIX_Header` (for capturing the information source of a whole package), `TTP`, `Threat_Actor` and `Campaign` constructs and by the `Producer` field in the `Indicator` construct.

The `InformationSourceType` can currently capture simple information identifying a single source of information including a very simple list of identities of contributors.
Real-world generation and evolution of threat information content often involves more complex provenience and provenance than this simple structure can support.
There is a need to be able to characterize these more complex information source situations in a consistent way across STIX.

An example scenario of this sort of complex source information would be: Org A publishes a prose threat information report; Org B transforms the report from Org A into structured STIX format (this is what MITRE did with the Mandiant APT1 and FireEye Poison Ivy reports); Org C  and Org D each take the STIX formatted report from Org A , do additional analysis and capture the result in structured STIX format;  Org E takes the STIX content from Org C and Org D and aggregates it into a single set of STIX formatted content.
This example illustrates the need to characterize more than just the immediate source of the content. It shows a need to characterize the evolutionary provenance of the content including the nature of role played by each link in the provenance chain.

#### Proposal
This proposal suggests the following set of refinements to the `InformationSourceType` :

* Addition of a `Description` field for providing a broad description of the nature of the information source
* Addition of a `Role` field (of `ControlledVocabularyStringType`) to characterize the role played by the information source party
* Change the name of the `Contributors` field to `Contributing_Sources` to more appropriately address its purpose
* Change the name of `ContributorsType` to `ContributingSourcesType` to more appropriately address its purpose
* Change the name of the `Contributor` field within the (newly renamed) `ContributingSourcesType` to `Source` to more appropriately address its purpose
* Change the type of the (newly renamed) `Source` field from `IdentityType` (which only captured identity and not the other useful information source fields) to `InformationSourceType` which adds the full set of information source fields and enables recursive chaining for provenance

The proposal further suggests the creation of a new default controlled vocabulary ( `InformationSourceRoleVocab-1.0`) with initial enumerated values of  `Initial Author`, `Content Enhancer/Refiner`, `Aggregator`, and `Transformer/Translator`.

Finally, this proposal suggests the addition of `Information_Source` elements to the Incident and `Course_of_Action` constructs that currently lack this capability.


A simple single author scenario could be represented as:
```xml
<stix:Information_Source>
	<stixCommon:Identity><stixCommon:Name>Org A</stixCommon:Name></stixCommon:Identity>
	<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Initial Author</stixCommon:Role>
</stix:Information_Source>

```

A translation case such as MITRE’s translation of the Mandiant APT1 report into STIX could be represented as:
```xml
<stix:Information_Source>
	<stixCommon:Identity><stixCommon:Name>MITRE</stixCommon:Name></stixCommon:Identity>
	<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Transformer/Translator</stixCommon:Role>
	<stixCommon:Contributing_Sources>
		<stixCommon:Source>
			<stix:Information_Source>
				<stixCommon:Identity><stixCommon:Name>Mandiant</stixCommon:Name></stixCommon:Identity>
				<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Initial Author</stixCommon:Role>
			</stix:Information_Source>
		</stixCommon:Source>
	</stixCommon:Contributing_Sources>
</stix:Information_Source>
```


The full complex scenario given as an example above could be represented as:
```xml
<stix:Information_Source>
	<stixCommon:Identity><stixCommon:Name>Org E</stixCommon:Name></stixCommon:Identity>
	<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Aggregator</stixCommon:Role>
	<stixCommon:Contributing_Sources>
		<stixCommon:Source>
			<stix:Information_Source>
				<stixCommon:Identity><stixCommon:Name>Org D</stixCommon:Name></stixCommon:Identity>
				<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Content Enhancer/Refiner</stixCommon:Role>
				<stixCommon:Contributing_Sources>
					<stixCommon:Source>
						<stix:Information_Source>
							<stixCommon:Identity><stixCommon:Name>Org B</stixCommon:Name></stixCommon:Identity>
							<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Transformer/Translator</stixCommon:Role>
							<stixCommon:Contributing_Sources>
								<stixCommon:Source>
									<stix:Information_Source>
										<stixCommon:Identity><stixCommon:Name>Org A</stixCommon:Name></stixCommon:Identity>
										<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Initial Author</stixCommon:Role>
									</stix:Information_Source>
								</stixCommon:Source>
							</stixCommon:Contributing_Sources>
						</stix:Information_Source>
					</stixCommon:Source>
				</stixCommon:Contributing_Sources>
			</stix:Information_Source>
		</stixCommon:Source>
		<stixCommon:Source>
			<stix:Information_Source>
				<stixCommon:Identity><stixCommon:Name>Org C</stixCommon:Name></stixCommon:Identity>
				<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Content Enhancer/Refiner</stixCommon:Role>
				<stixCommon:Contributing_Sources>
					<stixCommon:Source>
						<stix:Information_Source>
							<stixCommon:Identity><stixCommon:Name>Org B</stixCommon:Name></stixCommon:Identity>
							<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Transformer/Translator</stixCommon:Role>
							<stixCommon:Contributing_Sources>
								<stixCommon:Source>
									<stix:Information_Source>
										<stixCommon:Identity><stixCommon:Name>Org A</stixCommon:Name></stixCommon:Identity>
										<stixCommon:Role xsi:type="stixVocabs:InformationSourceRoleVocab-1.0">Initial Author</stixCommon:Role>
									</stix:Information_Source>
								</stixCommon:Source>
							</stixCommon:Contributing_Sources>
						</stix:Information_Source>
					</stixCommon:Source>
				</stixCommon:Contributing_Sources>
			</stix:Information_Source>
		</stixCommon:Source>
	</stixCommon:Contributing_Sources>
</stix:Information_Source>
```


#### Impact
This proposal resolves what is considered a significant shortcoming in STIX 1.0.1 that needs to be urgently addressed for a wide range of content the community is trying to represent today. It is not fully backward compatible but the areas of incompatibility are localized to the `Contributors` construct which appears to be rarely used due to its current limitations. Specifically, it changes the name of the `Contributors` and `Contributor` field and changes the `Contributor` field from `IdentityType` to `InformationSourceType`, adding a `Specification` layer above the `Identity` construct. Any instances of `InformationSourceType` would need to have the names of the `Contributors` and `Contributor` fields changed and a `Specification` element layer added to be valid for STIX 1.1.

#### Requested Feedback

1. Should this capability be added to STIX?
2. Are the specified additional fields appropriate?
3. Are the specified additional fields adequate?
4. Are the proposed values for `InformationSourceRoleVocab-1.0` appropriate?
5. Are the proposed values for `InformationSourceRoleVocab-1.0` adequate?
2. Should this capability be added in STIX 1.1 or wait until STIX 2.0 (NOTE: Exact timeframe for STIX 2.0 release is still undefined)?
