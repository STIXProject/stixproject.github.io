### Background

The [STIX Whitepaper](http://stix.mitre.org/about/documents/STIX_Whitepaper_v1.0.pdf) explains the impetus for standardizing threat data in the security community.

Contact <stix@mitre.org> for a complimentary introduction to the standard and how it can be applied to your data. If you're local to Boston or Washington, DC - training is available in person or via group teleconference. 

### Familiarize yourself with the Data Model and Schemas
In STIX the data model is represented as an XML Schema. The STIX schemas define the canonical STIX data model and the only official way to share STIX information is through XML instance documents that conform to these schemas.

Visit [the release page](http://stix.mitre.org/language/version1.1/) and choose which bundle of content you want to download. The recommended download is the [All Files (Offline)](http://stix.mitre.org/language/version1.1/stix_v1.1_offline.zip) bundle. It contains all STIX schemas, all CybOX schemas, and all extension/external schemas. In other words, everything you need to validate STIX instance documents. We do not suggest using the schemas from this GitHub schemas repository unless you know what you're doing: these are development versions and are not optimized for ease of use.

#### Review the Data Dictionary and Schema Documentation
The best way to familiarize yourself with the data model is to browse through the data dictionaries. These are available on the [release page](http://stix.mitre.org/language/version1.1/) under the "Data Dictionaries" download section. They'll list all of the STIX constructs, their fields, and what it all means.

The schema documentation is also available for those of you that want a little more detail than the data dictionaries but don't want to dig into the XML. This documentation is available on the [release page](http://stix.mitre.org/language/version1.1/), under the "Documentation" column.

### Look through the Samples

If you're like many people, there's no substitute for good sample data when working with a new language or tool. The STIX project has a [samples page](http://stix.mitre.org/language/version1.1/samples.html) for just that reason, containing short, use-case driven samples and longer reports that map to prose reports released by industry. We also have a [[walkthrough|Sample Walkthrough (1.1)]] that takes a look at the IP Watchlist from the samples page and walks you through the various STIX and CybOX concepts that it uses.

## Next Steps
Once you understand the core concepts of how STIX works and have either the schemas or the documentation so you can look up any data model questions, there are a couple options for where to look next:

* If you want to jump right into sample content, see the [[Sample Walkthrough|Sample Walkthrough (1.1)]]
* If you're interested in user-level tooling and programmatic support, go to the [[Tools]] page
* Finally, if you want to get started creating content, you want the [[Authoring Tutorial|Authoring Tutorial (1.1)]]
