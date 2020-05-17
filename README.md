# RobinTrader

## Setup Virtual Environment (macOS)
1. `python3 -m pip install --user virtualenv`
2. `python3 -m venv env`
3. `source env/bin/activate`

## Login Creds:
Create a file at the root called `env.json` that contains your username and password.
Example:
```
{
    "robin_username": "<YOUR USERNAME>",
    "robin_password": "<YOUR PASSWORD>"
}
```

## References:
- Python Virtual Environments:  https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/