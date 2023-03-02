#!/usr/bin/env node
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Subscribe to a channel
client.subscribe('holberton school channel');

// Listen for messages on the channel
client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    console.log(message);
    if (message === 'KILL_SERVER') {
      // Unsubscribe from the channel
      client.unsubscribe(channel);
      // Quit Redis client when finished
      client.quit();
    }
  }
});
