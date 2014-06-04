require 'bundler'
require 'fileutils'
require 'liquid'

Bundler.require

desc "Clean the data model documentation folder"
task :clean do
  blacklist = ['documentation/index.md'] # Files to not delete in the documentation directory
  
  FileUtils.rm_rf(Dir.glob("documentation/*") - blacklist)
end

desc "Regenerate the data model documentation"
task :regenerate do
  StixSchemaSpy::Schema.preload!

  # Load the documentation page template
  template = File.read("_layouts/documentation_page.html")

  # Write the file for the data model autocompleter
  json = StixSchemaSpy::Schema.all.map {|schema| schema.complex_types}.flatten.map {|type| {:name => type.name, :schema => type.schema.title, :link => type_link(type)}}
  File.open("js/autocomplete.js", "w") {|f| f.write("window.typeSuggestions = " + JSON.dump(json))}

  # Iterate through all types in the schemas and create pages for them
  StixSchemaSpy::Schema.all.each do |schema|
    schema.complex_types.each do |type|
      write_page(type, template)
    end
  end
end

def write_page(type, template)
  destination = "documentation/#{type.schema.prefix}/#{type.name}"

  FileUtils.mkdir_p(destination)

  results = Liquid::Template.parse(template).render(
    'type' => {
      'name' => type.name,
      'documentation' => type.documentation,
      'schema' => {
        'title' => type.schema.title
      },
      'vocab?' => type.vocab?,
      'fields?' => type.fields.length > 0,
      'fields' => type.fields.map { |field|
        {
          'name' => field.name,
          'link' => (field.type.kind_of?(StixSchemaSpy::ComplexType) && field.type.schema && !field.type.schema.blacklisted?) ? type_link(field.type) : false,
          'type' => field.type.name,
          'documentation' => field.documentation.split("\n")
        }
      }
    }
  )

  File.open("#{destination}/index.html", "w") {|f| f.write(results)}
end

def type_link(type)
  "/documentation/#{type.schema.prefix}/#{type.name}"
end