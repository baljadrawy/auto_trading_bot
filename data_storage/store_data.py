from pymongo import MongoClient
import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def store_data(data, collection_name):
    """تخزين البيانات في قاعدة بيانات MongoDB"""
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["trading_db"]
        collection = db[collection_name]
        collection.insert_many(data)
        logging.info(f"تم تخزين البيانات في مجموعة {collection_name} بنجاح")
    except Exception as e:
        logging.error(f"حدث خطأ أثناء تخزين البيانات: {e}")

# مثال على استخدام الدالة
data = [{"symbol": "AAPL", "price": 150.0}, {"symbol": "GOOGL", "price": 2800.0}]
store_data(data, "market_prices")
