from vital.client import Vital
from vital.environment import VitalEnvironment
import config


class VitalDataFetcher:
    def __init__(self,api_key,environment):
        self.client = Vital(api_key=api_key,environment=environment)

    def get_blood_pressure_data(self,user_id,start_date,end_date):
        response = self.client.vitals.blood_pressure(
            user_id = user_id,
            start_date = start_date,
            end_date = end_date
        )
        return response


def main():
    api_key = config.API_KEY
    environment = VitalEnvironment.SANDBOX
    fetcher = VitalDataFetcher(api_key,environment)
    user_id = config.user_id
    start_date = "2025-01-10"
    end_date = "2025-01-16"

    blood_pressure_data = fetcher.get_blood_pressure_data(user_id,start_date,end_date)
    
    print(blood_pressure_data)

if __name__ =="__main__":
    main()    

