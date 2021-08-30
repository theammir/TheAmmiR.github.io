import argparse
import json
import subprocess

__parser = argparse.ArgumentParser()

__parser.add_argument("lance_id", type=str)
__parser.add_argument("lance_money", nargs='?', type=str, default="0")
__parser.add_argument("lance_status", nargs="?", type=str)
__parser.add_argument("-d", "--delete", action='store_true')


args = __parser.parse_args()

lance_status = args.lance_status
lance_money = float(args.lance_money.strip("$"))
if (args.lance_status == "0"):
	lance_status = 'did-not'
elif (args.lance_status == "1"):
	lance_status = 'waiting'
elif (args.lance_status == "2"):
	lance_status = 'ok'

payments = json.load(open("json/payments.json", 'r'))
if (not args.delete):
	payments['data']['lance_status'][args.lance_id] = lance_status
	payments['data']['salary'][args.lance_id] = lance_money
else:
	del payments['data']['lance_status'][args.lance_id]
	del payments['data']['salary'][args.lance_id]

json.dump(payments, open("json/payments.json", 'w'))

# Pushing to origin
subprocess.Popen(f'git commit -am "Add {args.lance_id} lance"', shell=True)
subprocess.Popen('git push origin master')