'''
svakulenko
3 Jul 2018

Generate datasets

'''
import random

# template for the dialogue json structure
TEMPLATE_DIAL_1 = '''
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
                              "keyword1", 
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

TEMPLATE_DIAL_2 = '''
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
                              "keyword1", 
                              "%s"
                          ]
                      ]
                  }, 
                  {
                      "act": "inform", 
                      "slots": [
                          [
                              "keyword2", 
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
    "keyword1": "%s",
    "keyword2": "%s",
    "dataset_link": "sample"
},
'''

GREETINGS = ['hallo!!!', 'hi', 'hey', "hey you", "hey robot", "anybody there"]
THANKS = ["Danke!", "vielen dank"]


def generate_db(i):
    all_terms = []
    with open('search_terms_%d.txt' % i) as f:
        terms = f.readlines()
        for term in terms:
            term = term.strip().lower().split()
            all_terms.append('"%s"' % term[0])
            if len(term) > 1:
                print TAMPLATE_DB % (term[0], term[1])
                all_terms.append('"%s"' % term[1])
            else:
                print TAMPLATE_DB % (term[0], "")
    print ", ".join(all_terms)


def generate_dialogues(i):
    # load patterns
    with open('search_patterns_de_%d.txt' % i) as f:
        patterns = f.readlines()

    random.shuffle(patterns)

    for pattern in patterns:
        # load search terms
        with open('search_terms_%d.txt' % i) as f:
            terms = f.readlines()
            # shuffle terms
            random.shuffle(terms)
        # generate samples
        while terms:
            sample = ''
            keywords = terms.pop().strip().lower()
            term = keywords.split()
            j = 0
            for c in pattern.strip():
                if c == '*':
                    # draw a random search term
                    
                    sample += term[j]
                    j += 1
                else:
                    sample += c
            # greeting = random.choice(GREETINGS)
            # thanks = random.choice(THANKS)
            if i == 1:
                sample = TEMPLATE_DIAL_1 % (sample, keywords, 'sample')
            elif i == 2:
                sample = TEMPLATE_DIAL_2 % (sample, term[0], term[1], 'sample')


            # sample = TEMPLATE_DIAL % (greeting, sample, term, 'sample', thanks)
            if sample:
                print sample


if __name__ == '__main__':
    # generate_db(1)
    # generate_db(2)
    generate_dialogues(1)
    generate_dialogues(2)
