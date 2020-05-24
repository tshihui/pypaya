if __name__ == '__main__':
    print('Virtual Environment')
    print('a self-contained directory that contains python installation of\n'
          'a certain version of python + additional packages')
    print("changes to version in venv of program A will not interfere with\n"
          "version of another program running on another venv")

    print('\nCreating virtual environments')
    print('venv module can create and manage virtual environments')
    print('1. decide a directory and then run the venv module\n'
          'for eg: python3 -m venv tutorial-env\n'
          'creating tutorial-env environment -- directory, a copy of python interpreter\n'
          'standard library, and supporting files.')
    print('After creating the venv, you can activate it by running\n'
          'source tutorial-env/bin/activate')

    print('\nManaging packages with pip')
    print('pip by default install packages from pypi.org')
    print('pip also has a limited search function pip search xxxx')
    print('installation of a specific version of package can be achieved by\n'
          'pip install packageName==versionYouWant')
    print('if version already exists, pip will just not do anything.')
    print('pip install --upgrade packageName, will upgrade packages to latest version without specify version')
    print('pip uninstall packageName, will uninstall the package')
    print('pip show packageName will display information about a package')
    print('pip list shows all the packages installed in the environment')
    print('pip freeze > requirements.txt will save the list of packages with versions into txt file')
    print('for another person on another environment to have the same versions, he will have to perform:\n'
          'pip install -r requirements.txt')
