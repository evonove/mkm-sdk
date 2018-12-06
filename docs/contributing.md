Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs at https://github.com/evonove/mkm-sdk/issues

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

### Write Documentation

mkmsdk could always use more documentation, whether as part of the
official mkmsdk docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback

The best way to send feedback is to file an issue at https://github.com/evonove/mkm-sdk/issues

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `mkmsdk` for local development.

Fork the `mkmsdk` repo on GitHub and clone your fork locally:

    git clone git@github.com:your_name_here/mkmsdk.git

Install your local copy into a virtualenv. Assuming you have `virtualenvwrapper` installed, this is how you set up your fork for local development:

    $ mkvirtualenv mkmsdk
    $ cd mkmsdk/
    $ pip install -r requirements/dev.txt

Create a branch for local development so that you make your changes locally:

    $ git checkout -b name-of-your-bugfix-or-feature

When you're done making changes, check that your changes pass the tests, including testing
other Python versions with tox:

    $ tox

To get tox, just pip install it into your virtualenv.

Commit your changes and push your branch to GitHub:

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

Submit a pull request through the GitHub website and wait for it to be accepted!

## Code formatting

Every contribution must be formatted with the `black` code formatter.
This arguments must be used `--line-length 120 --py36 --skip-numeric-underscore-normalization`.

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for every Python version currently supported.