const mongoose = require('mongoose');

const connectingFlightInfoSchema = new mongoose.Schema({
    FlightNumber: String,
    Company: String,
    DepartureTime: String
});

const sharedFlightInfoSchema = new mongoose.Schema({
    SharedFlightNumber: String,
    SharedFlightCompany: String,
    ConnectingFlightInfo: connectingFlightInfoSchema
});

const vehicleTypeSchema = new mongoose.Schema({
    Model: String,
    Capacity: Number,
    StandardMenu: String
});

const locationSchema = new mongoose.Schema({
    Country: String,
    City: String,
    AirportName: String,
    AirportCode: String
});

const flightSchema = new mongoose.Schema({
    FlightNumber: { type: String, required: true, unique: true },
    Date: { type: Date, required: true },
    FlightDuration: String,
    FlightDistance: Number,
    FlightSource: locationSchema,
    FlightDestination: locationSchema,
    VehicleType: vehicleTypeSchema,
    SharedFlightInfo: sharedFlightInfoSchema
});

const Flight = mongoose.model('Flight', flightSchema);
module.exports = Flight;
