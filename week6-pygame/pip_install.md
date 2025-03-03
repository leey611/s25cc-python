# Installing Python modules with `pip`
In the python language, there are lots of libraries/modules we can use to make applicaitons. The way we install and manage libraries is to use [`pip`](https://pip.pypa.io/en/stable/installation/).

`pip` is the package manager tool for python that enables you to install packages. `pip` comes along when you install python on your machine.

## Installing a package with `pip install [name-of-package]`
To install a package for your python application, run the command `pip install [name-of-package]`.

To install `pygame`, we run `pip install pygame`. If it doesn't work, try:
- `pip3 install pygame` or
- `python -m pip install pygame` or
- `python3 -m pip install pygame`

## `.venv` (for mac users)
If you are a mac user and using VS code, you might see VS Code pop up a prompt asking you to run the installation on a `.venv`. What is `.venv` and why do we need it?

Because there are many versions in Python and its available packages, we want to safely install packages and not have conflicts with our python's global version. Therefore, a virtual environment (`.venv`) can ensure that we have a safe environment to run certain versions of python and the packages.

## Resources
- [Python Virtual Environments - Full Tutorial for Beginners](https://www.youtube.com/watch?v=Y21OR1OPC9A) by Tech With Tim


