Project to work with GitHub.

# Requirements

- Python 3.6+.

- Python3 venv.

~~~
sudo apt-get install python3-venv
~~~

- Bash terminal.

- Git.

~~~
sudo apt-get install git
~~~

# Run

Download GitHub required projects:

~~~
/bin/bash download_repositories
~~~

Create a virtual environment:

~~~
python3 -m venv env
~~~

Activate the virtual environment:

~~~
source env/bin/activate
~~~

Install requirements:

~~~
/bin/bash install_pip
~~~

Run the module:

~~~
python github.py
~~~
