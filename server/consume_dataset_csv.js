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
    var city = csvName.substring(9, csvName.length - 15);
    var superCsv = csvName.substring(0, csvName.length - 15) + ".csv";
    var processString = csvName.substring(0, csvName.length - 10);
    processString = processString.substr(processString.length - 7);
    var preprocessString = ' ; python preprocess_' + (csvName[0] === 'c' ? 'calendar.py ' : 'listings.py ');
    
var execStr = "aws s3 cp s3://tslemoullec-clean-datasets/" + superCsv + ".gz . ; gunzip "
    + superCsv + ".gz ; aws s3 cp s3://tslemoullec-airbnb-listings/Paris/"
+ csvName + " . ; gunzip " + csvName + preprocessString + csvName.substring(0, csvName.length - 3)
+ " ; gzip < "+ superCsv + " > " + superCsv + ".gz; aws s3 mv " + superCsv + ".gz s3://tslemoullec-clean-datasets --storage-class STANDARD_IA"
    
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
