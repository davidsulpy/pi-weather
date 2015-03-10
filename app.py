from ISStreamer.Streamer import Streamer
import time
import os

bucketKey = os.getenv('IS_BUCKET_KEY', 'resinio_temp_mon_test')
bucketName = os.getenv('IS_BUCKET_NAME', 'resin.io temp mon')
accessKey = os.getenv('IS_ACCESS_KEY', '')

streamer = Streamer(bucket_name=bucketName, bucket_key=bucketKey, access_key=accessKey)

for x in range(0, 150):
	streamer.log('iteration', x)
	streamer.log('temperature(F)', 72)

	time.sleep(.1)

streamer.close()