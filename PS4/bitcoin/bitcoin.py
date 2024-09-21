import requests
import argparse

parser = argparse.ArgumentParser(description="Number of Bitcoins.")
parser.add_argument('number', type=float)
args = parser.parse_args()

def main():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

        if response.status_code == 200:
            price = response.json()
        else:
            print(f'Fail to get the price.')

        p = float(price['bpi']['USD']['rate'].replace(",", ""))
        print(f'${p*args.number}')
    
    except requests.RequestException:
        pass

if __name__ == "__main__":
    main()