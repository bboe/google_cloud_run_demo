# Google Cloud Run Tech Demo

The code in the repository was written for a tech demo presentation given at my employer, AppFolio,
on May 24, 2019.

A video of my practice run through can be found at https://youtu.be/Ht3SuSWc0Js.


## Additional Commands


The two commands that are not included in the repository are:


```sh
# Build and add two tags to the container
docker build -t tech_demo -t us.gcr.io/prediction-service-models-qa/tech_demo .
````

```sh
# Push the container to Google's Container Registry
docker push us.gcr.io/prediction-service-models-qa/tech_demo
```
