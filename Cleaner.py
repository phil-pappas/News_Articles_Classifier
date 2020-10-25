from packages_imported import *


class Cleaner:
    """Cleaning functions that were used"""

    def concatenate_dataframes():
        frames = [df1, df2, df3]
        result = pd.concat(frames)
        return result

    def drop_null_values(df):
        df.dropna(subset=['Title', 'Text'], inplace=True)
        return df

    def drop_duplicate_values(df):
        df.drop_duplicates(subset=['Text'], keep='last', inplace=True)
        return df

    def remove_new_line(df):
        df.Text.replace('\n', ' ', regex=True, inplace=True)
        return df

    def remove_multiple_spaces(df):
        df.Text.replace('\s+', ' ', regex=True, inplace=True)
        return df

    def remove_non_ascii_chars(df):
        df.Text.replace(r'[^\x00-\x7F]', ' ', regex=True, inplace=True)
        return df

    def remove_most_noisy_words(df):
        '''TO BE UPDATED WITH MORE REGEXES - NEED TO DO IN A SEPARATE NOTEBOOK'''
        # removes whatever is inside brackets. for example {* loginWidget *}
        df.Text.replace(r'(\{.*?\})', ' ', regex=True, inplace=True)

        # removes sentences that begin with the following phrases
        df.Text.replace(
            r'(By using this website.*?\.)|(Learn about careers.*?\.)|(\( Source : .*?\))|((Published By:).*?\-)', ' ', regex=True, inplace=True)
        return df

    def remove_most_noisy_words_from_file(df, file_name):
        '''Remove predefined noisy words. These words have been detected with n-grams'''
        noisy_file = open(file_name, 'r')
        all_lines = noisy_file.readlines()
        lst = []

        for line in all_lines:
            # lst.append(line.strip())
            string_to_replace = line.strip()
            df.Text.replace(string_to_replace, ' ', regex=True, inplace=True)
            df.Text.replace(r'\( source.*\)', ' ', regex=True, inplace=True)
            df.Text.replace(r'\{(.*?)}', ' ', regex=True, inplace=True)
        noisy_file.close()
        #df.Text.replace({w: " " for w in lst}, regex=True, inplace=True)
        return df
        # to do - THIS ONE GOES TO ANOTHER CLASSS?
        # source : university || source : something   | \( source.*\)
        # {* registration_firstname *}  | \{(.*?)}
        # article extract not available.
        # ads with photos only
        # thank you for registering
        # tip : use comma'
        # need an account? create one now.
        # connect tweet linkedin comment email more
        # @telefootball
        # license photo
        # october, 2015 || oct. 21, 2015 || sept. || september
        # you have successfully emailed the post.
        # photo:
        # updated:, 10:17, a.m., friday,, oct., 2,, 2015, |,
        # posted:, 10:16, a.m., friday,, oct., 2,, 2015,

    def remove_ghost_words(list_2d):
        for i in range(len(list_2d)):
            temp_inner_list = list_2d[i]
            for word in temp_inner_list:
                if(len(word) < 1):
                    temp_inner_list.remove(word)  # remove from list
        return list_2d

    def remove_single_chars(df):
        # remove chars that are single such as "s"/.
        # If you replace the apostrophe "That's" then it's left "That s

        # maybe make it also to remove 2-chars? no many meaningful words exist see here: https://www.lexico.com/explore/two-letter-words
        # if also for 2-chars use this: \s(([a-z]{1})|([a-z]{2}))\b
        df.Text.replace(
            r'((?<=\s)|(?<=[^a-z]\.))[a-z](?=\s|\.{1}[^a-z])', ' ', regex=True, inplace=True)
        return df

    def remove_double_chars(df):
        # remove two-letters words
        df.Text.replace(r'\s+([a-z]{2})\b', ' ', regex=True, inplace=True)
        return df

    def remove_links(df):
        df.Text.replace(
            r'(https?:\/\/)?(www\.)?[a-z0-9-]+\.(com|org|net|uk)(\.[a-z]{2,3})?', ' ', regex=True, inplace=True)
        return df

    def remove_dates(df):
        # removes 22/09/2018, 01.04.2011, 18-12-2000
        df.Text.replace(
            r'(0?[1-9]|[12][0-9]|3[01])[\/\-\.](0?[1-9]|1[012])[\/\-\.]\d{4}', ' ', regex=True, inplace=True)
        return df

    def remove_years(df):
        # TODO: IMPROVE THIS? MATCHES 2019. 1877, 1382 etc.
        df.Text.replace(r'[1-2][0-9]\d{2}', ' ', regex=True, inplace=True)
        return df

    def remove_months(df):
        df.Text.replace(
            r'(jan(uary)?|feb(ruary)?|mar(ch)?|apr(il)?|may|jun(e)?|jul(y)?|aug(ust)?|sept(ember)?|oct(ober)?|nov(ember)?|dec(ember)?)', ' ', regex=True, inplace=True)
        return df

    def remove_days(df):
        # TODO: IMPORVE THE FOLLOWING
        # removes also sat which can be a verb and sun
        df.Text.replace(
            r'((mon|tues|wed(nes)?|thur(s)?|fri|sat(ur)?|sun)(day)?)', ' ', regex=True, inplace=True)
        return df

    def remove_time(df):
        # removes 09:11 PM - doesn't remove 23:38 because there is no PM nor AM
        df.Text.replace(
            r'\b((1[0-2]|0?[1-9]):([0-5][0-9])\s+([ap]?.[m]{1}.))', ' ', regex=True, inplace=True)
        # removes 23:38 format
        df.Text.replace(
            r'\b([0-1]([0-9])|([2])([0-3])):([0-5][0-9])', ' ', regex=True, inplace=True)
        return df

    def remove_punctuation(df):
        # removes all punctuations but NOT: dots (.), minus (-), and percentages (5) e.g. -2.48 %
        # We might want to keep those because of the financial and world categories
        df.Text.replace(r'[^\w\d\%\.\-\s]+|[_]', ' ', regex=True, inplace=True)
        return df

    def remove_punctuation_v2(df):
        # removes all multiple dots, hyphen (..) or surrounded by spaces
        # e.g. ".... . .", " - - - ---"
        df.Text.replace(
            r'((?<=\s)|(?<=[a-z0-9]{2}))((\.)|(\.{2,})|(\-)|(\-{2,}))(?=\s)', ' ', regex=True, inplace=True)
        return df

    def remove_numbers(df):
        # to do? / check remove_years() first
        return df
