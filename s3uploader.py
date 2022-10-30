import boto3
import pandas as pd

# Global Variables

REGION = 'eu-west-2' # London.
CREDENTIALS = r'C:\Users\nicko\Desktop\CREDENTIALS\anc_admin_accessKeys.xlsx'
ACCESS_KEY_ID_FIELD= 'Access key ID'
SECRET_ACCESS_KEY_FIELD = 'Secret access key'

# Local variables
access_pd = pd.read_excel(CREDENTIALS)

access_key_id = access_pd[ACCESS_KEY_ID_FIELD].iloc[0]
secret_access_key = access_pd[SECRET_ACCESS_KEY_FIELD].iloc[0]