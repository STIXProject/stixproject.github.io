---
layout: flat
title: STIX 1.2 (Current)
---

<div class="jumbotron">
  <div class="row">
    <div class="col-md-6 text-center">
      <h3 style="margin-top: 0">Release Notes</h3>
      <ul>
        <li>Addition of the <a href="/data-model/{{site.current_version}}/report/ReportType">report object</a></li>
        <li>Allow for multiple descriptions</li>
        <li>Addition of a <a href="/data-model/{{site.current_version}}/stixVocabs/VersioningVocab-1.0/">vocabulary</a> for versioning STIX content</li>
        <li>Many small fixes to documentation and vocabularies. <a href="https://github.com/STIXProject/schemas/issues?utf8=&q=milestone%3A%22Version+1.2%22+">Full Release Notes.</a></li>
      </ul>
    </div>
    <div class="col-md-6 text-center">
      <p>Want to get it all at once? Get the full download here. Otherwise, see individual downloads below.</p>
      <a class="btn btn-primary btn-lg" role="button" href="http://stix.mitre.org/language/version{{site.current_version}}/stix_v{{site.current_version}}_offline.zip">Full Download <span class="glyphicon glyphicon-download-alt"></span></a>
      <p class="small"><a href="/releases/archive">Release archive</a></p>
    </div>
  </div>
</div>

### Core and Components

|Schema|Version|Schema|Documentation|
|---------|-------|------|-------------|
|Core|1.2|[XSD](http://stix.mitre.org/XMLSchema/core/1.2/stix_core.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/core/1.2/stix_core.html)|
|Common|1.2|[XSD](http://stix.mitre.org/XMLSchema/common/1.2/stix_common.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/common/1.2/stix_common.html)|
|Default Vocabularies|1.2.0|[XSD](http://stix.mitre.org/XMLSchema/default_vocabularies/1.2.0/stix_default_vocabularies.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/default_vocabularies/1.2/stix_default_vocabularies.html)|
|Data Marking|1.2|[XSD](http://stix.mitre.org/XMLSchema/data_marking/1.2/data_marking.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/data_marking/1.2/data_marking.html)|
|Campaign|1.2|[XSD](http://stix.mitre.org/XMLSchema/campaign/1.2/campaign.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/campaign/1.2/campaign.html)|
|Course of Action|1.2|[XSD](http://stix.mitre.org/XMLSchema/course_of_action/1.2/course_of_action.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/course_of_action/1.2/course_of_action.html)|
|Exploit Target|1.2|[XSD](http://stix.mitre.org/XMLSchema/exploit_target/1.2/exploit_target.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/exploit_target/1.2/exploit_target.html)|
|Incident|1.2|[XSD](http://stix.mitre.org/XMLSchema/incident/1.2/incident.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/incident/1.2/incident.html)|
|Indicator|2.2|[XSD](http://stix.mitre.org/XMLSchema/indicator/2.2/indicator.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/indicator/2.2/indicator.html)|
|Report|1.0|[XSD](http://stix.mitre.org/XMLSchema/report/1.0/report.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/report/1.0/report.html)|
|Threat Actor|1.2|[XSD](http://stix.mitre.org/XMLSchema/threat_actor/1.2/threat_actor.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/threat_actor/1.2/threat_actor.html)|
|TTP|1.2|[XSD](http://stix.mitre.org/XMLSchema/ttp/1.2/ttp.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/ttp/1.2/ttp.html)|

### Extensions

|Schema|Extension Point|Version|Schema|Documentation|
|---------|-------|--------|------|-------------|
|CIQ 3.0|Address|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/address/ciq_3.0/1.2/ciq_3.0_address.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/address/ciq_3.0/1.2/ciq_3.0_address.html)
|CAPEC 2.7|Attack Pattern|1.1|[XSD](http://stix.mitre.org/XMLSchema/extensions/attack_pattern/capec_2.7/1.1/capec_2.7_attack_pattern.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/attack_pattern/capec_2.7/1.1/capec_2.7_attack_pattern.html)
|CIQ 3.0|Identity|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/identity/ciq_3.0/1.2/ciq_3.0_identity.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/identity/ciq_3.0/1.2/ciq_3.0_identity.html)
|MAEC 4.1|Malware|1.1|[XSD](http://stix.mitre.org/XMLSchema/extensions/malware/maec_4.1/1.1/maec_4.1_malware.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/malware/maec_4.1/1.1/maec_4.1_malware.html)
|Simple Marking|Marking|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/marking/simple/1.2/simple_marking.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/marking/simple/1.2/simple_marking.html)
|Terms of Use|Marking|1.1|[XSD](http://stix.mitre.org/XMLSchema/extensions/marking/terms_of_use/1.1/terms_of_use_marking.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/marking/terms_of_use/1.1/terms_of_use_marking.html)
|TLP|Marking|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/marking/tlp/1.2/tlp_marking.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/marking/tlp/1.2/tlp_marking.html)
|Generic Structured COA|Structured COA|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/structured_coa/generic/1.2/generic_structured_coa.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/structured_coa/generic/1.2/generic_structured_coa.html)
|Generic Test Mechanism|Test Mechanism|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/test_mechanism/generic/1.2/generic_test_mechanism.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/test_mechanism/generic/1.2/generic_test_mechanism.html)
|OpenIOC|Test Mechanism|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/test_mechanism/open_ioc_2010/1.2/open_ioc_2010_test_mechanism.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/test_mechanism/open_ioc_2010/1.2/open_ioc_2010_test_mechanism.html)
|OVAL 5.10|Test Mechanism|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/test_mechanism/oval_5.10/1.2/oval_5.10_test_mechanism.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/test_mechanism/oval_5.10/1.2/oval_5.10_test_mechanism.html)
|Snort|Test Mechanism|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/test_mechanism/snort/1.2/snort_test_mechanism.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/test_mechanism/snort/1.2/snort_test_mechanism.html)
|Yara|Test Mechanism|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/test_mechanism/yara/1.2/yara_test_mechanism.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/test_mechanism/yara/1.2/yara_test_mechanism.html)
|CVRF|Vulnerability|1.2|[XSD](http://stix.mitre.org/XMLSchema/extensions/vulnerability/cvrf_1.1/1.2/cvrf_1.1_vulnerability.xsd)|[HTML](http://stix.mitre.org/language/version1.2/xsddocs/XMLSchema/extensions/vulnerability/cvrf_1.1/1.2/cvrf_1.1_vulnerability.html)

### Data Dictionaries

Data dictionaries contain all of the objects and properties in the STIX language. Due to several requests, a data dictionary for OASIS CIQ is also available even though it's an external specification. All data dictionaries are Excel files.

* [Core, Common, Vocabularies, and Components](http://stix.mitre.org/language/version1.2/stix_1.2_data_dictionary.xlsx)
* [Extensions](http://stix.mitre.org/language/version1.2/stix_1.2_extensions_data_dictionary.xlsx)
* [OASIS CIQ (External)](http://stix.mitre.org/language/version1.2/oasis_ciq_data_dictionary.xlsx)

### Profile Templates

Profile templates can be used as a starting point to build your own [STIX Profiles](/documentation/profiles). All profile templates are Excel files.

* [STIX/CybOX](http://stix.mitre.org/language/version1.2/stix_1.2_profile_template_r1.xlsx)
* [CybOX Objects](http://stix.mitre.org/language/version1.2/cybox_2.1_objects_profile_template_r1.xlsx)

### Other

* [EDH Data Marking Extension](http://stix.mitre.org/language/version1.2/stix_v1.2_edh_marking_extension.zip) - A zip file with the EDH data marking extension and a few examples of how to use it.
* [Lockheed Martin Kill Chain Definition](http://stix.mitre.org/language/version1.2/stix_v1.2_lmco_killchain.xml) - An XML file with the definition for the Lockheed Martin Cyber Kill Chain.
* [Template Document](http://stix.mitre.org/language/version1.2/stix_v1.2_template.xml) - A template STIX document that can be used as a starting point when creating STIX by hand.
* [STIX 1.2 Online Version](http://stix.mitre.org/language/version1.2/stix_v1.2.zip) - This is equivalent to the full download but the schema locations point to the hosted schemas on stix.mitre.org rather than the local schemas.
