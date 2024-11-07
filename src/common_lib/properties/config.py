from dotenv import load_dotenv
import boto3
import os

from common_lib.util.singleton import Singleton

class Config(metaclass=Singleton):
    is_lambda = False
    def __init__(self):
        pass
        
    def load_config_file(self, config_file: str):
        load_dotenv(config_file, override = False)
        self.is_lambda = False
    
    def get_property(self, key: str, with_decryption: bool = False):
    
        if not self.is_lambda:
            return os.getenv(key)
        else:
            ssm = boto3.client('ssm')    
            response = ssm.get_parameter(Name = key, WithDecryption = with_decryption)
            return response['Parameter']['Value']
    
    