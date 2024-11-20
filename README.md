# Receipt Processor

## Overview

Receipt Processor is a web service for processing receipts and calculating points based on specific rules. The service is built with Python and Flask and supports in-memory data storage. It is fully Dockerized for easy deployment and testing.

## Features

-   Endpoints:
    -   POST /receipts/process: Submit a receipt for processing and receive a unique receipt ID.
    -   GET /receipts/{id}/points: Retrieve points awarded for a specific receipt.
-   Points Calculation Rules:
    -   1 point for every alphanumeric character in the retailer name.
    -   50 points if the total is a round dollar amount with no cents.
    -   25 points if the total is a multiple of 0.25.
    -   5 points for every two items on the receipt.
    -   Additional points based on item description length.
    -   6 points if the purchase date's day is odd.
    -   10 points if the purchase time is between 2:00 PM and 4:00 PM.

## Installation and Setup

#### Prerequisites

-   Docker installed on your system.

#### Running the Application with Docker

1. Clone the Repository:
   `git clone <repository_url>`
   `cd <repository_folder> `

2. Build the Docker Image:
   `docker build -t receipt-processor .`

3. Run the Docker Container:
   `docker run -p 5001:5000 receipt-processor`

4. Access the Application:

-   The service will be accessible at http://localhost:5001.

## Testing the Application

Using Postman

-   Import the API requests into Postman:
-   Create a POST request for http://localhost:5001/receipts/process.
-   Create a GET request for http://localhost:5001/receipts/{id}/points.
-   Follow the API examples to test the endpoints.

### API Examples

1. `'{
    "retailer": "M&M Corner Market",
    "purchaseDate": "2023-11-18",
    "purchaseTime": "14:30",
    "items": [
        {"shortDescription": "Bread", "price": "3.49"},
        {"shortDescription": "Milk", "price": "1.99"}
    ],
    "total": "5.48"
}'`
2. `{
    "retailer": "Walgreens",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}`
