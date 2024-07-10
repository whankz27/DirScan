import argparse
import requests

def scan_directories(url, wordlist_file, output_file, method):
    found_directories = []

    try:
        with open(wordlist_file, 'r') as file:
            directories = file.readlines()
    except FileNotFoundError:
        print(f'[!] File not found: {wordlist_file}')
        return

    for directory in directories:
        directory = directory.strip()
        full_url = f'{url}/{directory}/'
        try:
            if method.upper() == 'GET':
                response = requests.get(full_url)
            elif method.upper() == 'POST':
                response = requests.post(full_url)
            else:
                print(f'[!] Unsupported HTTP method: {method}')
                return

            if response.status_code == 200:
                print(f'[+] Directory found: {full_url}')
                found_directories.append(full_url)
            else:
                print(f'[-] Directory not found: {full_url}')
        except requests.exceptions.RequestException as e:
            print(f'[!] Error: {e}')
            continue

    if output_file:
        try:
            with open(output_file, 'w') as file:
                for directory in found_directories:
                    file.write(directory + '\n')
            print(f'[+] Output saved to: {output_file}')
        except Exception as e:
            print(f'[!] Error writing to output file: {e}')

def scan_list_of_targets(target_list_file, wordlist_file, output_file, method):
    try:
        with open(target_list_file, 'r') as file:
            targets = file.readlines()
    except FileNotFoundError:
        print(f'[!] File not found: {target_list_file}')
        return

    for target in targets:
        target = target.strip()
        print(f'\nScanning target: {target}')
        scan_directories(target, wordlist_file, output_file, method)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Directory Scanner for Web Application Testing")
    parser.add_argument('-u', '--url', type=str, help="Target URL")
    parser.add_argument('-w', '--wordlist', type=str, required=True, help="Path to wordlist file")
    parser.add_argument('-o', '--output', type=str, help="Output file to save found directories")
    parser.add_argument('-m', '--method', type=str, choices=['GET', 'POST'], default='GET', help="HTTP method to use (default: GET)")
    parser.add_argument('-l', '--list', type=str, help="Path to file containing list of target URLs")

    args = parser.parse_args()

    if args.list:
        scan_list_of_targets(args.list, args.wordlist, args.output, args.method)
    elif args.url:
        scan_directories(args.url, args.wordlist, args.output, args.method)
    else:
        print('[!] Either --url or --list must be provided')
        parser.print_help()
