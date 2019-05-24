#!/usr/bin/env python3
import argparse
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("domain")
    parser.add_argument("-c", "--concurrency", default=1, type=int)
    parser.add_argument("-r", "--requests", default=1, type=int)
    arguments = parser.parse_args()

    number_of_requests = max(arguments.concurrency, arguments.requests)

    print(f"Concurrency: {arguments.concurrency}")
    print(f"   Requests: {number_of_requests}")

    status_codes = Counter()

    with requests.Session() as session:
        start = time.time()
        with ThreadPoolExecutor(max_workers=arguments.concurrency) as pool:
            futures = []
            for request_number in range(number_of_requests):
                url = f"http://{arguments.domain}/{request_number}"
                futures.append(pool.submit(request_function, session, url))

            for future in as_completed(futures):
                status_codes[future.result()] += 1
            duration = time.time() - start

    print(f"   Duration: {duration:5.2f}\n")
    print("Status code counts")
    for (status_code, count) in status_codes.most_common():
        print(f"  {status_code}: {count}")


def request_function(session, url):
    try:
        return session.get(url, timeout=16).status_code
    except Exception as exception:
        return str(exception)


if __name__ == "__main__":
    sys.exit(main())
