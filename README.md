userinfo
===

CLI tool for exporting user information into JSON or CSV file.

## Usage

Pass in the format (`JSON` by default) and the destination file (`stdout` by default)

Example for CSV format:
```
$ userinfo --format=csv --path=/path/to/users.csv
```

## Installation From Source

To install the package after you've cloned the repository, you'll
want to run the following command from within the project directory:
```
$ pip install --user -e .
```

## Preparing for Development

Follow these steps to start developing with this project:

1. Ensure `pip` and `pipenv` are installed
2. Clone repository: `git clone git@github.com:xledbd/userinfo`
3. `cd` into the repository
4. Activate virtualenv: `pipenv shell`
5. Install dependencies: `pipenv install`
