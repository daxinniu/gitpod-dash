sudo gcloud builds submit --tag gcr.io/delta-jigsaw-334522/test_dash_app  --project=delta-jigsaw-334522

sudo gcloud run deploy --image gcr.io/delta-jigsaw-334522/test_dash_app --platform managed  --project=delta-jigsaw-334522 --allow-unauthenticated