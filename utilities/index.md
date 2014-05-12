---
layout: flat
---

## User-level Tooling

User-level tooling can help abstract away the STIX XML and provide you with different views or capabilities for working with STIX that may not require you to know XML at all. Currently, the two more capable user-level tools are STIXViz and stix_to_html.

### STIXViz

![STIXViz Screenshot](https://github.com/STIXProject/stix-viz/wiki/images/STIXVizExampleFigure1.png)

STIXViz is a tool provided by the STIX project to visualize STIX documents in a tree-type structure. It can show the linkages between various STIX components to help you understand how everything fits together.

The STIXViz tool is packaged and available for download as a Windows executable but is implemented in a combination of HTML and Javascript so, when built from source, is cross-platform or could even be integrated into a webpage.

If you're just starting out in STIX and want to see what it's capable of, I suggest downloading STIXViz and opening up the more complex reports available on the STIX [Samples Page](http://stix.mitre.org/language/version1.0.1/samples.html) (Poison Ivy and APT1) in the tool.

STIXViz also includes stix_to_html as a component, so downloading the packaged build is a 2-for-one.

* [Direct Download (exe)](http://stix.mitre.org/downloads/StixVizDistro.zip)
* [Usage Guide](https://github.com/STIXProject/stix-viz/wiki/STIXViz-Usage)
* [Source Code](https://github.com/STIXProject/stix-viz/)

### stix_to_html

STIX to HTML is an XSLT stylesheet that can take a STIX XML document and turn it into a more readable HTML view. It is used by STIXViz to display individual components as an overlay on the tree view.

Unfortunately, stix_to_html is somewhat harder to use than STIXViz. If you're not familiar with XSLT or how to run it against XML, I would suggest downloading STIXViz and looking at the STIX_to_HTML output that it includes instead.

That said, the XSLT is easy enough to use if you understand how it works and if you run it directly it's easy to transform dozens of STIX documents at once.

* [Usage Guide](https://github.com/STIXProject/stix-to-html/wiki)
* [Source Code](https://github.com/STIXProject/stix-to-html)

## Developer Tools and Utilities

### OpenIOC_to_STIX

OpenIOC_to_STIX is a Python utility to convert Mandiant's OpenIOC format into STIX Indicators (with CybOX observables). This tool was used to generate the Indicators file in the APT1 report mapping on the samples page.

While useful for it's stated purpose, the other way to use this tool is as an example of how to generate STIX content programatically using the bindings. Looking through the source code is a great way to see how they work and how to import/use them, in particular for generating indicators with CybOX content.

* [Source Code](https://github.com/STIXProject/openioc-to-stix)

### stix-validator

STIXValidator is another Python utility that will schema-validate STIX documents and run them through compliance tests

* [Source Code](https://github.com/STIXProject/stix-validator)

## Programmatic Support

### Python

The STIX project currently provides bindings and higher-level APIs to the STIX language through the python-stix project.

* [Source Code](https://github.com/STIXProject/python-stix)
* [Usage Guide](https://github.com/STIXProject/python-stix/wiki/Getting-Started)

### Java

The STIX project does not currently provide bindings, but it should be possible to generate JAXB or XMLBeans bindings from the schemas (with some tweaking). If a community member provides these for STIX 1.0.1, we could link to them from here.

For JAXB, you will essentially need to create a bindings file that resolves some conflicts in the STIX schemas that occur when you turn the XML names into Java names. You'll also likely want a bindings file to put each of the schemas into a reasonable namespace. Finally, you'll run the JAXB generator, specifying the bindings file, against all of the STIX and CybOX schemas.

### .NET

Again, the STIX project does not provide bindings for .NET. Community members, however, have used Microsoft's standard XML tooling to work with STIX documents and create useful utilities.

### Ruby

Using JRuby, it's possible to use generated JAXB or XMLBeans bindings and import them into Ruby via a Rubygem. Though we don't provide this capability, the process is essentially:

* Generate Java bindings
* Package them as a gem
* Include the gem in your Gemfile (if using bundler) or install it manually

We would be happy to link to a Ruby project providing bindings.