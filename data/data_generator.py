'''
svakulenko
3 Jul 2018

Generate datasets for training and testing NL template learner
https://randomwordgenerator.com
'''
import random

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
            search_terms = []
            for c in pattern.strip():
                if c == '*':
                    # draw a random search term
                    term = terms.pop().strip()
                    search_terms.append(term)
                    sample += term
                else:
                    sample += c
            sample = sample + '\tsearch ' + ' '.join(search_terms)
            if sample:
                print sample
                samples.append(sample)

        train_samples = samples[:30]
        f_train.writelines('\n'.join(train_samples) + '\n')
        test_samples = samples[31:]
        f_test.writelines('\n'.join(test_samples) + '\n')

    # generate training data 1,000 instances
    # generate test data 300 instances
    # save data
