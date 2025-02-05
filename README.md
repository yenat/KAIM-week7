# Telegram Data Scraping and Image Collection

## Overview
This project aims to scrape data and collect images from public Telegram channels relevant to Ethiopian medical businesses. The collected data and images can be used for various purposes, including object detection and analysis.

## Prerequisites
- Python 3.6+
- [Telegram API credentials](https://my.telegram.org) (API ID and API Hash)
- Libraries: Telethon

## Installation
**Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

### Usage
Scrape data from a Telegram channel.

Run object detection using YOLO.

Store detection data in a database.

Run the FastAPI application.

### API Endpoints
Create Detection: POST /detections/

Get All Detections: GET /detections/

Get Detection by ID: GET /detections/{detection_id}

### Monitoring and Logging
Configure logging to track the process and capture errors.