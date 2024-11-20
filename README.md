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
   `git clone <repository_url>
cd <repository_folder> `

2. Build the Docker Image:
   `docker build -t receipt-processor .`

3. Run the Docker Container:
   `docker run -p 5001:5000 receipt-processor`

4. Access the Application:

-   The service will be accessible at http://localhost:5000.
