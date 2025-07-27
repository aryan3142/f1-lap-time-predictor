import fastf1
from src.preprocess import prepare_lap_data
from src.model import train_model

fastf1.Cache.enable_cache('cache')
session = fastf1.get_session(2023, 'Silverstone', 'Q')
session.load()

lap_data = prepare_lap_data(session)
score = train_model(lap_data)

print(f"Model trained. R² score: {score:.3f}")
