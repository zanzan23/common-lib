from dotenv import load_dotenv
import boto3
import os


class Config(object):
    is_lambda = False
    def __init__(self, is_lambda: bool, config_file: str = ''):
        self.is_lambda = is_lambda

        if not is_lambda:
            load_dotenv(config_file)
        

    def get_property(self, key: str, with_decryption: bool = False):
    
        if not self.is_lambda:
            return os.getenv(key)
        else:
            ssm = boto3.client('ssm')    
            response = ssm.get_parameter(Name = key, WithDecryption = with_decryption)
            return response['Parameter']['Value']
    
    