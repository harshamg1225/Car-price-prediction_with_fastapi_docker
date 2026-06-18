import joblib
import pandas as pd

from app.cache.redis_cache import get_cached_prediction, set_cached_prediction
from app.core.config import setting


modle = joblib.load(setting.MODEL_PATH)


def predict_car_price(data: dict):
    cache_key = " ".join([str(i) for i in data.values()])

    cached = get_cached_prediction(cache_key)

    if cached:
        return cached

    input_data = pd.DataFrame([data])

    prediction = modle.predict(input_data)[0]

    set_cached_prediction(cache_key, prediction)
    return prediction
