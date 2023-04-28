Touch: A Plugin for Pelican
===========================

[![Build Status](https://img.shields.io/github/actions/workflow/status/pelican-plugins/touch/main.yml?branch=main)](https://github.com/pelican-plugins/touch/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-touch)](https://pypi.org/project/pelican-touch/)
![License](https://img.shields.io/pypi/l/pelican-touch?color=blue)

This Pelican plugin sets the date on generated files based on source content `Date:` metadata.

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-touch

Usage
-----

This plugin performs `touch` on your generated files, using the date metadata from the source content.

This helps, among other things, to guide the web server regarding how to handle its cache.

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.

[existing issues]: https://github.com/pelican-plugins/touch/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the AGPL-3.0 license.
