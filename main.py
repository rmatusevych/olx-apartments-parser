from fetch import fetch_page
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="OLX parser script")

  parser.add_argument('--from_price', type=int, required=True, help="Start price for the apartments")
  parser.add_argument('--to_price', type=int, required=True, help='End price for the apartments')

  args = parser.parse_args()

  to_price = args.to_price
  from_price = args.from_price
  city = 'lvov'
  url = f"https://www.olx.ua/uk/nedvizhimost/kvartiry/dolgosrochnaya-arenda-kvartir/{city}/?currency=UAH&search%5Border%5D=created_at:desc&search%5Bfilter_float_price:from%5D={from_price}&search%5Bfilter_float_price:to%5D={to_price}"

  fetch_page(url)

