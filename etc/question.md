If my local directory is first on `PYTHONPATH` then why is it failing
to import my package instead of one in site-packages?

# Problem Description

The [file bin/rule_cli.py]() adds `../src` to the PYTHONPATH and then
attempts to import `rule.myrule`.

# This works fine initially

If you were to clone [this source code repo]() and then execute the
following:

    shell> python bin/rule_cli.py

You would see that `rule.myrule` loaded successfully.

## But then if you install rule from pypi it fails

If you then install rule from PyPi:

    shell> pip install rule

### Now the same invocation fails:

[This
gist](https://gist.github.com/metaperl/7d0dc5d011850edc5346fdaa82167760)
shows a failed execution with the error `ModuleNotFoundError: No
module named 'rule.myrule'`

# So my question is:

If the `PYTHONPATH` clearly has the `src` directory of the local repo
first on the `PYTHONPATH` then how can `import rule.myrule` fail?

## My next question is:

What can I do so that `import rule.myrule` works when `rule` from PyPI
installed?

# Bibliography

* https://www.reddit.com/r/learnpython/comments/hl1msg/if_my_local_directory_is_first_on_pythonpath_then/

* https://www.reddit.com/r/learnpython/comments/hl19ri/is_there_a_tool_that_names_all_pypi_modules/
