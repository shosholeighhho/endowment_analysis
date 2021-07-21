import pandas as pd

def main():
	data = pd.read_csv('asset_allocation_data.csv')
	print(data.head(n=10))

if __name__ == '__main__':
	main()
