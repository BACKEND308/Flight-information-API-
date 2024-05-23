from connect import connectDB



def insert_flight_information(db, flight_information_data):
    flight_information_collection = db.flight_information
    result = flight_information_collection.insert_one(flight_information_data)
    print(f"Inserted flight information with ID: {result.inserted_id}")

def main():
    db = connectDB()
   
    flight_information_data = [
        {
            "FlightNumber": "FL0001",
            "Date": "2024-05-01T15:00:00Z",
            "FlightDuration": "03:00",
            "FlightDistance": 2475,
            "FlightSource": {
                "Country": "USA",
                "City": "New York",
                "AirportName": "John F. Kennedy International Airport",
                "AirportCode": "JFK"
            },
            "FlightDestination": {
                "Country": "USA",
                "City": "Los Angeles",
                "AirportName": "Los Angeles International Airport",
                "AirportCode": "LAX"
            },
            "VehicleType": {
                "Model": "Boeing 737",
                "Capacity": 188,
                "SeatingPlan": "Standard",
                "StandardMenu": "Standard Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "TR1234",
                "SharedFlightCompany": "Turkish Airlines",
                "ConnectingFlightInfo": {
                    "FlightNumber": "LH5678",
                    "Company": "Lufthansa",
                    "DepartureTime": "2024-05-01T21:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0002",
            "Date": "2024-05-02T16:00:00Z",
            "FlightDuration": "02:45",
            "FlightDistance": 2140,
            "FlightSource": {
                "Country": "USA",
                "City": "Chicago",
                "AirportName": "O'Hare International Airport",
                "AirportCode": "ORD"
            },
            "FlightDestination": {
                "Country": "USA",
                "City": "San Francisco",
                "AirportName": "San Francisco International Airport",
                "AirportCode": "SFO"
            },
            "VehicleType": {
                "Model": "Airbus A320",
                "Capacity": 150,
                "SeatingPlan": "Economy",
                "StandardMenu": "Vegetarian Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "AA5678",
                "SharedFlightCompany": "American Airlines",
                "ConnectingFlightInfo": {
                    "FlightNumber": "BA1234",
                    "Company": "British Airways",
                    "DepartureTime": "2024-05-02T20:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0003",
            "Date": "2024-05-03T14:30:00Z",
            "FlightDuration": "04:00",
            "FlightDistance": 3000,
            "FlightSource": {
                "Country": "USA",
                "City": "Miami",
                "AirportName": "Miami International Airport",
                "AirportCode": "MIA"
            },
            "FlightDestination": {
                "Country": "Canada",
                "City": "Toronto",
                "AirportName": "Toronto Pearson International Airport",
                "AirportCode": "YYZ"
            },
            "VehicleType": {
                "Model": "Boeing 777",
                "Capacity": 300,
                "SeatingPlan": "Business",
                "StandardMenu": "Premium Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "UA6789",
                "SharedFlightCompany": "United Airlines",
                "ConnectingFlightInfo": {
                    "FlightNumber": "AC3456",
                    "Company": "Air Canada",
                    "DepartureTime": "2024-05-03T19:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0004",
            "Date": "2024-05-04T10:00:00Z",
            "FlightDuration": "05:00",
            "FlightDistance": 4000,
            "FlightSource": {
                "Country": "USA",
                "City": "Dallas",
                "AirportName": "Dallas/Fort Worth International Airport",
                "AirportCode": "DFW"
            },
            "FlightDestination": {
                "Country": "Mexico",
                "City": "Mexico City",
                "AirportName": "Benito Juárez International Airport",
                "AirportCode": "MEX"
            },
            "VehicleType": {
                "Model": "Boeing 747",
                "Capacity": 400,
                "SeatingPlan": "Economy",
                "StandardMenu": "Mexican Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "DL7890",
                "SharedFlightCompany": "Delta Airlines",
                "ConnectingFlightInfo": {
                    "FlightNumber": "AM5678",
                    "Company": "Aeromexico",
                    "DepartureTime": "2024-05-04T16:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0005",
            "Date": "2024-05-05T18:00:00Z",
            "FlightDuration": "02:30",
            "FlightDistance": 1800,
            "FlightSource": {
                "Country": "USA",
                "City": "Houston",
                "AirportName": "George Bush Intercontinental Airport",
                "AirportCode": "IAH"
            },
            "FlightDestination": {
                "Country": "USA",
                "City": "Atlanta",
                "AirportName": "Hartsfield-Jackson Atlanta International Airport",
                "AirportCode": "ATL"
            },
            "VehicleType": {
                "Model": "Airbus A330",
                "Capacity": 250,
                "SeatingPlan": "Business",
                "StandardMenu": "Southern Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "SW1234",
                "SharedFlightCompany": "Southwest Airlines",
                "ConnectingFlightInfo": {
                    "FlightNumber": "DL3456",
                    "Company": "Delta Airlines",
                    "DepartureTime": "2024-05-05T21:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0006",
            "Date": "2024-05-06T07:00:00Z",
            "FlightDuration": "01:45",
            "FlightDistance": 1200,
            "FlightSource": {
                "Country": "USA",
                "City": "Boston",
                "AirportName": "Logan International Airport",
                "AirportCode": "BOS"
            },
            "FlightDestination": {
                "Country": "Canada",
                "City": "Montreal",
                "AirportName": "Montreal-Pierre Elliott Trudeau International Airport",
                "AirportCode": "YUL"
            },
            "VehicleType": {
                "Model": "Boeing 757",
                "Capacity": 200,
                "SeatingPlan": "Economy",
                "StandardMenu": "Canadian Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "AC1234",
                "SharedFlightCompany": "Air Canada",
                "ConnectingFlightInfo": {
                    "FlightNumber": "WS5678",
                    "Company": "WestJet",
                    "DepartureTime": "2024-05-06T10:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0007",
            "Date": "2024-05-07T12:00:00Z",
            "FlightDuration": "02:15",
            "FlightDistance": 1600,
            "FlightSource": {
                "Country": "USA",
                "City": "Denver",
                "AirportName": "Denver International Airport",
                "AirportCode": "DEN"
            },
            "FlightDestination": {
                "Country": "USA",
                "City": "Seattle",
                "AirportName": "Seattle-Tacoma International Airport",
                "AirportCode": "SEA"
            },
            "VehicleType": {
                "Model": "Airbus A380",
                "Capacity": 500,
                "SeatingPlan": "First Class",
                "StandardMenu": "Seafood Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "UA1234",
                "SharedFlightCompany": "United Airlines",
                "ConnectingFlightInfo": {
                    "FlightNumber": "AS3456",
                    "Company": "Alaska Airlines",
                    "DepartureTime": "2024-05-07T16:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0008",
            "Date": "2024-05-08T19:00:00Z",
            "FlightDuration": "03:30",
            "FlightDistance": 2200,
            "FlightSource": {
                "Country": "USA",
                "City": "Philadelphia",
                "AirportName": "Philadelphia International Airport",
                "AirportCode": "PHL"
            },
            "FlightDestination": {
                "Country": "USA",
                "City": "Orlando",
                "AirportName": "Orlando International Airport",
                "AirportCode": "MCO"
            },
            "VehicleType": {
                "Model": "Boeing 737 Max",
                "Capacity": 190,
                "SeatingPlan": "Economy",
                "StandardMenu": "Orlando Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "JB1234",
                "SharedFlightCompany": "JetBlue Airways",
                "ConnectingFlightInfo": {
                    "FlightNumber": "WN5678",
                    "Company": "Southwest Airlines",
                    "DepartureTime": "2024-05-08T23:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0009",
            "Date": "2024-05-09T08:00:00Z",
            "FlightDuration": "01:30",
            "FlightDistance": 900,
            "FlightSource": {
                "Country": "USA",
                "City": "Las Vegas",
                "AirportName": "McCarran International Airport",
                "AirportCode": "LAS"
            },
            "FlightDestination": {
                "Country": "USA",
                "City": "Phoenix",
                "AirportName": "Phoenix Sky Harbor International Airport",
                "AirportCode": "PHX"
            },
            "VehicleType": {
                "Model": "Airbus A350",
                "Capacity": 280,
                "SeatingPlan": "Business",
                "StandardMenu": "Desert Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "SW3456",
                "SharedFlightCompany": "Southwest Airlines",
                "ConnectingFlightInfo": {
                    "FlightNumber": "UA6789",
                    "Company": "United Airlines",
                    "DepartureTime": "2024-05-09T11:00:00Z"
                }
            }
        },
        {
            "FlightNumber": "FL0010",
            "Date": "2024-05-10T06:00:00Z",
            "FlightDuration": "05:30",
            "FlightDistance": 3500,
            "FlightSource": {
                "Country": "USA",
                "City": "Washington, D.C.",
                "AirportName": "Washington Dulles International Airport",
                "AirportCode": "IAD"
            },
            "FlightDestination": {
                "Country": "UK",
                "City": "London",
                "AirportName": "Heathrow Airport",
                "AirportCode": "LHR"
            },
            "VehicleType": {
                "Model": "Boeing 787",
                "Capacity": 260,
                "SeatingPlan": "Premium Economy",
                "StandardMenu": "British Menu"
            },
            "SharedFlightInfo": {
                "SharedFlightNumber": "BA4321",
                "SharedFlightCompany": "British Airways",
                "ConnectingFlightInfo": {
                    "FlightNumber": "VS5678",
                    "Company": "Virgin Atlantic",
                    "DepartureTime": "2024-05-10T12:00:00Z"
                }
            }
        }
    ]

    # for data in flight_information_data:
    #     insert_flight_information(db, data)
  
if __name__ == '__main__':
    main()