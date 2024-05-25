const express = require('express');
const cors = require('cors');
require('dotenv').config();
const connectMongo = require('./db/connectMongo'); // Ensure this properly sets up and exports the MongoDB connection.
const flightRoutes = require('./routes/flight.routes'); // Adjust path if necessary

const app = express();

app.use(cors());
app.use(express.json()); // for parsing application/json
// MongoDB Connection
connectMongo();

// Use the flight routes
app.use('/api', flightRoutes); // This prefixes '/api' before your routes

// Define a simple route for testing
app.get('/', (req, res) => {
  res.send('Flight Information API is running!');
});


// Set the port and start the server
const PORT = process.env.PORT || 3002;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

