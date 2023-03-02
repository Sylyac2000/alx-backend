import express from 'express';
import kue from 'kue';
import redis from 'redis';
import { promisify } from 'util';

let reservationEnabled = true;
const app = express();
const queue = kue.createQueue();
const redisClient = redis.createClient();
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);
const reserveSeat = async (number) => {
  await setAsync('available_seats', number);
};
const getCurrentAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
};
const updateAvailableSeats = async (number) => {
  await reserveSeat(number);
  const availableSeats = await getCurrentAvailableSeats();
  if (availableSeats === 0) {
    reservationEnabled = false;
  }
};

reserveSeat(50);

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  const job = queue.create('reserve_seat', {}).save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats > 0) {
      await updateAvailableSeats(availableSeats - 1);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});
