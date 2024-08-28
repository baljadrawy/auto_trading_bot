import pandas as pd
import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_data(data):
    """تحليل البيانات باستخدام Pandas"""
    try:
        df = pd.DataFrame(data)
        summary = df.describe()
        logging.info("تم تحليل البيانات بنجاح")
        return summary
    except Exception as e:
        logging.error(f"حدث خطأ أثناء تحليل البيانات: {e}")
        return None

# مثال على استخدام الدالة
data = [{"symbol": "AAPL", "price": 150.0}, {"symbol": "GOOGL", "price": 2800.0}]
summary = analyze_data(data)
