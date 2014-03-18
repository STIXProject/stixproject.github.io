require 'json'

module Jekyll

  module Links
    def type_link(type)
      "#{@site.config['root']}/documentation/#{type.schema.prefix}/#{type.name}"
    end
  end

  class DocumentationPage < Page

    include Links

    def initialize(site, base, schema, type)
      @site = site
      @base = base
      @dir = "#{schema.prefix}/#{type.name}/"
      @name = 'index.html'

      # This is really what determines where the file goes. We put it in index.html to avoid having ugly .html extensions in our paths.
      @url = "/documentation/#{type.schema.prefix}/#{type.name}/index.html"

      # This loads the layout file
      read_yaml(File.join(base, '_layouts'), 'documentation.html')

      # Set the data for the page
      self.data['title'] = type.name
      self.data['subtitle'] = schema.title

      self.data['documentation'] = type.documentation.split("\n")

      self.data['test_type'] = type.fields.first.name if type.fields.length > 0

      if type.vocab? # If the type is a default vocabulary, show values from that vocab
        self.data['vocab_items'] = type.vocab_values
      end

      self.data['type_fields'] = type.fields.map do |field|
        {
          'name' => field.name,
          'link' => (field.type.kind_of?(StixSchemaSpy::ComplexType) && field.type.schema && !field.type.schema.blacklisted?) ? type_link(field.type) : false,
          'type' => field.type.name,
          'documentation' => field.documentation.split("\n")
        }
      end
    end
  end

  class DocumentationGenerator < Generator

    include Links

    safe false

    def generate(site)
      @site = site
      # Parse the schemas and generate documentation for each type

      if @site.config['generate_documentation'] && @site.config['generate_documentation'] != 'false'

        require 'stix_schema_spy'

        StixSchemaSpy::Schema.preload! # Load all default schemas

        StixSchemaSpy::Schema.all.each do |schema|
          schema.preload! # Load types and elements from schemas
        end

        # Generate autocomplete data and write it to the site config
        json = StixSchemaSpy::Schema.all.map {|schema| schema.complex_types}.flatten.map {|type| {:name => type.name, :schema => type.schema.title, :link => type_link(type)}}
        File.open("#{site.config['source']}/js/autocomplete.js", "w") {|f| f.write("window.typeSuggestions = " + JSON.dump(json))}

        # Generate a page for each type
        StixSchemaSpy::Schema.all.each do |schema|
          schema.complex_types.each do |type|
            site.pages << DocumentationPage.new(site, site.source, schema, type)
          end
        end
      end
    end
  end
end