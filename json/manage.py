import argparse
import json
import time
import os

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

commit_message = f"Add {args.lance_id} lance" if args.delete == False and not payments['data']['lance_status'].get(args.lance_id, None) else f"Delete {args.lance_id}" if args.delete == True  else f"Edit {args.lance_id} lance"

if (not args.delete):
	payments['data']['lance_status'][args.lance_id] = lance_status
	payments['data']['salary'][args.lance_id] = lance_money
else:
	del payments['data']['lance_status'][args.lance_id]
	del payments['data']['salary'][args.lance_id]

json.dump(payments, open("json/payments.json", 'w'))

# Pushing to origin
os.system('git add .')
time.sleep(1)
os.system(f'git commit -am "{commit_message}"')
time.sleep(3)
os.system('git push origin master')