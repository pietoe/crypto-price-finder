from bs4 import BeautifulSoup
import requests

def find_crypto(crypto_coin):
    try:
        url = f"https://www.google.com/finance/quote/{crypto_coin}-CAD"
        HTML = requests.get(url).text
        soup = BeautifulSoup(HTML, 'html.parser')
        bitcoin = soup.find(class_="YMlKec fxKbKc").text.replace(",","")
    
    
    
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"
        
    return(bitcoin)