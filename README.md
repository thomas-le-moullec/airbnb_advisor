# airbnb_advisor
This is a readme for an **Airbnb** data mining and predictions prototype (web-based) that is entirely run and hosted on **AWS Cloud** to help short terms renters and renting investors.

```
Prototype Website: https://thomas-lemoullec.com/index.html
```
```
API: https://api.thomas-lemoullec.com
```

## Introduction and Concept
### Rise of Airbnb is changing the Real Estate game
More and more property investors in the housing market are investing in short-term rental properties as money-making machines in various cities around the world. 
Airbnb is offering a disruptive platform: Rent whenever you want your own place.

The Airbnb concept is targeting different types of owners:
* The non-professional owners who wish to rent their property or a room for a short term (E.g: When they are on vacations)
* The professionals who are investing in short-term rental with Airbnb, they usually have several properties to rent.

From the research I have done so far, Airbnb is growing at a rapid speed. This also brings with it complexities and opportunities given the scale of operations. Overall, the insights I gathered include:

* Big Cities Are Still the Most Booked
* Smaller Vacation Spots Are Gaining More Popularity
* Renters Look for Unconventional Accommodation
* Strict Regulations in Some Cities

### Solution
**What about a solution that can help investors to find the best price for their real estate renting ?**
 * E.g : Based on the history of the market prices for this specific type of property in this specific location at this exact date, the price could be increase by 21%
 
**What about a solution that can help future owners to find the best investment based on their criterias ?**
 * Based on the renting rate history and the prices history we would be able to give the optimal investment for specific Budget, specific ROI delay, specific City or specific seasons to rent
 * E.g: With 300 000 $ Budget, I want my money back in n years and I only want to rent at this specific seasons in this country / city. The best investment is this type of appartment in this district of Paris.
 
 **Prediction:**
  * The Basic prediction model will be based on 2 datasets, one describing the properties listed (106 criterias, E.g: Balcony, bathroom, location), one describing the renting calendar (Rate, prices, dates).
  * Combining this two datasets to get the price for a specific type of appartment and the number of days rented over a specific period of time (t) would give us a prediction of the potential income over the t period.
  * The predicted income for a period of time for a specific type of property would then be crossed with the investor criterias to find the optimal investment

## Vision
 * Based on investment criterias (Budget, ROI, City, Renting Period), give the best optimal investment (2 rooms, 1 bathroom, 1 balcony in this district).
 * Forecast AWS to predict optimal price for a property (Based on property type and Time Series data of the last 5 years).
 * Real Time data with Dynamic DashBoard that can be connect with Alexa: "What is the optimal price today ?"
 * Solution that can manage investor properties automatically by interacting with Airbnb API based on the price prediction model and the current market situation.

## Project Technologies and System architecture
    * Amazon Web Services (S3, EC2, SQS, Lamdba, CloudFront, Route53, API Gateway) (Hosted on Seoul region)
    * Python 3.*
    * Nodejs 8.10

```    
S3: Stores website and is also used to upload the original CSV that we receive from Airbnb
``` 
``` 
EC2: Server used for pre-processing
``` 
``` 
SQS: Queuing system built to digest the CSV, push it eventually to POSTGRES version x
``` 
``` 
Lambda: To build the API gateway. In the future, this can be exposed to other data providers.
``` 
``` 
CloudFront: 
``` 

## Data (as input)
    * Airbnb DataSets: http://insideairbnb.com/get-the-data.html
    * (Coming): Airbnb API: https://www.airbnb.com/partner
    * (Coming): Real Estate Market API: 

## Delivery phases:
   * 1 - Build Simple architecture to expose an open API and a website (Sampling: 3 cities; Berlin, Paris, Hong Kong)
    * The website will be used for datavisualization.
    * The open API will be exposing the data clean from data sets coming from http://insideairbnb.com
    
 ## Future Work
 
 ## Authors

_Thomas, <br/>


## License

Created for the purposes of Amazon Interview. The data belongs with Inside Airbnb.

## Acknowledgments

:+1: http://insideairbnb.com// <br/>
:+1: AWS <br/>
:+1: HKUST <br/>
