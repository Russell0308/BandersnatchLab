from sklearn.ensemble import RandomForestClassifier
import joblib
from datetime import datetime
from app.data import Database

class Machine:

    def __init__(self, df):
        self.name = 'Random Forest Classifier'
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target = df['Rarity']
        features = df.drop('Rarity', axis=1)
        self.model = RandomForestClassifier()
        self.model.fit(features, target)

    def __call__(self, feature_basis):
        prediction = self.model.predict(feature_basis)
        confidence = self.model.predict_proba(feature_basis)
        i = prediction[0].split(' ')[1] 
        confidence = str(confidence[0][int(i)] * 100) + '%'
        return prediction[0], confidence

    def save(self, filepath):
        joblib.dump(self.model, filepath)

    @staticmethod
    def open(filepath):
        model = joblib.load(filepath)
        db = Database()
        df = db.dataframe()
        df.drop(columns=['_id', 'Name', 'Type', 'Damage', 'Timestamp'], inplace=True)
        return Machine(df)

    def info(self):
        return (f'Base model: {self.name} \nTimestamp: {self.timestamp}')
