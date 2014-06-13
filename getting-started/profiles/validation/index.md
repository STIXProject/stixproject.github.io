---
layout: getting_started
title: Profile validation
---

STIX [Profiles](..) are a mechanism to describe a particular usage of STIX as practiced by a community, organization, or tool. Profiles are represented using a [specially-formatted Excel spreadsheet](../representation). Instance documents may be automatically validated against that spreadsheet to determine whether they conform with it.

## Background

Although profiles are useful for developers, analysts, and business owners to arrive at a common understanding of a STIX data exchange, they can also be used to automatically validate that a particular STIX instance document conforms to the requirements that they define. This capability can be used in development to ensure that the developed tool conforms to the profile requirements or in production to ensure that produced or consumed documents conform.

Profile validation should not be considered the last word in the conformance of a STIX document to the profile, however. Certain profile rules in any given profile may not be automatically validatable (if field A is present, field B must be present is not currently supported, for example) and therefore some manual steps must also be taken to ensure compliance. That said, automated validation can test for the vast majority of important rule use cases and therefore can be a good start.

Profile validation requires that the profile is [authored](../authoring) such that the automated capabilities are fully supported. In general this happens automatically but there are several special cases outlined in the authoring guide that must be followed. Generally, the profile validator will throw an error if this is not the case but in certain edge cases this might not happen and the validation might give a false positive or false negative.

## Using the STIX Validator

The STIX validator is a command-line utility written in Python and available [on Github](https://github.com/STIXProject/stix-validator). To use it, you'll need to follow the install instructions in the README (including install Python if you don't have it already) and then clone the source code into some directory.

The validator has two options for validating against profiles: you can pass it an instance document and a profile and it will tell you whether the instance document conforms to the profile, and you can pass it just a profile and it will output an XSLT file or Schematron schema that can then be used by XSLT or Schematron tools to validate instance documents without requiring the validator logic.

### Generating XSLT and Schematron

To generate XSLT, run the following command from the command line:

```
python sdv.py --profile <stix_profile.xlsx> --xslt-out <stix_profile.xslt> --schematron-out <stix_profile.sch>
```

### Evaluating instance documents

```
python sdv.py --input-file <stix_document.xml> --schema-dir schema --profile <stix_profile.xlsx>
```

Note that this will validate both against the STIX schemas and against the profile. If schema validation fails, profile validation will not be run.

The output should be fairly straightforward if you have a successful validation:

```
[-] Processing 1 files
[-] Validating STIX document examples/ex02.xml against XML schema...
[-] Validating STIX document examples/ex02.xml against profile examples/Example_Profile.xlsx...
[+] XML schema validation results: examples/ex02.xml : VALID
[+] Profile validation results: examples/ex02.xml : VALID
```

This indicates that the document is valid against both the schemas and the profile. If validation fails, it will indicate this as INVALID and will include a list of errors.

## Understanding Errors

If the document is not valid against the profile the validator will go you an explanation as to why. Each error consists of the message and the line number(s) that the error applies to.

<table class="table table-bordered table-hover table-condensed">
  <thead>
    <tr>
      <th>Error</th>
      <th>Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>[FIELD] is prohibited by this profile</td>
      <td>The given field is not allowed to be present per the profile but was found in the instance document. The field must be removed for the document to be valid.</td>
    </tr>
    <tr>
      <td>[FIELD] is required by this profile</td>
      <td>The given field is required but was not found in the instance document. The field must be added for the document to be valid.</td>
    </tr>
    <tr>
      <td>The allowed xsi:types for [FIELD] are [TYPE LIST]</td>
      <td>This indicates that the field requires a specific list of possible xsi:types (implementations for an extension point) and either no xsi:type was used or one outside the allowable list was used. The xsi:type (implementation) must be changed to one from the list for the document to be valid.</td>
    </tr>
    <tr>
      <td>The allowed values for [FIELD] are [VALUE LIST]</td>
      <td>This indicates that the field requires a specific set of possible values and one outside this list was used. The field value must be changed to one from the list for the document to be valid.</td>
    </tr>
  </tbody>
</table>

## Questions?

Profiles are a complicated topic and profile validation is a complicated part of that topic. Please [get in touch](mailto:stix@mitre.org) with the team if you have any questions or think this documentation could be improved.

If you encounter any errors with the validator, please open an issue in the [issue tracker](https://github.com/STIXProject/stix-validator/issues).