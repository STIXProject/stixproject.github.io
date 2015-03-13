# stixproject.github.io

This repository is used to build http://stixproject.github.io. If you're looking for documentation about STIX, you should head over there now, or go straight to the [Getting Started page](http://stixproject.github.io/getstarted/).

If you're looking for information about editing the content on the site, you're in the right place!

## Installation

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

## Contributing

The STIX Project welcomes contributions to our documentation repository. If you have a change you want to make:

1. Fork this repository
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

You can also speak to the STIX team by e-mailing stix@mitre.org and we can make the change for you.
