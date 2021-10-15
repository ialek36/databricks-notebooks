import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--apikey',  help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args)

print("started test...")
print(args.apikey)

print("finished test...")
