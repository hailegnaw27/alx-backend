import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (phoneNumber === '4153518780') {
    return done(new Error('Phone number 4153518780 is blacklisted'));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

