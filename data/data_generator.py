'''
svakulenko
3 Jul 2018

Generate datasets for training and testing NL template learner
'''
import random

# load patterns
with open('search_patterns.txt') as f:
    patterns = f.readlines()
# load search terms
with open('search_terms.txt') as f:
    terms = f.readlines()

random.shuffle(patterns)

with open('generated_train.txt', 'wb') as f_train, open('generated_test.txt', 'wb') as f_test:
    for pattern in patterns:
        # shuffle terms
        random.shuffle(terms)
        # generate samples
        samples = []
        for i in xrange(len(terms)):
            sample = ''
            search_terms = []
            for c in pattern.strip():
                if c == '*':
                    # draw a random search term
                    term = terms[i].strip()
                    search_terms.append(term)
                    sample += term
                else:
                    sample += c
            sample = sample + '\tsearch ' + ' '.join(search_terms)
            print sample
            samples.append(sample)
        assert len(samples) == len(terms)

        train_samples = samples[:40]
        f_train.writelines('\n'.join(train_samples) + '\n')
        test_samples = samples[41:51]
        f_test.writelines('\n'.join(test_samples) + '\n')

    # generate training data 1,000 instances
    # generate test data 300 instances
    # save data