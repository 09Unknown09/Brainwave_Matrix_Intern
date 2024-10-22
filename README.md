
# Phishing Link Scanner

The Phishing Link Checker is a Python script designed to help identify potential phishing URLs by analyzing various indicators and content. This tool can be useful for security professionals and individuals looking to protect themselves from phishing attacks.


## Features

- Checks for common phishing indicators in the URL.
- Identifies suspicious Top-Level Domains (TLDs).
- Scans for suspicious content in the webpage.
- It handles different types of URLs (HTTP, HTTPS, shortened URLs, IP-based URLs)
- Works on multiple platforms (Windows, macOS, Linux), ensuring that it can be deployed in a variety of environments.


## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

To install the required libraries, you can use `pip`:

```bash
 pip install requests beautifulsoup4

```



## Usage
1. Clone the repository:

```
git clone https://github.com/09Unknown09/phishing-link-checker.git
```
```
cd phishing-link-checker
```
2. Run the script:
```
python Phishing Link Scanner.py
```
3. Enter the URL to check when prompted.
## Example
Here is an example of how the script can be used:
```
Enter the URL to check: http://example.com
```
The script will analyze the URL and print whether it is likely safe or contains phishing indicators.
## Acknowledgements


- Inspired by various open-source projects and security tools.
- Special thanks to the Brainwave Matrix Solution who have helped improve this script.

## Disclaimer
This tool is for educational purposes and should be used responsibly. Always ensure you have authorization to test the security of any assets.
## License

This project is licensed under the MIT License. See the [MIT](https://choosealicense.com/licenses/mit/) file for more details.

