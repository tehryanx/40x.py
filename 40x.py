#!/usr/bin/env python3

import sys

pl_file = "./paths.txt"

def read_in():
	return [x.strip() for x in sys.stdin.readlines()]

urls = read_in()

for url in urls:
	# remove trailing slash
	url = url[:-1] if url[-1] == '/' else url
	# target is the last element
	target_path = url.split("/")[-1]
	# url is everything but the final path element
	url = "/".join(url.split("/")[:-1])


	with open(pl_file) as f:
		payloads = f.readlines()

	payloads = [x.rstrip() for x in payloads] 

	for payload in payloads:
		payload = payload.replace("TARGET", target_path)

		print(f"{url}/{payload}")
