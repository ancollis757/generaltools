import boto3
from boto3.s3.transfer import TransferConfig
import pandas as pd

# Global Variables

REGION = 'eu-west-2' # London.
CREDENTIALS = r'C:\Users\nicko\Desktop\CREDENTIALS\anc_admin_accessKeys.xlsx'
ACCESS_KEY_ID_FIELD= 'Access key ID'
SECRET_ACCESS_KEY_FIELD = 'Secret access key'
BUCKET_NAME = 'amelia-photos-long-term-storage-anc'
FILE_TO_UPLOAD_FULLPATH = r"C:\Users\nicko\Desktop\TEMP-AmeliaZIPS\03_2017.zip"
FILE_NAME_KEY = r"03_2017.zip"

# Functions

def multipart_upload_boto3(s3_resource,filepath,key, config):

    s3_resource.Object(BUCKET_NAME, key).upload_file(filepath,
                            ExtraArgs={'ContentType': 'text/pdf'}, # JSON string, NEED TO CHANGE THIS
                            Config=config,
                            #Callback=ProgressPercentage(filepath_1) # See progress of upload.
                            )

# Local variables
access_pd = pd.read_excel(CREDENTIALS)
access_key_id = access_pd[ACCESS_KEY_ID_FIELD].iloc[0]
secret_access_key = access_pd[SECRET_ACCESS_KEY_FIELD].iloc[0]

# MAIN RUN

s3_resource = boto3.resource('s3') # Define resource being used.

# Set config for multipart upload.
config = TransferConfig(multipart_threshold=1024 * 25, # Minimum part size of 25MB to use multipart upload.
                        max_concurrency=10, # Maximum threads. Leave as default of 10.
                        multipart_chunksize=1024 * 100, # Size of each multi-part transfer. Used 100MB.
                        use_threads=True)

#Run the multipart upload.
multipart_upload_boto3(s3_resource, FILE_TO_UPLOAD_FULLPATH, FILE_NAME_KEY, config)
