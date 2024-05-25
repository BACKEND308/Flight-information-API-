const mongoose = require('mongoose');

const connectMongo = async () => {
  console.log('Environment Variable MONGO:', process.env.MONGO); // Add this line to debug
  try {
    await mongoose.connect(process.env.MONGO);
    console.log('MongoDB connected successfully');
  } catch (err) {
    console.error('MongoDB connection error:', err);
    process.exit(1);
  }
};

module.exports = connectMongo;
