import requests
import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/market_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_market_data(api_url):
    """جلب بيانات السوق من API"""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        logging.info("تم جلب بيانات السوق بنجاح")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"حدث خطأ أثناء جلب بيانات السوق: {e}")
        return None

# مثال على استخدام الدالة
api_url = "https://api.example.com/marketdata"
market_data = get_market_data(api_url)
