Development notes to remind this Ruby programmer how things are done
in the Python world.

# Working with the pypi test server

These command assume that ~/.pypirc has an entry for _pypitest_
(https://testpypi.python.org/pypi).

To register (only once):

    python setup.py register -r pypitest

To publish to the pypi test server:

    python setup.py sdist upload -r pypitest

To install from the pypi test server:

    pip install -i https://testpypi.python.org/pypi rabbit_droppings

To see the packages installed on the pypi test server, send your
browser to:

    https://testpypi.python.org/

## Working with the "real" pypi server

These command assume that ~/.pypirc has an entry for _pypi_
(https://pypi.python.org/pypi).

To register (only once):

    python setup.py register -r pypi

To publish to the "real" pypi server:

    python setup.py sdist upload -r pypi

To see the packages installed on the "real" pypi server, send your
browser to:

    https://pypi.python.org/pypi?%3Aaction=pkg_edit&name=rabbit_droppings

## Why I'm not using wheels

It is possible to distribute the package as a wheel:

    python setup.py bdist_wheel upload -r pypi
    python setup.py bdist_wheel upload -r pypitest

But wheels don't always get used.  The problem is that "pip install"
will install from a wheel, and work.  But installing the package as a
dependency of another package will use the source install, and that
might not work.  By not publishing the wheel at all, we can use "pip
install" to test the source version of the package and ensure it
works.
