from packages_imported import *


class NLP:
    """NLP functions that were used"""

    def tokenization(df):
        # return df['Text'].map(lambda x: x.split(" "))
        return df['Text'].map(lambda x: x.split(" "))

    def rejoin_words(row):
        my_list = row
        joined_words = (" ".join(my_list))
        return joined_words

    def lemmatize(articles_split_by_word):
        articles_split_by_word = articles_split_by_word.apply(
            lambda words: [WordNetLemmatizer().lemmatize(w) for w in words])
        return articles_split_by_word

    # FIX THIS FUNCTION
    def stemming(articles_split_by_word):
        articles_split_by_word = articles_split_by_word.apply(
            lambda words: [PorterStemmer().stem(w) for w in words])
        return articles_split_by_word

    def remove_stop_words(row):
        english_Stop_Words = stopwords.words('english')
        my_list = row
        meaningful_words = [w for w in my_list if not w in english_Stop_Words]
        return (meaningful_words)

    def remove_splitted_words(row):
        # remove(or split) RainyDay, PlayingInTheCold
        # regex: [A-Z][a-z]*[A-Z][a-z]*
        # TODO: ?
        return

    def remove_rare_words(df):
        # see here https://www.analyticsvidhya.com/blog/2018/02/the-different-methods-deal-text-data-predictive-python/
        # TODO: ?
        return df

    def to_lower_case(df, column_name):
        return df[column_name].str.lower()
