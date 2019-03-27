# Airbnb Advisor
Airbnb big data project to help short terms renting investors.

Website: https://thomas-lemoullec.com/index.html

API: https://api.thomas-lemoullec.com

## Introduction and Market History
The travel landscape has evolved substantially since the dawn of the internet in 1991. In the travel space, Expedia and Booking.com (then bookings.nl) launched in 1996. A big year for Chinese players was 1999, with Alibaba and Ctrip both launching. Online travel agents brought new opportunities for hotels, but also disrupted the traditional relationships between hotels, travel agents, and Global Distribution Systems (GDS). Younger companies like Airbnb are now stepping forward as the next wave of disruption in the lodging industry.

We are at a stage today where it is unlikely to imagine a lodging landscape without short-term rentals. Often labeled as one of the biggest disruptors in the travel industry, Airbnb has moved into the mainstream. Short-term rentals have a long history in many countries, often unregulated and in the form of informal exchanges. Companies like HomeAway and Airbnb have paved the way for the short-term rental market to move online, and have given homeowners an easier entry into the business of hosting. Today we see that short-term rental bookings are mostly made online using an intermediary. In this aspect, the short-term rental category is miles ahead of the hotel industry.

The current growth of tourism and mobility due to many factors (Low-Cost flights, Chinese Tourism, Online Booking, Remote Jobs, International Conferences) is bringing a lot of possibilities for short term renting.

## Today: Rise of Airbnb is changing the Real Estate game

It’s a well-known story by now: Airbnb’s rise has been astronomical. 4 million Airbnb listings worldwide: 191 countries, 65,000 cities. Airbnb is worth at least $38 billion.
Airbnb is Offering a disruptive flexibility: Rent whenever you want your own place.
More and more property investors in the housing market are investing in short-term rental properties as money-making machines.

This concept is targeting different types of owners:
* The non-professional owners who wish to rent their property or a room for a short term (E.g: When they are in vacations)
* The professionals who are investing in short-term rental with Airbnb, they usually have several properties to rent.

Airbnb is growing fast as well as the complexity and opportunities of its market:
* Big Cities Are Still the Most Booked
* Smaller Vacation Spots Are Gaining More Popularity
* Renters Look for Unconventional Accommodation
* Strict Regulations in Some Cities

## Solution: Airbnb Advisor
### Executive Summary -
#### 1. Expected Results - Features and Benefits:
What about a solution that can help investors to find the best price for their real estate renting ?
 * E.g : Based on the history of the market prices for this specific type of property in this specific location at this exact date, the price could be increase by 21%
 
What about a solution that can help futur owners to find the best investment based on their criterias ?
 * Based on the renting rate history and the prices history we would be able to give the optimal investment for specific Budget, specific ROI delay, specific City or specific seasons to rent
 * E.g: With 300 000 $ Budget, I want my money back in n years and I only want to rent at this specific seasons in this country / city. The best investment is this type of appartment in this district of Paris.
 
 **Prediction -**
  * The Basic prediction model will be based on 2 datasets, one describing the properties listed (106 criterias, E.g: Balcony, bathroom, location), one describing the renting calendar (Rate, prices, dates).
  * Combining this two datasets to get the price for a specific type of appartment and the number of days rented over a specific period of time (t) would give us a prediction of the potential income over the t period.
  * The predicted income for a period of time for a specific type of property would then be crossed with the investor criterias to find the optimal investment


#### 2. Vision: The future might be like this
 * Based on investment criterias (Budget, ROI, City, Renting Period), give the best optimal investment (2 rooms, 1 bathroom, 1 balcony in this district).
 * Forecast AWS to predict optimal price for a property (Based on property type and Time Series data of the last 5 years).
 * Real Time data with Dynamic DashBoard that can be connect with Alexa: "What is the optimal price today ?"
 * Solution that can manage investor properties automatically by interacting with Airbnb API based on the price prediction model and the current market situation.

#### 3. RoadMap: Delivery phases
    1. Build Simple architecture to expose an open API and a website (Sampling: 3 cities; Berlin, Paris, Hong Kong)
      * The website will be used for datavisualization.
      * The open API will be exposing the data clean from data sets coming from http://insideairbnb.com
  
#### 4. Project Technologies:
    * Amazon Web Services (S3, EC2, SQS, Lamdba, RDS, CloudFront, Route53, API Gateway)
    * Python 3.*
    * Nodejs 8.10
    
#### 5. Architecture
    
#### 6. Costs - Budget
 
#### 7. Data sources
    * Airbnb DataSets: http://insideairbnb.com/get-the-data.html
    * (Coming): Airbnb API: https://www.airbnb.com/partner
    * (Coming): Real Estate Market API: https://www.zillow.com/ , https://www.programmableweb.com/api/zilyo-vacation-rental, AirVestor
    
 ## Frequently Asked Questions
 
 ## Customer Experience

 ## User Manual
  ### 1. Concepts
  ### 2. How to user Airbnb Solution
      1. API Documentation
      2. Website
