import sqlite3
import csv
import os
import progressbar
from pprint import pprint
from modules.lemmatization.lemmatization import lemmatization
from modules.get_ngram_info.get_ngram_info import get_ngram_info
from datetime import datetime

changes_date = str(datetime.now())

u = sqlite3.connect('unigrams.db')
u_cursor = u.cursor()

b = sqlite3.connect('bigrams.db')
b_cursor = b.cursor()

t = sqlite3.connect('trigrams.db')
t_cursor = t.cursor()


def read_data():
    with open(os.path.join('..', 'tests', 'data_to_add.csv'), 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list()
        for row in reader:
            doc = ''.join(row).split(';')
            data.append({'text': doc[0], 'tonal': doc[1]})

        return data


def lemmatization_all_data(data):
    print('lemmatization...')
    with progressbar.ProgressBar(max_value=len(data)) as bar:
        for n in range(len(data)):
            data[n]['text'] = lemmatization(data[n]['text'])
            bar.update(n)

    return data


def split_into_bigrams(text):
    unigrams = text.split()
    return [unigrams[n] + ' ' + unigrams[n + 1] for n in range(len(text.split()) - 1)]


def split_into_trigrams(text):
    unigrams = text.split()
    return [unigrams[n] + ' ' + unigrams[n + 1] + ' ' + unigrams[n + 2] for n in range(len(text.split()) - 2)]


def split_into_ngrams(data):
    print('\nsplitting documents into N-grams...')
    unigrams = list()
    bigrams = list()
    trigrams = list()

    with progressbar.ProgressBar(max_value=len(data)) as bar:
        for n, doc in enumerate(data):
            for unigram in doc['text'].split():
                if unigram not in unigrams:
                    unigrams.append(unigram)

            for bigram in split_into_bigrams(doc['text']):
                if bigram not in bigrams:
                    bigrams.append(bigram)

            for trigram in split_into_trigrams(doc['text']):
                if trigram not in trigrams:
                    trigrams.append(trigram)
            bar.update(n)

    return unigrams, bigrams, trigrams


def check_ngram(ngram):
    data = get_ngram_info(ngram)
    if data and data[0]:
        return True
    else:
        return False


def split_ngrams_by_status(unigrams, bigrams, trigrams):
    print('\nsplitting N-grams by database status...')
    new_unigrams = {'true': list(), 'false': list()}
    new_bigrams = {'true': list(), 'false': list()}
    new_trigrams = {'true': list(), 'false': list()}

    with progressbar.ProgressBar(max_value=len(unigrams) + len(bigrams) + len(trigrams)) as bar:
        k = 0
        for unigram in unigrams:
            if check_ngram(unigram):
                new_unigrams['true'].append(unigram)
            else:
                new_unigrams['false'].append(unigram)
            k += 1
            bar.update(k)

        for bigram in bigrams:
            if check_ngram(bigram):
                new_bigrams['true'].append(bigram)
            else:
                new_bigrams['false'].append(bigram)
            k += 1
            bar.update(k)

        for trigram in trigrams:
            if check_ngram(trigram):
                new_trigrams['true'].append(trigram)
            else:
                new_trigrams['false'].append(trigram)
            k += 1
            bar.update(k)

    return new_unigrams, new_bigrams, new_trigrams


def update_value(ngram, pos_count, neg_count):
    data = get_ngram_info(ngram)
    pos_count += data[1]
    neg_count += data[2]

    if ngram.count(' ') == 0:
        u_cursor.execute("""UPDATE 'Data' 
                            SET 'Pos_count' = %d
                            SET 'Neg_count' = %d
                            SET 'Chenges_Date' = '%s'
                            WHERE 'Ngram' = '%s'""" % (pos_count, neg_count, changes_date, ngram))
        u.commit()

    elif ngram.count(' ') == 1:
        b_cursor.execute("""UPDATE 'Data' 
                            SET 'Pos_count' = %d
                            SET 'Neg_count' = %d
                            SET 'Chenges_Date' = '%s'
                            WHERE 'Ngram' = '%s'""" % (pos_count, neg_count, changes_date, ngram))
        b.commit()

    elif ngram.count(' ') == 2:
        t_cursor.execute("""UPDATE 'Data' 
                            SET 'Pos_count' = %d
                            SET 'Neg_count' = %d
                            SET 'Chenges_Date' = '%s'
                            WHERE 'Ngram' = '%s'""" % (pos_count, neg_count, changes_date, ngram))
        t.commit()


def add_value(ngram, pos_count, neg_count):
    if ngram.count(' ') == 0:
        u_cursor.execute("""INSERT INTO 'Data' 
                            VALUES ('%s', %d, %d, %d, '%s')""" % (ngram, pos_count, neg_count, 1, changes_date))
        u.commit()

    elif ngram.count(' ') == 1:
        b_cursor.execute("""INSERT INTO 'Data' 
                            VALUES ('%s', %d, %d, %d, '%s')""" % (ngram, pos_count, neg_count, 1, changes_date))
        b.commit()

    elif ngram.count(' ') == 2:
        t_cursor.execute("""INSERT INTO 'Data' 
                            VALUES ('%s', %d, %d, %d, '%s')""" % (ngram, pos_count, neg_count, 1, changes_date))
        t.commit()


def count_occurrences(ngram, data):
    pos_count = 1
    neg_count = 1

    for doc in data:
        if ngram in doc['text']:
            if doc['tonal'] == 'positive':
                pos_count += 1
            else:
                neg_count += 1

    return pos_count, neg_count


def add_ngrams_to_db(unigrams, bigrams, trigrams, data):
    # adding true values
    for unigram in unigrams['true']:
        update_value(unigram, *count_occurrences(unigram, data))


data = lemmatization_all_data(read_data())
unigrams, bigrams, trigrams = split_ngrams_by_status(*split_into_ngrams(data))
