import boto3
import os

# Load your environment variables (you might need to load from env.py)
if os.path.exists('env.py'):
    import env

# Test the connection
try:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name='eu-north-1'
    )
    
    # Try to list your bucket
    response = s3.list_objects_v2(Bucket='fold-project-four')
    print("✅ AWS connection successful!")
    print(f"Bucket contents: {response.get('Contents', [])}")
    
except Exception as e:
    print(f"❌ AWS connection failed: {e}")