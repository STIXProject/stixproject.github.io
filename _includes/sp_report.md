As of STIX 1.2, the [Report](/data-model/{{site.current_version}}/report/ReportType) construct should be used to give context to a set of STIX content. You'll often see this in cases where a producer wants wrap up some threat intelligence with a common story such as a report about a particular campaign, actor, or piece of malware. The available fields are `Title`, `Intent`, `Description`, `Short_Description`, and `Information_Source`. At least `Title`, `Intent`, and `Information_Source` are recommended.

Note that unlike `STIXType`, the `Information_Source` field does not apply to the content included in the report but simply to the report itself.

Reports allow you to both reference content and embed content in order to denote that it's included in the report. It's generally suggested that you reference content from reports unless you have a good reason to embed it (document size, for example).
