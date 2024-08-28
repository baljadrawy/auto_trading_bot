import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def set_trading_goals(predictions, threshold=0.05):
    """وضع أهداف التداول بناءً على التنبؤات"""
    try:
        goals = []
        for prediction in predictions:
            if prediction > threshold:
                goals.append("شراء")
            else:
                goals.append("بيع")
        logging.info("تم وضع أهداف التداول بنجاح")
        return goals
    except Exception as e:
        logging.error(f"حدث خطأ أثناء وضع أهداف التداول: {e}")
        return None

# مثال على استخدام الدالة
predictions = [0.1, 0.03, 0.07]
goals = set_trading_goals(predictions)
print(goals)
