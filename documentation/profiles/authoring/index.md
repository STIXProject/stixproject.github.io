---
layout: flat
title: Authoring profiles
---

## Getting Started: What type of profile should I create? 

The first step to creating a profile is to understand which type of profile you want to create. In general, profiles can be bucketed into a few types, and by understanding the type of profile you want to create you can ask yourself the right questions about what to include. A writeup of the different types of profiles is contained in the [profiles guide](..).

For the example in this document, we'll be creating a community profile that will allow a number of organizations to exchange basic indicator information.

## Step 1: Get the templates

Download the [profile template](http://stix.mitre.org/language/profiles.html#documentation) for the version of STIX that you want to create a profile for. If you plan to use just STIX and its extensions, the STIX Profile Template is enough. If you plan to go into details on how CybOX objects are supported, download the CybOX Object Profile Template Tabs as well.

Make sure to copy or rename the STIX template to whatever is appropriate for the profile you're creating.

## Step 2: Populate the overview

As explained in the [representation guide](../representation), the Overview tab of a profile gives a high level picture of what a profile is all about. Configuring that is an entirely manual process by the author of the profile, so we'll need to go through that now.

Open up the STIX template and select the overview tab. Fill in the information appropriately under "Profile Information" and "Description".

Next, go down the list of STIX Components, Features, etc. and select the correct value in column B from the dropdown. If you aren't sure about any of the values just make sure to come back and set them correctly later: as explained above, they will not be automatically set based on what you change in the details tabs.

## Step 3: Prepare the template

The template will probably include extra tabs that you won't need. For example, if you aren't using Threat Actor in your profile you can hide or delete that tab.

Similarly, if you plan to use CybOX objects those tabs will need to be copied from the CybOX Object Template Tab. Make sure to put them before the "Namespaces" and "Instance Mapping" tabs so you don't confuse people.

## Step 3: Start with STIX Core

Starting with the STIX Core tab, STIXType type, follow this process:

1. Iterate through each field in the type, setting the values appropriately:
  a. Mark the field's occurrence to required, suggested, optional, or prohibited
  b. If the field is a controlled vocabulary or extension point and you want to restrict the allowable implementations, fill in the fully-qualified xsi:types for the allowable values in the Implementation column, separated by commas. For example, to restrict a field to either TLP marking or simple marking use: "simpleMarking:SimpleMarkingStructureType, tlpMarking:TLPMarkingStructureType". The allowable namespace prefixes are listed in the "Namespaces" tab.
  c. For simple value types, if you want to restrict the value of the field fill in the allowable values in the Values column, once again separated by commas.
  d. Enter any notes or other miscellaneous validation requirements in the Notes column.

2. Any type that is permitted in your profile (i.e. might potentially appear in instance documents) will need to be coded. These types fall into the categories of:
  a. Types for fields that you've marked as optional, suggested, or required.
  b. xsi:types that are permitted (not necessarily required, just permitted) for fields that are marked as optional, suggested, or required
  c. As a special case, make sure to cover all CybOX objects you might use.
  d. You can skip controlled vocabularies as long as you encode the parent type, since the child types don't have any extra fields on top of those.

3. Rinse and repeat steps 1-2 until you finish all types.

4. Types that are completely unused (i.e. are not going to appear in instance documents because all instances are prohibited) can be hidden or deleted.

<img src="flowchart.png" alt="flowchart" />

## Step 4: Cleanup and summarize

Go through the profile again and make sure the summary matches the details. Many people who will look at your profile will only glance at the summary tab, so it's important that it reflects reality.

You can also take this time to make sure any tabs you don't need are hidden or deleted and all type rows that you don't need are hidden or deleted. While not necessary, it will reduce some noise and make it easy for people to see what actually falls into your profile.
