import tensorflow as tf
import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def predict_prices(model, data):
    """التنبؤ بالأسعار باستخدام النموذج المدرب"""
    try:
        predictions = model.predict(data)
        logging.info("تم التنبؤ بالأسعار بنجاح")
        return predictions
    except Exception as e:
        logging.error(f"حدث خطأ أثناء التنبؤ بالأسعار: {e}")
        return None

# مثال على استخدام الدالة
# data هو مجموعة البيانات التي ستقوم بتقديمها للنموذج المدرب للتنبؤ بالأسعار.
