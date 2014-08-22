### Controlled Structure XPaths

The XPath specified in a data marking controlled structure field must select all fields (elements and attributes) that the marking will be applied to. It is not sufficient to select only the root element using the `/` character. Instead, you should use the `node()` function to select relevant nodes. For example, to select the entire document you should use `//node()` while to select a parent construct (Indicator, for example), you could use `ancestor-or-self::stix:Indicator//node()`.

As noted in the annotations, prefixes are valid if they are declared in scope of the Controlled_Structure element.
