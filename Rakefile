# Note: to run this you'll need to init/update the submodules for stix and then for cybox within stix. Sorry :(

require 'bundler'
require 'fileutils'
require 'liquid'
require 'stix_schema_spy'

$destination = "data-model"

$stix_prefixes = ['campaign', 'coa', 'et', 'genericStructuredCOA', 'genericTM',
                  'incident', 'indicator', 'marking', 'simpleMarking',
                  'snortTM', 'stix', 'stix-capec', 'stix-ciqaddress',
                  'stix-ciqidentity', 'stixCommon', 'stix-cvrf', 'stix-maec',
                  'stix-openioc', 'stix-oval', 'stixVocabs', 'ta',
                  'tlpMarking', 'TOUMarking', 'ttp', 'yaraTM', 'report']

$stix_uri_fmt = "http://stix.readthedocs.org/en/%s/api/"
$cybox_uri = "http://cybox.readthedocs.org/en/stable/"

# Map STIX versions to branches in the python-stix documentation
$python_versions = {
    "1.0" => nil,
    "1.0.1" => nil,
    "1.1" => nil,
    "1.1.1" => "v1.1.1.5",
    "1.2" => "stable",
}

$stix_links = {
    "campaign:AssociatedCampaignsType" => "campaign/campaign.html#stix.campaign.AssociatedCampaigns",
    "campaign:AttributionType" => "campaign/campaign.html#stix.campaign.Attribution",
    "campaign:CampaignType" => "campaign/campaign.html#stix.campaign.Campaign",
    "campaign:NamesType" => "campaign/campaign.html#stix.campaign.Names",
    "campaign:RelatedIncidentsType" => "campaign/campaign.html#stix.campaign.RelatedIncidents",
    "campaign:RelatedIndicatorsType" => "campaign/campaign.html#stix.campaign.RelatedIndicators",
    "campaign:RelatedTTPsType" => "campaign/campaign.html#stix.campaign.RelatedTTPs",
    "coa:CourseOfActionType" => "coa/coa.html#stix.coa.CourseOfAction",
    "coa:ObjectiveType" => "coa/objective.html#stix.coa.objective.Objective",
    "coa:RelatedCOAsType" => "coa/coa.html#stix.coa.RelatedCOAs",
    "coa:StructuredCOAType" => nil,
    "et:AffectedSoftwareType" => "exploit_target/vulnerability.html#stix.exploit_target.vulnerability.AffectedSoftware",
    "et:ConfigurationType" => "exploit_target/configuration.html#stix.exploit_target.configuration.Configuration",
    "et:CVSSVectorType" => "exploit_target/vulnerability.html#stix.exploit_target.vulnerability.CVSSVector",
    "et:ExploitTargetType" => "exploit_target/exploit_target.html#stix.exploit_target.ExploitTarget",
    "et:PotentialCOAsType" => "exploit_target/exploit_target.html#stix.exploit_target.PotentialCOAs",
    "et:RelatedExploitTargetsType" => "exploit_target/exploit_target.html#stix.exploit_target.RelatedExploitTargets",
    "et:VulnerabilityType" => "exploit_target/vulnerability.html#stix.exploit_target.vulnerability.Vulnerability",
    "et:WeaknessType" => "exploit_target/weakness.html#stix.exploit_target.weakness.Weakness",
    "genericStructuredCOA:GenericStructuredCOAType" => nil,
    "genericTM:GenericTestMechanismType" => nil,
    "incident:AffectedAssetsType" => nil,
    "incident:AffectedAssetType" => "incident/affected_asset.html#stix.incident.affected_asset.AffectedAsset",
    "incident:AssetTypeType" => "incident/affected_asset.html#stix.incident.affected_asset.AssetType",
    "incident:AttributedThreatActorsType" => "incident/incident.html#stix.incident.AttributedThreatActors",
    "incident:CategoriesType" => nil,
    "incident:COARequestedType" => nil,
    "incident:COATakenType" => "incident/coa.html#stix.incident.coa.COATaken",
    "incident:COATimeType" => "incident/coa.html#stix.incident.coa.COATime",
    "incident:ContributorsType" => "incident/contributors.html#stix.incident.contributors.Contributors",
    "incident:DirectImpactSummaryType" => "incident/direct_impact_summary.html#stix.incident.direct_impact_summary.DirectImpactSummary",
    "incident:EffectsType" => nil,
    "incident:ExternalIDType" => "incident/external_id.html#stix.incident.external_id.ExternalID",
    "incident:ExternalImpactAssessmentModelType" => nil,
    "incident:HistoryItemType" => "incident/history.html#stix.incident.history.HistoryItem",
    "incident:HistoryType" => "incident/history.html#stix.incident.history.History",
    "incident:ImpactAssessmentType" => "incident/impact_assessment.html#stix.incident.impact_assessment.ImpactAssessment",
    "incident:IncidentType" => "incident/incident.html#stix.incident.Incident",
    "incident:IndirectImpactSummaryType" => "incident/indirect_impact_summary.html#stix.incident.indirect_impact_summary.IndirectImpactSummary",
    "incident:JournalEntryType" => "incident/history.html#stix.incident.history.JournalEntry",
    "incident:LeveragedTTPsType" => "incident/incident.html#stix.incident.LeveragedTTPs",
    "incident:LossEstimationType" => "incident/loss_estimation.html#stix.incident.loss_estimation.LossEstimation",
    "incident:NatureOfSecurityEffectType" => nil,
    "incident:NonPublicDataCompromisedType" => "incident/property_affected.html#stix.incident.property_affected.NonPublicDataCompromised",
    "incident:PropertyAffectedType" => "incident/property_affected.html#stix.incident.property_affected.PropertyAffected",
    "incident:RelatedIncidentsType" => "incident/incident.html#stix.incident.RelatedIncidents",
    "incident:RelatedIndicatorsType" => "incident/incident.html#stix.incident.RelatedIndicators",
    "incident:RelatedObservablesType" => "incident/incident.html#stix.incident.RelatedObservables",
    "incident:TimeType" => "incident/time.html#stix.incident.time.Time",
    "incident:TotalLossEstimationType" => "incident/total_loss_estimation.html#stix.incident.total_loss_estimation.TotalLossEstimation",
    "indicator:CompositeIndicatorExpressionType" => "indicator/indicator.html#stix.indicator.indicator.CompositeIndicatorExpression",
    "indicator:IndicatorType" => "indicator/indicator.html#stix.indicator.indicator.Indicator",
    "indicator:RelatedCampaignReferencesType" => nil,
    "indicator:RelatedIndicatorsType" => "indicator/indicator.html#stix.indicator.indicator.RelatedIndicators",
    "indicator:RelatedObservablesType" => "indicator/sightings.html#stix.indicator.sightings.RelatedObservables",
    "indicator:SightingsType" => "indicator/sightings.html#stix.indicator.sightings.Sightings",
    "indicator:SightingType" => "indicator/sightings.html#stix.indicator.sightings.Sighting",
    "indicator:SuggestedCOAsType" => "indicator/indicator.html#stix.indicator.indicator.SuggestedCOAs",
    "indicator:TestMechanismsType" => nil,
    "indicator:TestMechanismType" => nil,
    "indicator:ValidTimeType" => "indicator/valid_time.html#stix.indicator.valid_time.ValidTime",
    "marking:MarkingSpecificationType" => "data_marking.html#stix.data_marking.MarkingSpecification",
    "marking:MarkingStructureType" => "data_marking.html#stix.data_marking.MarkingStructure",
    "marking:MarkingType" => "data_marking.html#stix.data_marking.Marking",
    "simpleMarking:SimpleMarkingStructureType" => "extensions/marking/simple_marking.html#stix.extensions.marking.simple_marking.SimpleMarkingStructure",
    "snortTM:SnortTestMechanismType" => "extensions/test_mechanism/snort_test_mechanism.html#stix.extensions.test_mechanism.snort_test_mechanism.SnortTestMechanism",
    "stix:CampaignsType" => nil,
    "stix:IncidentsType" => nil,
    "stix:IndicatorsType" => nil,
    "stix:RelatedPackagesType" => "core/stix_package.html#stix.core.stix_package.RelatedPackages",
    "stix:RelatedPackageType" => nil,
    "stix:STIXHeaderType" => "core/stix_header.html#stix.core.stix_header.STIXHeader",
    "stix:STIXType" => "core/stix_package.html#stix.core.stix_package.STIXPackage",
    "stix:ThreatActorsType" => nil,
    "stix:TTPsType" => "core/ttps.html#stix.core.ttps.TTPs",
    "stixCommon:ActivityType" => "common/activity.html#stix.common.activity.Activity",
    "stixCommon:AddressAbstractType" => nil,
    "stixCommon:CampaignBaseType" => nil,
    "stixCommon:CampaignReferenceType" => nil,
    "stixCommon:ConfidenceAssertionChainType" => "common/confidence.html#stix.common.confidence.ConfidenceAssertionChain",
    "stixCommon:ConfidenceType" => "common/confidence.html#stix.common.confidence.Confidence",
    "stixCommon:ContributingSourcesType" => "common/information_source.html#stix.common.information_source.ContributingSources",
    "stixCommon:ControlledVocabularyStringType" => "common/vocabs.html#stix.common.vocabs.VocabString",
    "stixCommon:CourseOfActionBaseType" => nil,
    "stixCommon:DateTimeWithPrecisionType" => "common/datetimewithprecision.html#stix.common.datetimewithprecision.DateTimeWithPrecision",
    "stixCommon:EncodedCDATAType" => "common/common.html#stix.common.EncodedCDATA",
    "stixCommon:ExploitTargetBaseType" => nil,
    "stixCommon:ExploitTargetsType" => nil,
    "stixCommon:GenericRelationshipListType" => "common/related.html#stix.common.related.GenericRelationshipList",
    "stixCommon:GenericRelationshipType" => "common/related.html#stix.common.related.GenericRelationship",
    "stixCommon:IdentityType" => "common/identity.html#stix.common.identity.Identity",
    "stixCommon:IncidentBaseType" => nil,
    "stixCommon:IndicatorBaseType" => nil,
    "stixCommon:InformationSourceType" => "common/information_source.html#stix.common.information_source.InformationSource",
    "stixCommon:KillChainPhaseReferenceType" => "common/kill_chains.html#stix.common.kill_chains.KillChainPhaseReference",
    "stixCommon:KillChainPhasesReferenceType" => "common/kill_chains.html#stix.common.kill_chains.KillChainPhasesReference",
    "stixCommon:KillChainPhaseType" => "common/kill_chains.html#stix.common.kill_chains.KillChainPhase",
    "stixCommon:KillChainsType" => "common/kill_chains.html#stix.common.kill_chains.KillChains",
    "stixCommon:KillChainType" => "common/kill_chains.html#stix.common.kill_chains.KillChain",
    "stixCommon:NamesType" => nil,
    "stixCommon:ProfilesType" => nil,
    "stixCommon:ReferencesType" => nil,
    "stixCommon:RelatedCampaignReferenceType" => nil,
    "stixCommon:RelatedCampaignType" => "common/related.html#stix.common.related.RelatedCampaign",
    "stixCommon:RelatedCourseOfActionType" => "common/related.html#stix.common.related.RelatedCOA",
    "stixCommon:RelatedExploitTargetType" => "common/related.html#stix.common.related.RelatedExploitTarget",
    "stixCommon:RelatedIdentitiesType" => "common/identity.html#stix.common.identity.RelatedIdentities",
    "stixCommon:RelatedIdentityType" => "common/related.html#stix.common.related.RelatedIdentity",
    "stixCommon:RelatedIncidentType" => "common/related.html#stix.common.related.RelatedIncident",
    "stixCommon:RelatedIndicatorType" => "common/related.html#stix.common.related.RelatedIndicator",
    "stixCommon:RelatedObservableType" => "common/related.html#stix.common.related.RelatedObservable",
    "stixCommon:RelatedPackageRefsType" => "common/related.html#stix.common.related.RelatedPackageRefs",
    "stixCommon:RelatedPackageRefType" => "common/related.html#stix.common.related.RelatedPackageRef",
    "stixCommon:RelatedThreatActorType" => "common/related.html#stix.common.related.RelatedThreatActor",
    "stixCommon:RelatedTTPType" => "common/related.html#stix.common.related.RelatedTTP",
    "stixCommon:StatementType" => "common/statement.html#stix.common.statement.Statement",
    "stixCommon:StructuredTextType" => "common/structured_text.html#stix.common.structured_text.StructuredText",
    "stixCommon:ThreatActorBaseType" => nil,
    "stixCommon:ToolInformationType" => "common/tools.html#stix.common.tools.ToolInformation",
    "stixCommon:TTPBaseType" => nil,
    "stix-capec:CAPEC2.7InstanceType" => nil,
    "stix-ciqaddress:CIQAddress3.0InstanceType" => nil,
    "stix-ciqidentity:CIQIdentity3.0InstanceType" => "extensions/identity/ciq_identity_3_0.html#stix.extensions.identity.ciq_identity_3_0.CIQIdentity3_0Instance",
    "stix-ciqidentity:STIXCIQIdentity3.0Type" => "extensions/identity/ciq_identity_3_0.html#stix.extensions.identity.ciq_identity_3_0.STIXCIQIdentity3_0",
    "stix:CoursesOfActionType" => nil,
    "stix-cvrf:CVRF1.1InstanceType" => nil,
    "stix-maec:MAEC4.1InstanceType" => "extensions/malware/maec_4_1_malware.html#stix.extensions.malware.maec_4_1_malware.MAECInstance",
    "stix-openioc:OpenIOC2010TestMechanismType" => "extensions/test_mechanism/open_ioc_2010_test_mechanism.html#stix.extensions.test_mechanism.open_ioc_2010_test_mechanism.OpenIOCTestMechanism",
    "stix-oval:OVAL5.10TestMechanismType" => nil,
    "stixVocabs:AssetTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.AssetType",
    "stixVocabs:AttackerInfrastructureTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.AttackerInfrastructureType",
    "stixVocabs:AttackerToolTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.AttackerToolType",
    "stixVocabs:AvailabilityLossTypeVocab-1.0" => nil,
    "stixVocabs:AvailabilityLossTypeVocab-1.1.1" => "common/vocabs.html#stix.common.vocabs.AvailabilityLossType",
    "stixVocabs:CampaignStatusVocab-1.0" => "common/vocabs.html#stix.common.vocabs.CampaignStatus",
    "stixVocabs:COAStageVocab-1.0" => "common/vocabs.html#stix.common.vocabs.COAStage",
    "stixVocabs:CourseOfActionTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.CourseOfActionType",
    "stixVocabs:DiscoveryMethodVocab-1.0" => "common/vocabs.html#stix.common.vocabs.DiscoveryMethod",
    "stixVocabs:HighMediumLowVocab-1.0" => "common/vocabs.html#stix.common.vocabs.HighMediumLow",
    "stixVocabs:ImpactQualificationVocab-1.0" => "common/vocabs.html#stix.common.vocabs.ImpactQualification",
    "stixVocabs:ImpactRatingVocab-1.0" => "common/vocabs.html#stix.common.vocabs.ImpactRating",
    "stixVocabs:IncidentCategoryVocab-1.0" => "common/vocabs.html#stix.common.vocabs.IncidentCategory",
    "stixVocabs:IncidentEffectVocab-1.0" => "common/vocabs.html#stix.common.vocabs.IncidentEffect",
    "stixVocabs:IncidentStatusVocab-1.0" => "common/vocabs.html#stix.common.vocabs.IncidentStatus",
    "stixVocabs:IndicatorTypeVocab-1.0" => nil,
    "stixVocabs:IndicatorTypeVocab-1.1" => "common/vocabs.html#stix.common.vocabs.IndicatorType",
    "stixVocabs:InformationSourceRoleVocab-1.0" => "common/vocabs.html#stix.common.vocabs.InformationSourceRole",
    "stixVocabs:InformationTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.InformationType",
    "stixVocabs:IntendedEffectVocab-1.0" => "common/vocabs.html#stix.common.vocabs.IntendedEffect",
    "stixVocabs:LocationClassVocab-1.0" => "common/vocabs.html#stix.common.vocabs.LocationClass",
    "stixVocabs:LossDurationVocab-1.0" => "common/vocabs.html#stix.common.vocabs.LossDuration",
    "stixVocabs:LossPropertyVocab-1.0" => "common/vocabs.html#stix.common.vocabs.LossProperty",
    "stixVocabs:MalwareTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.MalwareType",
    "stixVocabs:ManagementClassVocab-1.0" => "common/vocabs.html#stix.common.vocabs.ManagementClass",
    "stixVocabs:MotivationVocab-1.0.1" => nil,
    "stixVocabs:MotivationVocab-1.0" => nil,
    "stixVocabs:MotivationVocab-1.1" => "common/vocabs.html#stix.common.vocabs.Motivation",
    "stixVocabs:OwnershipClassVocab-1.0" => "common/vocabs.html#stix.common.vocabs.OwnershipClass",
    "stixVocabs:PackageIntentVocab-1.0" => "common/vocabs.html#stix.common.vocabs.PackageIntent",
    "stixVocabs:PlanningAndOperationalSupportVocab-1.0.1" => "common/vocabs.html#stix.common.vocabs.PlanningAndOperationalSupport",
    "stixVocabs:PlanningAndOperationalSupportVocab-1.0" => nil,
    "stixVocabs:SecurityCompromiseVocab-1.0" => "common/vocabs.html#stix.common.vocabs.SecurityCompromise",
    "stixVocabs:SystemTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.SystemType",
    "stixVocabs:ThreatActorSophisticationVocab-1.0" => "common/vocabs.html#stix.common.vocabs.ThreatActorSophistication",
    "stixVocabs:ThreatActorTypeVocab-1.0" => "common/vocabs.html#stix.common.vocabs.ThreatActorType",
    "ta:AssociatedActorsType" => "threat_actor/threat_actor.html#stix.threat_actor.AssociatedActors",
    "ta:AssociatedCampaignsType" => "threat_actor/threat_actor.html#stix.threat_actor.AssociatedCampaigns",
    "ta:ObservedTTPsType" => "threat_actor/threat_actor.html#stix.threat_actor.ObservedTTPs",
    "ta:ThreatActorType" => "threat_actor/threat_actor.html#stix.threat_actor.ThreatActor",
    "tlpMarking:TLPMarkingStructureType" => "extensions/marking/tlp.html#stix.extensions.marking.tlp.TLPMarkingStructure",
    "TOUMarking:TermsOfUseMarkingStructureType" => "extensions/marking/terms_of_use_marking.html#stix.extensions.marking.terms_of_use_marking.TermsOfUseMarkingStructure",
    "ttp:AttackPatternsType" => nil,
    "ttp:AttackPatternType" => "ttp/attack_pattern.html#stix.ttp.attack_pattern.AttackPattern",
    "ttp:BehaviorType" => "ttp/behavior.html#stix.ttp.behavior.Behavior",
    "ttp:ExploitsType" => nil,
    "ttp:ExploitTargetsType" => "ttp/exploit_targets.html#stix.ttp.exploit_targets.ExploitTargets",
    "ttp:ExploitType" => "ttp/exploit.html#stix.ttp.exploit.Exploit",
    "ttp:InfrastructureType" => "ttp/infrastructure.html#stix.ttp.infrastructure.Infrastructure",
    "ttp:MalwareInstanceType" => "ttp/malware_instance.html#stix.ttp.malware_instance.MalwareInstance",
    "ttp:MalwareType" => nil,
    "ttp:PersonasType" => nil,
    "ttp:RelatedTTPsType" => "ttp/related_ttps.html#stix.ttp.related_ttps.RelatedTTPs",
    "ttp:ResourceType" => "ttp/resource.html#stix.ttp.resource.Resource",
    "ttp:ToolsType" => nil,
    "ttp:TTPType" => "ttp/ttp.html#stix.ttp.TTP",
    "ttp:VictimTargetingType" => "ttp/victim_targeting.html#stix.ttp.victim_targeting.VictimTargeting",
    "yaraTM:YaraTestMechanismType" => nil,
}

$practices = {
    "indicator:IndicatorType" => "sp_indicator.md",
    "marking:MarkingSpecificationType" => "sp_handling.md",
    "stix:STIXHeaderType" => "sp_package.md",
    "stix:STIXType" => "sp_package.md",
    "cybox:ObservableType" => "sp_observable.md",
    "report:ReportType" => "sp_report.md"
}

desc "Regenerate the data model documentation"
task :regenerate do
  # Make Liquid aware of the Jekyll includes directory
  #Liquid::Template.file_system = Liquid::LocalFileSystem.new("_includes")

  # Preload all versions of all schemas first so our introspection can tell what's available
  StixSchemaSpy::Schema::VERSIONS.each do |v|
    if v == StixSchemaSpy::Schema.latest_version
      StixSchemaSpy::Schema.preload!(v, "_schemas/stix") # For the current version use the included submodule schemas, which may have doc updates
    else
      StixSchemaSpy::Schema.preload!(v)
    end
  end

  StixSchemaSpy::Schema::VERSIONS.each do |version|
    # Load the documentation page template
    template = File.read("_layouts/data_model_page.html")

    # Write the file for the data model autocompleter
    json = StixSchemaSpy::Schema.all(version).map {|schema| schema.complex_types}.flatten.map {|type| {:name => type.name, :schema => type.schema.title, :link => type_link(type, version)}}
    File.open("js/autocomplete-#{version}.js", "w") {|f| f.write("window.typeSuggestions = " + JSON.dump(json))}

    # Iterate through all types in the schemas and create pages for them
    StixSchemaSpy::Schema.all(version).each do |schema|
      schema.complex_types.each do |type|
        write_page(type, template, version)
      end
    end
  end
end

def write_page(type, template, version)
  destination = type_path(type, version)

  FileUtils.mkdir_p(destination)

  results = Liquid::Template.parse(template).render(
    'type' => {
      'latest_version' => StixSchemaSpy::Schema.latest_version,
      'this_version' => version,
      'versions' => StixSchemaSpy::Schema::VERSIONS.reject {|v|
        schema = StixSchemaSpy::Schema.find(type.schema.prefix, v)
        (schema && schema.find_type(type.name)).nil?
      },
      'name' => type.name,
      'documentation' => process_documentation(type.documentation.split("\n"), version),
      'schema' => {
        'title' => type.schema.title,
        'prefix' => type.schema.prefix
      },
      'vocab?' => type.vocab?,
      'fields?' => type.fields.length > 0,
      'fields' => fields(type, version),
      'vocab_items' => vocab_items(type),
      'api_link' => python_link(type, version),
      'suggested_practices' => suggested_practices(type)
    }
  )

  File.open("#{destination}/index.html", "w") {|f| f.write(results)}
end

def type_link(type, version)
  "/#{type_path(type, version)}"
end

def type_path(type, version)
  "#{$destination}/#{version}/#{type.schema.prefix}/#{type.name}"
end

def python_link(type, version)
  $stix_uri = $stix_uri_fmt % $python_versions[version]
  prefix = ($stix_prefixes.include? type.prefix) ? $stix_uri : $cybox_uri
  link = $stix_links["#{type.schema.prefix}:#{type.name}"]
  # Only build links if we have a supported version (currently 1.1.1 or 1.2)
  # and there is a corresponding mapping page
  if $python_versions[version] && link then
    prefix + link
  else
    nil
  end
end

def suggested_practices(type)
  $practices["#{type.schema.prefix}:#{type.name}"]
end

def fields(type, version)
  type.fields.map do |field|
    {
      'name' => field.name,
      'link' => (field.type.kind_of?(StixSchemaSpy::ComplexType) && field.type.schema && !field.type.schema.blacklisted?) ? type_link(field.type, version) : false,
      'type' => field.type.name,
      'documentation' => process_documentation(field.documentation.split("\n"), version),
      'occurrence' => field_occurrence(field)
    }
  end
end

def field_occurrence(field)
  if field.kind_of?(StixSchemaSpy::Attribute)
    field.use
  else
    max_occurs = field.max_occurs == 'unbounded' ? 'n' : field.max_occurs
    "#{field.min_occurs}..#{max_occurs}"
  end
end

def vocab_items(type)
  return [] unless type.vocab?

  type.vocab_values.map {|v|
    {
      'name' => v[0],
      'description' => v[1]
    }
  }
end

def process_documentation(docs, version)
  if docs.kind_of?(String)
    add_internal_links(docs, version)
  else
    docs.map {|doc|
      add_internal_links(doc, version)
    }
  end
end

def add_internal_links(doc, version)
  doc
    .gsub(/\S+Vocab-\d(\.\d){1,2}/) {|match| "<a href='/#{$destination}/#{version}/stixVocabs/#{match}'>#{match}</a>"}
    .gsub(/ \S+Type /) do |match|
      name = match.strip
      type = find_type(name)
      if type
        " <a href='#{type_link(type, version)}'>#{name}</a> "
      else
        match
      end
    end
end

def find_type(type)
  types = StixSchemaSpy::Schema.all.map do |schema|
    schema.find_type(type)
  end.compact

  # Only return the found type if we found exactly one, otherwise it's ambiguous
  types.length == 1 ? types.first : nil
end
