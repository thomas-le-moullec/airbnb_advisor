# Airbnb Advisor
This is a Memo / ReadMe for an **Airbnb** data mining and predictions prototype (web-based) that is entirely run and hosted on **AWS Cloud** to help short terms renters and renting investors.

```
Prototype Website: https://thomas-lemoullec.com/index.html
```
```
API: https://api.thomas-lemoullec.com
```

## Industry Context
The travel landscape has evolved substantially since the dawn of the internet in 1991. In the travel space, Expedia and Booking.com (then bookings.nl) launched in 1996. A big year for Chinese players was 1999, with Alibaba and Ctrip both launching. Online travel agents brought new opportunities for hotels, but also disrupted the traditional relationships between hotels, travel agents, and Global Distribution Systems (GDS). Younger companies like Airbnb are now stepping forward as the next wave of disruption in the lodging industry.

We are at a stage today where it is unlikely to imagine a lodging landscape without short-term rentals. Often labeled as one of the biggest disruptors in the travel industry, Airbnb has moved into the mainstream. Short-term rentals have a long history in many countries, often unregulated and in the form of informal exchanges. Companies like HomeAway and Airbnb have paved the way for the short-term rental market to move online, and have given homeowners an easier entry into the business of hosting. Today we see that short-term rental bookings are mostly made online using an intermediary. In this aspect, the short-term rental category is miles ahead of the hotel industry.

The current growth of tourism and mobility due to many factors (Low-Cost flights, Chinese Tourism, Online Booking, Remote Jobs, International Conferences) is bringing a lot of possibilities for short term renting.

## Introduction and Concept
### Rise of Airbnb is changing the Real Estate game
More and more property investors in the housing market are investing in short-term rental properties as money-making machines in various cities around the world. 
Airbnb is offering a disruptive platform: Rent whenever you want your own place.

The Airbnb concept is targeting different types of owners:
* **The non-professional owners who wish to rent their property** or a room for a short term (E.g: When they are on vacations)
* **The professionals who are investing in short-term rental with Airbnb**, they usually have several properties to rent.

From the research I have done so far, Airbnb is growing at a rapid speed. This also brings with it complexities and opportunities given the scale of operations. Overall, the insights I gathered include:

* Big Cities Are Still the Most Booked
* Smaller Vacation Spots Are Gaining More Popularity
* Renters Look for Unconventional Accommodation
* Strict Regulations in Some Cities

### Airbnb Statistics:
 ![alt text](https://s3.ap-northeast-2.amazonaws.com/airbnb-advisor-prototype-resources/Airbnb+Statistics+for+Target+Market+Demographics+and+Growth+++iPropertyManagement.com.png)
 
    - 4 million Airbnb listings worldwide.
    - 191 Countries, 65000 Cities
    - About 500,000 stays per night
    - Airbnb’s value worldwide is $38 billion
    - 650,000 hosts on Airbnb
    - Average of 3 listings per host

More Statistics here: https://ipropertymanagement.com/airbnb-statistics/    

### Executive Summary - Solution (Prototype)

**Problem:**
 * The fast growing market is getting more and more complex and more competitive, finding the optimal price for owners is taking time and is not easy.
 * Short term renting is full of opportunities for new investors, but finding the best property isn't easy and can be unexpected.
 * More and more investors or agents are managing several properties, things are getting redundant and time consuming.
 
**Targets:**
 * The non-professional owners who wish to rent their property
 * The Professionals investing in short-term rental properties as money-making machines

**What about a solution that can help investors to find the best price for their real estate renting ?**
 * E.g : Based on the history of the market prices for this specific type of property in this specific location at this exact date, the price could be increase by 21%
 
**What about a solution that can help future owners to find the best investment based on their criterias ?**
 * Based on the renting rate history and the prices history we would be able to give the optimal investment for specific Budget, specific ROI delay, specific City or specific seasons to rent
 * E.g: With 300 000 $ Budget, I want my money back in n years and I only want to rent at this specific seasons in this country / city. The best investment is this type of appartment in this district of Paris.
 
**Prediction:**
  * The Basic prediction model will be based on 2 datasets, one describing the properties listed (106 criterias, E.g: Balcony, bathroom, location), one describing the renting calendar (Rate, prices, dates).
  * Combining this two datasets to get the price for a specific type of appartment and the number of days rented over a specific period of time (t) would give us a prediction of the potential income over the t period.
  * The predicted income for a period of time for a specific type of property would then be crossed with the investor criterias to find the optimal investment

Calendar CSV Sample:
![alt text](https://s3.ap-northeast-2.amazonaws.com/airbnb-advisor-prototype-resources/Calendar_csv_sample.png)
Listings CSV Sample:
![alt text](https://s3.ap-northeast-2.amazonaws.com/airbnb-advisor-prototype-resources/Listings_csv_sample.png)

## Vision
 * Based on investment criterias (Budget, ROI, City, Renting Period), give the best optimal investment (2 rooms, 1 bathroom, 1 balcony in this district).
 * Forecast AWS to predict optimal price for a property (Based on property type and Time Series data of the last 5 years).
 * Real Time data with Dynamic DashBoard that can be connect with Alexa: "What is the optimal price today ?"
 * Solution that can manage investor properties automatically by interacting with Airbnb API based on the price prediction model and the current market situation.

 ## Customer Experience - User Manual (Prototype)
  ### 1. Concepts
  ### 2. How to use Airbnb Solution
      1. API Documentation
      - https://api.thomas-lemoullec.com/dev/listings/{city}
      - https://api.thomas-lemoullec.com/dev/calendar/{city}
      - https://api.thomas-lemoullec.com/dev/dashboard/{city}
      2. Website
      - https://thomas-lemoullec.com/index.html

## Project Technologies and System architecture (Prototype)
Current Technological for the prototype:
 - Amazon Web Services (S3, EC2, SQS, Lamdba, CloudFront, Route53, API Gateway) (Hosted on Seoul region)
 - Python 3.* | Nodejs 8.10

**Details and Pipeline through AWS Services:**

```    
S3: CSV (Dataset) is uploaded on a S3 Standard bucket, this new upload will trigger a SQS Queue. 
``` 
``` 
SQS: Queuing system built used to push the new uploaded file details. A new message in this queue means a new dataset to process, in brief a new job needs to be done.
``` 
``` 
EC2: Server c5d.2xlarge On Spot is used as a core of the prototype, into an auto-scaling group changing from 1 to 3 machines. This machine on this specific biling gives us good computation power for a low price and a lot of flexibility: Adapated to prototype.
Server is doing a long-polling on the SQS queue (Nodejs) and get the name of the new uploaded dataset in the Stand S3 bucket. The EC2 instance will download the csv file and preprocess it with Python.<br/>
For the purpose of the prototype, the csv file cleaned is stored in a IA S3 Bucket.
The original CSV file from the S3 bucket is then removed by the EC2 instance.
The Cleaned data will then be inserted within a PostgreSQL DataBase (Create / Update Table, Insert and SQL operations to insert relevant information), this is done automatically based on the name of the file (City and date).
``` 
```
RDS: A PostgreSQL Database on a db.t2.medium 100 GB SSD Storing the Relevant information from the dataSets. Mutli AZ, Encrypted and Read Replica.
```
``` 
Lambda and API Gateway: To build the Open API. Lambda are coded in Nodejs. "Dev" is the only API stage available.
``` 
``` 
CloudFront: Used the CDN to distribute the Static Website and the Open API with more efficiency.
```
``` 
S3 thomas.le-moullec.com: Public Bucket to serve the Website displaying Data Visualisation.
``` 
```
Route53: Alias to our reserved DNS for the API and the Website. 
```

![alt text](https://s3.ap-northeast-2.amazonaws.com/airbnb-advisor-prototype-resources/Airbnb+Advisor+Architecture+Final.png)
Explore the CloudCraft Architecture
https://cloudcraft.co/view/d618ff05-7d30-473e-9c88-a8686a03452d?key=g73drwWc45GzplVWyPniPw

### Well-Architected Framework and Standards applied for Airbnb Prototype

#### Security
1. Data Protection:
- Transit: API and Website are using SSL / HTTPS
- Rest: Database and buckets are encrypted

2. Privilege management:
- Root Account protected with MFA (Multi Factor Authentification)
- Groups: Dev Account with SDK and Console Access (Strict and Organised groups will be created once developers will join the project)
- Roles: used within IAM. Specific role for the EC2 instance and Specific role for the lambda functions. Policies restricted as much as possible for the SQS, S3, EC2 and Lambda.
- Credentials: Currently only stored in environment variable and not encrypted. (AWS Key Management Service in Future)
3. Infrastructure Protection:
- RDS Inbound Limited to PostgreSQL Port from Role attributed to EC2.
- EC2 only reachable through SSH
4. Detective Controls:
- CloudWatch DashBoard to present resources metrics over time
- CloudWatch Alarm to trigger Scaling In or Scaling out of the EC2 instances
#### Reliability
1. Foundations
- Not really applicable for the prototype. Would need to deal with SQL and Lambda limits
2. Change Management
- So far the system is quite 'rigid' except the AutoScaling Group of the EC2 Instance which is scaling based on CPU.
- Would be more scalable and Cost Efficient with Lambda functions instead of EC2.
- Monitoring and Alarms will be more precise in the future
3. Failure Management
- Database is backed up frequently and replicate, durability and reliability offered by Mutli AZ.
- The Code can be more secure: Type of message in SQS and SQL Queries, QA needs to be done.
- Image of the EC2 core backed up and used to restart a new instance, Volume is saved on EC2 Termination.
#### Performance Efficiency
1. Compute
 - Appropriate Type of EC2 instance with Autoscaling depending on charge (Data Mining incoming needs large compute power)
2. Storage
 - Current Prototype does not need a proper storage. Using S3 with Fast Transfer Acceleration is useful.
 - Once the Features will be precised, needs to ensure that the storage will be appropriate over time.
3. Database
 - Monitor Database
 - Read Replica on Database
4. Space-time trade-off
 - CloudFront CDN for Caching and Edge performance (Important for Website and Open API)
#### Cost Optimization
1. Matched supply and demand / Cost-effective resources
 - On Spot with AutoScaling is a good ration price / power
 - Database could be reviewed based on future features
 - Lambda functions with API Gateway is the most optimize choice for an API.
2. Keep an eye on Spendings
 - No Access Control yet
 - Not Monitoring enough - Need some precise tags to track
 - Optimizing termination of resources for the prototype
3. Optimize over time
 - Think Long term on the project to choose the best services and keep on eye on new service
#### Operational Excellence
 - Prototype is not yet really robust but not really needed as no 100% Available Service needed.
 - Need to monitor and prepare to respond to unplanned operational events.

## Costs - Budget (Prototype)
Current costs are estimates for the protoype only.
**Summarize of Prototype Budget:**
![alt text](https://s3.ap-northeast-2.amazonaws.com/airbnb-advisor-prototype-resources/budget_prototype_airbnb.png)

More Details about the Prototype Budget:
https://s3.ap-northeast-2.amazonaws.com/airbnb-advisor-prototype-resources/Budget+for+Airbnb+Advisor+Architecture.xlsx

## Data (as input)
    - Airbnb DataSets: http://insideairbnb.com/get-the-data.html
    -(Coming): Airbnb API: https://www.airbnb.com/partner
    -(Coming): Real Estate Mrket API: https://www.zillow.com/ , https://www.programmableweb.com/api/zilyo-vacation-rental, AirVestor

## Delivery phases and Future Work:
* 0. Project requirements From Amazon on the **22/03/2019**
* 1. Build Simple architecture to expose an open API and a website (Sampling: 3 cities; Berlin, Paris, Hong Kong)
   - The website will be used for datavisualization.<br/>
   - The open API will be exposing the data clean from data sets coming from http://insideairbnb.com <br/>
   **Due Date:** 29/03/2019 - **Passed**
 
* 2. Deeper Business Understanding and project plan:
   - Study of Metrics and Data
   - Study of the existing
   - Definition of key features
   - Definition of Solution Architecture, Pipeline and future costs
   - Design of clear RoadMap<br/>
   **Due Date:** 15/04/2019
   
 * 3. Deliver a solution able to find the optimal price for a specific asset
   - Business Understanding
   - Data Preparation
   - Data Transformation
   - Modeling<br/>
   **Due Date:** 01/05/2019
 
 
## Human Resources and Efforts:
Phase 0 - 1
* 1 person - Thomas LE MOULLEC
* Effort: 4 days
 
 ## Frequently Asked Questions
 
 ## Authors

_Thomas, <br/>

## License
Created for the purposes of Amazon Interview. The data belongs with Inside Airbnb.

## Acknowledgments
:+1: http://insideairbnb.com// <br/>
:+1: AWS <br/>
:+1: HKUST <br/>
