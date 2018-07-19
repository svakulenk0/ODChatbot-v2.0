# ODChatbot-v2.0

## Requirements

Python 3

* torch==0.3.1
* nltk

```
pip --no-cache-dir install -r requirements.txt
```

* mkdir log

* Download NLTK stopwords

In Python console:
```
>>> import nltk
>>> nltk.download()
Downloader> d
Identifier> stopwords

nltk.download('punkt')
```

* Set simlink to this folder as an [opsdroid]() skill (in ~/.local/share/opsdroid/opsdroid-modules/skill on Linux)
```
ln -sfn ~/ODChatbot-v2.0 ODExploration
```

## Training with default parameters

```
python3 model.py -mode train -model tsdf-OD
```

## Inference

```
python3 model.py -mode iteract -model tsdf-OD
```

## Acknowledgement

Based on [Sequicity](https://github.com/WING-NUS/sequicity)

```
@inproceedings{lei2018sequicity,
  title={Sequicity: Simplifying Task-oriented Dialogue Systems with Single Sequence-to-Sequence Architectures},
  author={Lei, Wenqiang and Jin, Xisen and Ren, Zhaochun and He, Xiangnan and Kan, Min-Yen and Yin, Dawei},
  year={2018},
  organization={ACL}
}
```
