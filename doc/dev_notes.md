Development notes to remind this Ruby programmer how things are done
in the Python world.

# Working with the pypi test server

These command assume that ~/.pypirc has an entry for _pypitest_
(https://testpypi.python.org/pypi).

To register (only once):

    python setup.py register -r pypitest

To publish to the pypi test server:

    python setup.py bdist_wheel upload -r pypitest
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

    python setup.py bdist_wheel upload -r pypi
    python setup.py sdist upload -r pypi

To see the packages installed on the "real" pypi server, send your
browser to:

    https://pypi.python.org/pypi?%3Aaction=pkg_edit&name=rabbit_droppings
