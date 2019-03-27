require('dotenv').config();
const { Consumer } = require('sqs-consumer');
var exec = require('child_process').exec;
var queueURL = process.env.QUEUE_URL

function treatMessage(message) {
    try {
        message = JSON.parse(message);
    } catch (e) {
        return 1;
    }
    var bucketName = message.Records[0].s3.bucket.name;
    var fileName = message.Records[0].s3.object.key;
    var csvName = fileName.substring(fileName.indexOf("/") + 1);
    var processString = csvName.substring(0, csvName.length - 10);
    processString = processString.substr(processString.length - 7);
    var preprocessString = ' ; python preprocess_' + (csvName[0] === 'c' ? 'calendar.py ' : 'listings.py ');
    var processed_file = csvName.substring(0, csvName.length - 7) + "_processed.csv"
    var execStr = "aws s3 cp s3:\/\/" + bucketName + '/' + fileName + ' . ; gunzip ' + csvName +
      preprocessString + csvName.substring(0, csvName.length - 3) +
      " ; python data_extraction.py " + processString + " ; gzip " + processed_file + 
      "; aws s3 mv " + processed_file + ".gz" +
      " s3:\/\/tslemoullec-clean-datasets --storage-class STANDARD_IA" +
      "; aws s3 rm s3:\/\/tslemoullec-airbnb-listings/" + fileName;
    console.log(execStr);
    exec(execStr, function(err, stdout, stderr) {
      if (err) {
        console.log(err);
      }
      console.log(stdout);
    });
    return 0;
}

const app = Consumer.create({
  queueUrl: queueURL,
  handleMessage: async (message) => {
    treatMessage(message.Body);
  }
});

app.on('error', (err) => {
  console.error(err.message);
});

app.on('processing_error', (err) => {
  console.error(err.message);
});

app.start();
