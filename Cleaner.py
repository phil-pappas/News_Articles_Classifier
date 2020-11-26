from packages_imported import *


class Cleaner:
    """Cleaning functions that were used"""

    # used??or not?
    def concatenate_dataframes(df1, df2, df3):
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
        '''THE FOLLOWING REGEXES ARE EXPLAINED IN THE Find_Noisy_words NOTEBOOK'''
        df.Text.replace(r'(\{.*?\})', '', regex=True, inplace=True)
        df.Text.replace(
            r'((Most Read)|(Need a Profile\?)|(By using this website)|(By submitting your registratio)).*?a link to create a new password\.', '', regex=True, inplace=True)
        df.Text.replace(r'(By using this website.*?\.)',
                        '', regex=True, inplace=True)
        df.Text.replace(r'(Tip : Use comma.*?Learn more...)',
                        '', regex=True, inplace=True)
        df.Text.replace(r'(Published By:).*?\-', '', regex=True, inplace=True)
        df.Text.replace(
            r'(Ads with Photos only:.*?RSS Feeds .)\s*(Featured Classifieds)*', '', regex=True, inplace=True)
        df.Text.replace(r'(Terms Quotes.*?\s*\-*\s+News Network)',
                        '', regex=True, inplace=True)
        df.Text.replace(
            r'Article extract not available\. Link to *(the)* source for the full article\.*', '', regex=True, inplace=True)
        df.Text.replace(
            r'((Subscription Required An online service)|(Need an account\? Create one now)).*', '', regex=True, inplace=True)
        df.Text.replace(
            r'(Sorry, an error occurred\.)*\s(Please sign in or register to leave a comment).*', '', regex=True, inplace=True)
        df.Text.replace(
            r'((Join the conversation Sign)|(There are no comments yet\. Be the first)).*', '', regex=True, inplace=True)
        df.Text.replace(
            r'(\(AP Photo.*?\))|(\(Photo by.*?\)|(\(Photo\:.*?\)))', '', regex=True, inplace=True)
        df.Text.replace(
            r'((SUBSCRIBE FOLLOW US)|Copyright)*\s2015*\s(Cox Media Group)', '', regex=True, inplace=True)
        df.Text.replace(
            r'((Copyright 2015).*?All rights reserved.)\s+(This material may not be published, broadcast, rewritten or redistributed)*', '', regex=True, inplace=True)
        df.Text.replace(
            r'Related Sponsored Links By Cox Media Group National Content Desk', '', regex=True, inplace=True)
        df.Text.replace(r'This material may not be published.*?\.',
                        '', regex=True, inplace=True)
        df.Text.replace(r'Copyright.*?\.', '', regex=True, inplace=True)
        df.Text.replace(r'Thank you for registering! We have sent.*',
                        '', regex=True, inplace=True)
        df.Text.replace(r'(Click to play video Return to video Video settings Please Log in to update your video settings Video will begin in 5 seconds\. Don\'t play Play now More video Recommended Replay video Return to video Video settings Please Log in to update your video settings)|(Return to video Video settings Please Log in to update your video settings Video will begin in 5 seconds\. Don\'t play Play now More video Recommended)', '', regex=True, inplace=True)
        df.Text.replace(
            r'((Click to play video)|(Replay video))*\s+(Return to video Video settings Please Log in to update your video settings)', '', regex=True, inplace=True)
        df.Text.replace(
            r'(Video will begin in 5 seconds\. Don\'t play Play now More video Recommended)', '', regex=True, inplace=True)
        df.Text.replace(r'Company News - .*-', '', regex=True, inplace=True)
        df.Text.replace(r'For Updates Check.*', '', regex=True, inplace=True)
        df.Text.replace(
            r'Make Your Passion Your Career.*?job that interests you:', '', regex=True, inplace=True)
        df.Text.replace(r'\( Source : .*?\)', '', regex=True, inplace=True)
        df.Text.replace(r'Learn about careers.*?\.',
                        '', regex=True, inplace=True)
        df.Text.replace(r'CONNECT TWEET LINKEDIN COMMENT EMAIL MORE',
                        '', regex=True, inplace=True)
        df.Text.replace(r'Local Real Estate Cars For Sale',
                        '', regex=True, inplace=True)
        df.Text.replace(r'By Kyle Newport,.*', '', regex=True, inplace=True)
        df.Text.replace(r'> Top News', '', regex=True, inplace=True)
        df.Text.replace(r'> Entertainment', '', regex=True, inplace=True)
        df.Text.replace(r'^.*(?=License Photo).*?\-\-',
                        '', regex=True, inplace=True)
        df.Text.replace(
            r'\* \* A version of this article appeared.*?\.', '', regex=True, inplace=True)
        df.Text.replace(r'^.*(?=License Photo).*?\-\-',
                        '', regex=True, inplace=True)
        df.Text.replace(r'(DJ\?@.*?k\^Am|kAm.*?k\^Am)',
                        '', regex=True, inplace=True)

        return df

    def remove_ghost_words(list_2d):
        for i in list_2d.iteritems():
            for word in i[1]:
                if(len(word) < 1):
                    i[1].remove(word)  # remove from list

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
        df.Text.replace(r'[^\w\d\%\.\-\s]+|[_]', ' ',
                        regex=True, inplace=True)
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
