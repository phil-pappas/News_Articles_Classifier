from packages_imported import *


class EDA:
    # def __init__(self):

    def process_time(time_taken):
        message = "Process completed.\nTime taken: "
        if (time_taken >= 3600):
            print(message + "{hours}h {minutes}mins {seconds}secs".format(
                hours=(time_taken//3600),
                minutes=((time_taken % 3600)//60),
                seconds=((time_taken % 3600) % 60)))
        elif (time_taken >= 60):
            print(message + "{minutes}mins {seconds}secs".format(
                minutes=(time_taken//60),
                seconds=(time_taken % 60)))
        else:
            print(message + "{seconds} seconds".format(seconds=time_taken))

    def display_outliers_boxplot(df, column_name):
        sns.boxplot(x=df[column_name])

    def display_outliers_skewness_value(df, column_name):
        '''Several machine learning algorithms make the assumption that the data 
        follow a normal (or Gaussian) distribution. This is easy to check with 
        the skewness value, which explains the extent to which the data is normally distributed. 
        Ideally, the skewness value should be between -1 and +1, and any major deviation from 
        this range indicates the presence of extreme values.
        Source: https://www.pluralsight.com/guides/cleaning-up-data-from-outliers'''
        print(df[column_name].skew())

    def remove_outliers_by_iqr_score(df):
        '''Calculating the IQR Score in order to remove the outliers.'''
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        # print(IQR)
        df_out = df[~((df < (Q1 - 1.5 * IQR)) |
                      (df > (Q3 + 1.5 * IQR))).any(axis=1)]
        # print(df_out.shape)
        return df_out

    def remove_outliers_by_range(df, column_name, greater_than_value, less_than_value):
        df = df[df[column_name] > greater_than_value]
        df = df[df[column_name] < less_than_value]
        return df

    def display_distribution(categories_count, plot_title, x_label, y_label):
        '''[Input] categories_count: type of int64 Series (1-dimension)'''
        plt.figure(figsize=(15, 10))
        plt.title(plot_title, fontsize=22)
        plt.xlabel(x_label, fontsize=18)
        plt.ylabel(y_label, fontsize=18)
        plt.xticks(rotation=90)
        sns.set(style="darkgrid")
        sns.barplot(categories_count.index, categories_count.values)
        plt.show()
        # plt.savefig("Category-articles.png")

    def display_buzzwords(text_values):
        '''[Input] text_values: Array of text elements separated by comma'''
        t1 = time.time()

        long_string = ','.join(text_values)
        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color="white",
                              max_words=5000, contour_width=3, contour_color='steelblue')
        wordcloud = wordcloud.generate(long_string)
        # wordcloud.to_image()

        plt.figure(figsize=(20, 10))
        plt.imshow(wordcloud)

        t2 = time.time()
        print("Process completed.\nTime taken:")
        print("{:.2f}".format(round(t2-t1, 2))+" seconds.")

    def display_outliers(df):
        # to do
        # display a boxplot?
        return df

    def find_ngrams(input_list, n):
        return list(zip(*(input_list[i:] for i in range(n))))

    def find_most_common_n_grams(articles_split_by_word, n):
        occurrences = {}
        for item in articles_split_by_word:
            ngrams_per_article = collections.Counter(EDA.find_ngrams(item, n))
            items_list = list(ngrams_per_article.most_common(n))
            words_list = []
            # print(items_list)
            if (items_list):
                for item in items_list[0][0]:
                    words_list.append(item)

                words = ' '.join(map(str, words_list))
                #occurrences_within_article = list_of_dict_values[0][1]
                #print("words: "+words)
                if words in occurrences:
                    occurrences[words] += 1
                else:
                    occurrences[words] = 1
        return occurrences

    def count_words_per_records_opt_1(df):
        return df['Text'].str.split().str.len()

    def count_words_per_records_opt_2(df):
        return df.Text.apply(lambda x: len(str(x).split()))

    def difference_percentage(num_A, num_B):
        "Differences between two numbers as a percentage with two digits e.g. 45.38%"
        if (num_A >= num_B):
            temp = ((num_B-num_A)/num_A) * 100
            temp = round(temp, 2)  # keep only two digits after decimal
        else:
            temp = ((num_A-num_B)/num_B) * 100
            temp = round(temp, 2)  # keep only two digits after decimal
        return temp

    def count_records_per_label(df, new_column_name):
        "count the number of records for each category and store them in a new column"
        return df.groupby(['Category'], sort=False).size().reset_index(name=new_column_name)
