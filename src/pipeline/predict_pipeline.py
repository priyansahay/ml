import sys
import pandas as pd
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='artificats\model.pkl'
            preprocessor_path='artificats\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transfrom(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,
        gender: str,
        race_ethnicty: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score:int):

        self.gender = gender
        self.race_ethnicty = race_ethnicty
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
        
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {

                'gender' : [self.gender],
                'race_ethnicty' : [self.race_ethnicty],
                'parental_level_of_education' : [self.parental_level_of_education],
                'lunch' : [self.lunch],
                'test_preparation_course' : [self.test_preparation_course],
                'reading_score' : [self.reading_score],
                'writing_score' : [self.writing_score]

            }
            return pd.DataFrame(custom_data_input_dict)
        
        
        except Exception as e:
            return CustomException(e,sys)
    