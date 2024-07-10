# DirScan
usage: directory_scanner.py [-h] [-u URL] -w WORDLIST [-o OUTPUT] [-m {GET,POST}] [-l LIST]

Directory Scanner for Web Application Testing

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL
  -w WORDLIST, --wordlist WORDLIST
                        Path to wordlist file
  -o OUTPUT, --output OUTPUT
                        Output file to save found directories
  -m {GET,POST}, --method {GET,POST}
                        HTTP method to use (default: GET)
  -l LIST, --list LIST  Path to file containing list of target URLs
