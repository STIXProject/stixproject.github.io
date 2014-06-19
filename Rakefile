require 'bundler'
require 'fileutils'
require 'liquid'
require 'stix_schema_spy'

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
      'documentation' => process_documentation(type.documentation),
      'schema' => {
        'title' => type.schema.title
      },
      'vocab?' => type.vocab?,
      'fields?' => type.fields.length > 0,
      'fields' => fields(type),
      'vocab_items' => vocab_items(type)
    }
  )

  File.open("#{destination}/index.html", "w") {|f| f.write(results)}
end

def type_link(type)
  "/documentation/#{type.schema.prefix}/#{type.name}"
end

def fields(type)
  type.fields.map do |field|
    {
      'name' => field.name,
      'link' => (field.type.kind_of?(StixSchemaSpy::ComplexType) && field.type.schema && !field.type.schema.blacklisted?) ? type_link(field.type) : false,
      'type' => field.type.name,
      'documentation' => process_documentation(field.documentation.split("\n")),
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

def process_documentation(docs)
  if docs.kind_of?(String)
    add_internal_links(docs)
  else
    docs.map {|doc|
      add_internal_links(doc)
    }
  end
end

def add_internal_links(doc)
  doc
    .gsub(/\S+Vocab-\d\.\d/) {|match| "<a href='/documentation/stixVocabs/#{match}'>#{match}</a>"}
    .gsub(/ \S+Type /) do |match|
      name = match.strip
      type = find_type(name)
      if type
        " <a href='/documentation/#{type.schema.prefix}/#{name}'>#{name}</a> "
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