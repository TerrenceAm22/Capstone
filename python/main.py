import boto3
import botocore
from botocore.exceptions import ClientError
import io
import pandas as pd
import numpy as np



s3 = boto3.resource('s3')
s3_client = boto3.client('s3', region_name='us-east-1', aws_access_key_id="AKIA4RUK35ODZ42KXHZE",
                               aws_secret_access_key="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")




# class s3:

    # def __init__(self, bucket, filename):
    #     self.bucket = bucket
    #     self.filename = filename
    

    # def upload_my_file(self, bucket, folder, file_as_binary, file_name):
    #     file_as_binary = io.BytesIO(file_as_binary)
    #     key = folder+"/"+file_name
    #     try:
    #         s3_client.upload_fileobj(file_as_binary, bucket, key)
    #     except ClientError as e:
    #         print(e)
    #         return False
    #     return True
    
    # def from_s3(bucket, object_name, file_name):
    #     """ scrip that downloads
    #     csv or any object from s3 bucket
    #     """

    #     s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

    #     s3 = boto3.resource('s3')
    #     try:
    #         s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_local_image.jpg')
        
    #     except botocore.exceptions.ClientError as e:
    #         if e.response['Error']['Code'] == "404":
    #             print("The object does not exist.")
    #     else:
    #         raise
    #     return



def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


s3 = boto3.client('s3')
with open("/Users/selah/Documents/Terrence/python/crunchyroll.csv", "rb") as f:
    s3.upload_fileobj(f, "boto3tut", "Crunchyroll")
















































