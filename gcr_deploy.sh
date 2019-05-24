gcloud beta run deploy \
       --image us.gcr.io/prediction-service-models-qa/tech_demo \
       --allow-unauthenticated \
       --concurrency=80 \
       --memory=256Mi \
       --timeout=30 \
       techdemo
