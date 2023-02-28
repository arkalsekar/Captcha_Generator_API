# Captcha Generator API

A Simple Web API created using Python Flask and PIL/OpenCV Library which can generate Captchas and can be used to Verify Captchas as well.

## Installation

Either Download the zip file or clone the repository using github cli.

```bash
git clone https://github.com/arkalsekar/Captcha_Generator_API.git
```

## Usage

It is pretty simple to start download the requirements and set it up locally.

Firstly, Downlaod the requirements by using the following command.
```bash
pip install -r requirements.txt
```

Now, Run the Application using the following Command.
```bash
python app.py
```

## Endpoints

Currently, we have only one endpoint ie 

```bash 
/getCaptcha
```
But sending a ```GET``` request to at the above endpoint, you will get bytes of the Captcha Image and a Captcha as a String.
You can use the Bytes to construct captcha image and display it to the users and use Captcha Text to verify, whether the captcha entered is correct or not. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
