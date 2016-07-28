---
layout: flat
title: Utilities & Developer Resources
---

## User-level Tooling

User-level tooling can help abstract away the STIX XML and provide you with different views or capabilities for working with STIX that may not require you to know XML at all. Currently, the two more capable user-level tools are `STIXViz` and `STIX to HTML`.

### STIXViz

A visualization tool that renders STIX documents in three unique ways which capture and present hierarchical, relational, and temporal perspectives of the content.

`StixViz` is implemented in Javascript as a standalone application using the node-webkit application runtime which is based on the Chromium rendering engine and node.js. It is packaged and available for download as both a Windows and OSX executable but when built from source, can run on other platforms or could even be integrated into a webpage.

`STIXViz` helps you understand the connections and relationships between the components of a STIX document through three different views:

* __Graph View:__ The Graph View is the default view when visualizing STIX content. STIX constructs are displayed as nodes in a force-directed graph layout. Nodes are connected via their relationships as expressed in the underlying STIX content. This provides a clear, concise view of the connections and relationships between STIX components (e.g., what TTPs are leveraged by a Threat Actor).  
* __Timeline View:__ The Timeline View captures the temporal information of entities within a STIX document and renders that data within a zoomable, scrollable timeline window. Temporal events which span a period of time (i.e., there is a start and end timestamp) are rendered as horizontal bars, while events that occur at a single point in time are rendered as dots along the visual plane. Event types are color coded, as denoted by a legend at the upper right of the timeline view.  
* __Tree View:__ The Tree View renders the components of a STIX document as nodes within a tree structure. The tree presents the structure of a STIX document as well as the relationships between components in a STIX document. Each node can be expanded to show children and related entities, or collapsed to hide them. Nodes can also be double-clicked to focus them, moving the selected node to the root level while also hiding ancestor and sibling nodes.

`STIXViz` also includes the `STIX to HTML` as a component, allowing users to view the details and contents of the rendered nodes.

If you're just starting out in STIX and want to see what it's capable of, we suggest downloading `STIXViz` and opening up the more complex reports available on the [STIX Sample Reports](http://stixproject.github.io/examples/) page (e.g., FireEye Poison Ivy Report and Mandiant APT1 Report) in the tool.

* [Download](https://github.com/STIXProject/stix-viz/releases)
* [Usage Guide](https://github.com/STIXProject/stix-viz/wiki/STIXViz-Usage)
* [Source Code](https://github.com/STIXProject/stix-viz/)

### STIX to HTML

`STIX to HTML` is an XSLT stylesheet that can transform a STIX XML document into a human-readable HTML view. It was designed to be leveraged by developers, either as a mechanism for batch rendering STIX document or to be embedded as a visualization component within a STIX-capable application.

The `STIX to HTML` transform is leveraged by `STIXViz` to display the contents and details of individual components.

Because `STIX to HTML` is an XSLT stylesheet, users must be familiar with XSLT or XSLT processing libraries/engines (e.g., `Saxon` or `libxslt`) in order to use it. If you're not familiar with XSLT or how to run it against XML, we suggest downloading `STIXViz` and looking at the `STIX to HTML` output that it includes instead.

Because `STIX to HTML` was created by and for developers, allowing for customization and extension were a priority. [Documentation](https://github.com/STIXProject/stix-to-html/wiki/Customizing-stix-to-html-transform) on how to customize `STIX to HTML` to fit your application/operational needs is also available. 

* [Usage Guide](https://github.com/STIXProject/stix-to-html/wiki)
* [Source Code](https://github.com/STIXProject/stix-to-html)

## Developer Tools and Utilities
The STIX project develops and maintains utilities for the STIX community which generate, translate, or otherwise leverage STIX content in useful ways. Many of our projects utilize our own developer tools and APIs, so other developers can use these utilities as examples of how to navigate the STIX API landscape!

### OpenIOC to STIX

`OpenIOC to STIX` is a Python utility to convert Mandiant's OpenIOC format into STIX Indicators (with CybOX Observables). This tool was used to generate the Indicators file in the APT1 report mapping on the [STIX Sample Reports](http://stixproject.github.io/examples/) page.

While useful for it's stated purpose, the other way to use this tool is as an example of how to generate STIX content programmatically using the [machine-generated bindings](http://stix.readthedocs.org/en/latest/api_vs_bindings/index.html) included in the `python-stix` APIs. Looking through the source code is a great way to see how they work and how to import/use them, in particular for generating indicators with CybOX content.

* [Source Code](https://github.com/STIXProject/openioc-to-stix)

### STIX Validator (Python)

`STIX Validator` is a command-line Python utility which validates STIX XML documents in three different ways:  

* __XML Schema:__ STIX documents can be validated against the bundled STIX schemas.
* __Suggested Practices:__ STIX documents are validated against [Suggested Practices](/documentation/suggested-practices).
* __STIX Profiles:__ The validator can parse Excel [STIX Profiles](http://stixproject.github.io/documentation/profiles/), convert them into [ISO Schematron](http://www.schematron.com/spec.html) documents and perform validation against the translated Schematron rules.

The `STIX Validator` can also translate Excel STIX Profiles into either [ISO Schematron](http://www.schematron.com/spec.html) or XSLT documents to be used within other applications or validation environments.

* [Source Code](https://github.com/STIXProject/stix-validator)
* [Releases](https://github.com/STIXProject/stix-validator/releases)

### Java STIX Validator

The `Java STIX Validator` is a Java FX application, which can perform STIX XML Schema validation via a graphical user interface.

* [Source Code](https://github.com/STIXProject/java-stix-validator)
* [Releases](https://github.com/STIXProject/java-stix-validator/releases)

## Programmatic Support
The STIX project develops and maintains APIs which aid developers in parsing, creating, and manipulating STIX content programmatically.

### Python APIs (python-stix)

The `python-stix` APIs provide [machine-generated bindings and higher-level APIs](http://stix.readthedocs.org/en/latest/api_vs_bindings/index.html) that aid in the creation, consumption, and manipulation of STIX content. STIX documents can be serialized to and from Python dictionaries, JSON, and schema-valid XML documents.

Our hope is to lift developers above the XML and allow them to focus on creating and parsing cyber threat intelligence as STIX without having to worry about things like XML namespaces, document ordering of elements, or schema locations.

* [Source Code](https://github.com/STIXProject/python-stix)
* [Releases](https://pypi.python.org/pypi/stix/)
* [Documentation](http://stix.readthedocs.org/en/latest/)

### Java

The STIX project provides a [java-stix](https://github.com/STIXProject/java-stix) library for both Java and JAXB XML developers. It provides convenience methods to the XJC generated JAXB model. java-stix is not intended to be a one-for-one replacement for the [python-stix](https://github.com/STIXProject/python-stix) API.

Please send any feedback about java-stix to <{{ site.contact_email }}>.

### .NET

The STIX project does not provide bindings for .NET. Community members, however, have used Microsoft's standard XML tooling to work with STIX documents and create useful utilities.

We would be glad to link to a .NET project providing bindings. Please contact us at <{{ site.contact_email }}>.

### Ruby

Using JRuby, it's possible to use generated JAXB or XMLBeans bindings and import them into Ruby via a Rubygem. Though we don't provide this capability, the process is essentially:

* Generate Java bindings
* Package them as a gem
* Include the gem in your Gemfile (if using bundler) or install it manually

We would be glad to link to a Ruby project providing bindings. Please contact us at <{{ site.contact_email }}>.
