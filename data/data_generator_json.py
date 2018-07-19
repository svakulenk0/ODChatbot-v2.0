'''
svakulenko
3 Jul 2018

Generate datasets
im looking for something related to * or *
have you got something on * or *
i am interested in * and *
'''
import random

# template for the dialogue json structure
TEMPLATE_DIAL = '''
{
    "dial": [
      {
        "turn": 0,
        "usr": {
          "transcript": "%s",
          "slu": [
            {
              "act": "inform",
              "slots": [
                [
                  "keyword",
                   "%s"
                ]
              ]
            }
          ]
        },
        "sys": {
          "sent": "%s"
        }
      }
    ]
},
'''

TAMPLATE_DB = '''
{
    "dataset_name": "sample",
    "keyword": "%s",
    "dataset_link": "sample"
},
'''

def generate_db():
    all_terms = []
    with open('search_terms.txt') as f:
        terms = f.readlines()
        for term in terms:
            term = term.strip()
            print TAMPLATE_DB % term
            all_terms.append('"%s"' % term)
    print ", ".join(all_terms)


def generate_dialogues():
    # load patterns
    with open('search_patterns.txt') as f:
        patterns = f.readlines()

    random.shuffle(patterns)

    with open('generated_train.txt', 'wb') as f_train, open('generated_test.txt', 'wb') as f_test:
        for pattern in patterns:
            # load search terms
            with open('search_terms.txt') as f:
                terms = f.readlines()
                # shuffle terms
                random.shuffle(terms)
            # generate samples
            samples = []
            while terms:
                sample = ''
                for c in pattern.strip():
                    if c == '*':
                        # draw a random search term
                        term = terms.pop().strip()
                        sample += term
                    else:
                        sample += c
                # sample = sample + '\tsearch ' + term
                sample = TEMPLATE_DIAL % (sample, term, 'sample')
                if sample:
                    print sample
                    samples.append(sample)

            train_samples = samples[:30]
            f_train.writelines('\n'.join(train_samples) + '\n')
            test_samples = samples[31:]
            f_test.writelines('\n'.join(test_samples) + '\n')


if __name__ == '__main__':
    # generate_db()
    generate_dialogues()
