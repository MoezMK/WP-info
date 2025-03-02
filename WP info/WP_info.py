import requests
import sys
import concurrent.futures
import argparse
import csv
import time
import pyfiglet
import random
from tqdm import tqdm


wp_logo = pyfiglet.figlet_format("WP Info")
contact_info = "\nTelegram: @Moezmk0_rt\tGitHub: MoezMK\n"

print("______________________________________________________")
def check_wordpress(url):
    try:
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
            ])
        }
        response = requests.get(f"{url}/wp-json/wp/v2/users", headers=headers, timeout=10)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def fetch_user_data(url):
    try:
        headers = {
            "User-Agent": random.choice([
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"
            ])
        }
        response = requests.get(f"{url}/wp-json/wp/v2/users", headers=headers, timeout=10)
        if response.status_code == 200:
            users = response.json()
            user_data = []
            for user in users:
                user_info = {
                    "id": user.get("id"),
                    "name": user.get("name"),
                    "link": user.get("link")
                }
                user_data.append(user_info)
            return user_data
        else:
            print("[-] Failed to fetch data. Ensure the URL is correct and the site is running WordPress.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[-] An error occurred while connecting to the site: {e}")
        return None

def print_user_data(user_data):
    if user_data:
        print("{:<10} {:<20} {:<50}".format("ID", "Name", "Link"))
        print("-" * 80)
        for user in user_data:
            print("{:<10} {:<20} {:<50}".format(user["id"], user["name"], user["link"]))
    else:
        print("[-] No data to display.")

def export_to_csv(user_data, filename="user_data.csv"):
    if user_data:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Link"])
            for user in user_data:
                writer.writerow([user["id"], user["name"], user["link"]])
        print(f"[+] Data exported to {filename}")
    else:
        print("[-] No data to export.")

def fetch_multiple_urls(urls):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(fetch_user_data, url): url for url in urls}
        for future in tqdm(concurrent.futures.as_completed(future_to_url), total=len(urls), desc="Fetching data"):
            url = future_to_url[future]
            try:
                results.append(future.result())
            except Exception as e:
                print(f"[-] Error fetching data from {url}: {e}")
    return results

def main():
    print(wp_logo)
    print(contact_info)
    print("______________________________________________________\n")
    parser = argparse.ArgumentParser(description="Fetch WordPress user data.")
    parser.add_argument("-u", "--url", help="URL of the WordPress site")
    parser.add_argument("-f", "--file", help="File containing multiple URLs (one per line)")
    parser.add_argument("-o", "--output", help="Output file (CSV format)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
    args = parser.parse_args()

    if not args.url and not args.file:
        print("Usage: python tool.py -u <URL> or -f <file>")
        sys.exit(1)

    urls = []
    if args.url:
        urls.append(args.url.strip("/"))
    if args.file:
        with open(args.file, "r") as file:
            urls = [line.strip("/") for line in file.readlines()]

    valid_urls = []
    for url in urls:
        if check_wordpress(url):
            valid_urls.append(url)
        else:
            print(f"[-] The site {url} is not running WordPress or does not support the REST API.")

    if not valid_urls:
        print("[-] No valid WordPress sites found.")
        sys.exit(1)

    user_data_list = fetch_multiple_urls(valid_urls)
    for user_data in user_data_list:
        print_user_data(user_data)
        if args.output:
            export_to_csv(user_data, args.output)

    # Close the program after completion
    input("\nPress Enter to close the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()
