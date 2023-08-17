class S3:
    def __init__(self, bucket, logger):
        self.s3 = boto3.client(
            service_name="s3",
            aws_access_key_id="AKDSJSDJASIDJASOD",
            aws_secret_access_key="GAFDAFSADFSADSADSADADSADASFSADGFAS",
        )
        self.bucket = bucket
        self.logger = logger or logging.getLogger("AlluxioS3")

