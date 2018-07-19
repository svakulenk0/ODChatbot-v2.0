# ODChatbot-v2.0

## Requirements

Python 3

* Flask
* elasticsearch
* keras
* tensorflow / tensorflow-gpu

## Seq2Seq models

* basic: character-level LSTM Encoder-Decoder [Keras](https://github.com/keras-team/keras/blob/master/examples/lstm_seq2seq.py)



### Train 

python3 seq2seq_char.py -e 500 -l 1500 -b 64

Parameters:

-e  number of epochs
-l  number of training samples
-b  batch size


python3 seq2seq_char.py -e 1000 -l 50 -b 1

### Results

Number of samples: 41
Train on 32 Validate on 9 for 1000 epochs

Can not handle search queries, e.g.

data about education
search graz

is there something about economics
search politics

### Tips

* To memorize longer or more responses increase training time, i.e. train for more epochs, e.g. in 200-500 epochs the model can memorize 'Hi! I am here to help you explore the available open data sets! Are you interested in something specifically or just looking around?'
