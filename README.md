# Usage Instructions

MassMailer is a free open source recursive email sender based on python. It utilizes CSV files 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
git clone github.com/0xGassin/MassMailer
```

```bash
cd MassMailer
```

```bash
pip3 install -r requirements.txt
```

## Setup

In order for the mailer to work, you will need to create an app password within your gmail account and replace the credentials given to you by gmail with the credentials in the .env file.

1) Head over to this URL and login
```
https://myaccount.google.com/apppasswords
```

2) Chose 'Custom', give it a name and copy the password generated. Then paste that password in the .env file and add it to APPPASSWORD, here you can also change the EMAILADDRESS to your email.

Please make sure to update tests as appropriate.

## Usage

```txt
Usage:
    python3 main.py -i <inputfile>
    python3 main.py --input <inputfile>

    Templates:
    Option 1: Uses template 1
    You can add as many templates as you need, however you will need to rewrite the logic for choosing the templates if you add more than the default amount (3)

```

## License

[MIT](https://choosealicense.com/licenses/mit/)
