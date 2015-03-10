# About
Source for [the STIX documentation site](http://stixproject.github.io)

## Getting Help

[![Join the public chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/STIXProject/schemas)

E-mail the developers at <stix@mitre.org>

[Get started with a STIX tutorial](http://stixproject.github.io/getting-started/)

## Contributing
Pull requests welcome! 

We suggest you:
1. Fork the repository
2. Create a feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push your branch to the remote (`git push origin my-new-feature`)
5. Create a Pull Request for your branch


## Building the site locally

1. Install Ruby 1.9.3 or higher for your platform (if it isn't already installed).
1. Install the bundler gem: `gem install bundler`
1. Install the dependencies via bundler: `bundle install`
1. Run the server with `jekyll server` or a static build with `jekyll build`

Note: Jekyll has some "issues" on Windows. See: [Jekyll on Windows](http://jekyllrb.com/docs/windows/#installation) for instructions. The issues I encountered (other than those covered in those instructions) were:
* You'll need to install jekyll version 2.3.0:

```
gem uninstall jekyll # If you already installed it
gem install jekyll --version "=2.3.0"
```

* You'll need to install pygments version 0.5.0:

```
gem uninstall pygments.rb
gem install pygments.rb --version "=0.5.0"
```

If you run into any problems on other platforms, see the [Jekyll Installation Docs](http://jekyllrb.com/docs/installation/). In particular, you'll need to be able to compile native code so on OS X you'll need the Xcode Command Line tools and on Linux you'll need the appropriate build packages (build-essential on Ubuntu, etc). As with most other STIX projects, you'll also need the libxml development libraries installed.

## Running the data model regeneration

In order to run the data model regeneration you'll need to initialize the submodule with the latest version of the STIX schemas in it. To do so:

```
git submodule init
git submodule update
cd _schemas/stix
git submodule init
git submodule update
```

From there, you can run the regeneration via a rake task:

```
rake regenerate
```

