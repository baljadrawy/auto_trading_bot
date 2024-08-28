import tensorflow as tf
import logging

# إعداد التسجيل
logging.basicConfig(filename='../logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_model(input_shape):
    """إنشاء نموذج تعلم آلي باستخدام TensorFlow"""
    try:
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=input_shape),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        logging.info("تم إنشاء نموذج تعلم الآلة بنجاح")
        return model
    except Exception as e:
        logging.error(f"حدث خطأ أثناء إنشاء نموذج تعلم الآلة: {e}")
        return None

# مثال على استخدام الدالة
model = create_model((10,))
