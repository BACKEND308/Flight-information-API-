const mongoose = require('mongoose');

const flightSchema = new mongoose.Schema({
  FlightNumber: { type: String, required: true, unique: true },
  DepartureAirport: { type: String, required: true },
  ArrivalAirport: { type: String, required: true },
  FlightDate: { type: Date, required: true },
  DepartureTime: { type: String, required: true },
  ArrivalTime: { type: String, required: true },
  Price: { type: Number, required: true }
});

const Flight = mongoose.model('Flight', flightSchema);
module.exports = Flight;
