import backtrader as bt
import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MyStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if self.dataclose[0] > self.dataclose[-1]:
            self.buy()
        elif self.dataclose[0] < self.dataclose[-1]:
            self.sell()

def run_backtest(data):
    """تشغيل اختبار الاستراتيجية باستخدام Backtrader"""
    try:
        cerebro = bt.Cerebro()
        cerebro.addstrategy(MyStrategy)
        data_feed = bt.feeds.PandasData(dataname=data)
        cerebro.adddata(data_feed)
        cerebro.run()
        logging.info("تم تشغيل اختبار الاستراتيجية بنجاح")
    except Exception as e:
        logging.error(f"حدث خطأ أثناء تشغيل اختبار الاستراتيجية: {e}")

# مثال على استخدام الدالة
import pandas as pd
data = pd.read_csv("historical_data.csv")
run_backtest(data)
