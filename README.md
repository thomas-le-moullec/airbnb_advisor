# airbnb_advisor
Airbnb big data project to help short terms renting investors.

## Introduction and Concept

## Vision
 * Based on investment criterias (Budget, ROI, City, Renting Period), give the best optimal investment (2 rooms, 1 bathroom, 1 balcony in this district).
 * Forecast AWS to predict optimal price for a property (Based on property type and Time Series data of the last 5 years).
 * Real Time data with Dynamic DashBoard that can be connect with Alexa: "What is the optimal price today ?"

## Project Technologies:
 * Amazon Web Services (S3, EC2, SQS, Lamdba, CloudFront, Route53, API Gateway)
 * Python 3.*
 * Nodejs 8.10

## Delivery phases:
  ### 1- Build Simple architecture to expose an open API and a website (Sampling: 3 cities)
    * The website will be used for datavisualization.
    * The open API will be exposing the data clean from data sets coming from http://insideairbnb.com
