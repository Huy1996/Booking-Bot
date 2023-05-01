# Booking Bot

## Overview
A Python web scraper that allows users to search for hotels on booking.com and display the results in a table format on the terminal.

## Technologies Stack
* Python: the programming language used to write the scraper script
* Selenium: a web testing framework used to automate browser interactions and perform web scraping
* Git: a version control system used for managing code changes and collaborating with others
* GitHub: a web-based platform for hosting and sharing code repositories
* Command-line interface: a command-line tool used to execute commands and run the scraper script

## Features
* Location search: Users can search for hotels by locations, such as city
* Date selection: Users can select check-in and check-out dates for their stay
* Number of guests: Users can specify the number of adults, children, and room needed for their stay.
* Web scraping: The scraper users Selenium to scrape Booking.com for hotel data.
* Terminal output: The scraped data is displayed in a table format on the terminal for easy viewing
* Link to booking page: The scraped includes a link to hotel's booking page Booking.com under shorted url form, allow users to book their stay directly from the terminal.

## How to Setup and Run
1. Clone the repository to your local machine <br>
> `git clone https://github.com/Huy1996/Booking-Bot.git`
2. Navigate to the project directory
> `cd Booking-Bot'
3. Install the requirement library
> `pip install -r requirements.txt`
4. Run the program
> `python run.py`
5. Enter location, check in date, check out date, number of adults, children, and rooms when prompted
6. Wait for the scraper to finish running.
7. The result will displayed in a table format on the terminal.