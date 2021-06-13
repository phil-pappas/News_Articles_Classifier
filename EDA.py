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

    def display_accuracy_scores_per_parameter(x_values, y_values, x_label, y_label, title):
        #import plotly.express as px
        fig = px.scatter(x=x_values,
                         y=y_values,
                         labels={
                             "x": x_label,
                             "y": y_label
                         },
                         title=title)
        fig.show()

    def display_confusion_matrix(y_test, y_pred, distinct_categories, plot_title):
        from sklearn.metrics import confusion_matrix
        import numpy as np

        conf_mat = confusion_matrix(y_test, y_pred)
        fig, ax = plt.subplots(figsize=(10, 10))
        heatmap = sns.heatmap(conf_mat, annot=True, fmt='d',
                              xticklabels=np.unique(y_test),
                              yticklabels=np.unique(y_pred),
                              square=True)
        plt.ylabel('Actual', size=20)
        plt.xlabel('Predicted', size=20)
        ax.set_title(plot_title, size=20)

        # rotate text in the x axis
        heatmap.set_xticklabels(heatmap.get_xmajorticklabels(), rotation=40)
        # change the text in the x,y axis
        heatmap.set_xticklabels(heatmap.get_xmajorticklabels(), fontsize=13)
        heatmap.set_yticklabels(heatmap.get_ymajorticklabels(), fontsize=13)

        # Fixing the margin problem
        b, t = plt.ylim()  # discover the values for bottom and top
        b += 0.5  # Add 0.5 to the bottom
        t -= 0.5  # Subtract 0.5 from the top
        plt.ylim(b, t)  # update the ylim(bottom, top) values
        ####
        plt.show()

    def display_outliers_boxplot(df, column_name, x_name, y_name, title_name):
        # sns.boxplot(x=df[column_name]) seaborn boxplot
        px.box(df, x=x_name, y=y_name, title=title_name,
               hover_data=[column_name]).show()

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

    def display_distribution_matplot(categories_count, plot_title, x_label, y_label):
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

    def display_distribution_donut(df, values_column, labels_column, chart_title):
        from plotly.offline import iplot
        '''        
        ------------------------- [Input Parameters] -------------------------
        --- df: Dataframe with number of records to visualise
        --- values_column: The name of the column that contains the number of records
        --- labels_column: The name of the column that contains the names of each class
        ----------------------------------------------------------------------
        '''
        fig = {
            "data": [
                {
                    "values": df[values_column],
                    "labels": df[labels_column],
                    "textposition": "outside",
                    "domain": {"x": [0, .77]},
                    "name": "Criticality",
                    "marker": {'colors': px.colors.cyclical.Twilight
                               },
                    "textinfo": "percent+label",
                    "textfont": {'color': '#000000', 'size': 15},
                    "hole": .5,
                    "type": "pie",
                    "automargin": False
                }],
            "layout": {
                "title": chart_title,
                "annotations": [
                    {
                        "font": {
                            "size": 25,
                            "color": '#000000'
                        },
                        "showarrow": False,
                        "text": "News",
                        "x": 0.31,
                        "y": 0.5
                    }
                ]
            }
        }

        iplot(fig)

    def display_stats_distribution_pre_post_processing(df, chart_title):
        import plotly.graph_objs as go
        from plotly.offline import iplot

        data = [go.Bar(x=df['Category'],
                       y=df['Count_Pre_Processing'],
                       name="Pre-Processing",
                       text=df['Count_Pre_Processing'],
                       textposition='outside',
                       hovertext="Reduced by "+df['Records_Loss'],
                       marker_color='rgb(128, 0, 0)'),

                go.Bar(x=df['Category'],
                       y=df['Count_Post_Processing'],
                       name='Post-Processing',
                       text=df['Count_Post_Processing'],
                       textposition='outside',
                       hovertext="Reduced by "+df['Records_Loss'],
                       marker_color='rgb(0, 64, 128)')]

        layout = go.Layout(
            barmode='group',
            title=chart_title,
            xaxis_title="Categories",
            yaxis_title="# of Records",
            autosize=False,
            width=900,
            height=500,
            legend=dict(
                x=0,
                y=0.99,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ))

        fig = go.Figure(data=data, layout=layout)
        iplot(fig)

    def display_buzzwords(text_values, category, type, save_or_not):
        '''[Input] '''
        '''
        ------------------------- [Input Parameters] -------------------------
        --- text_values: Array of text elements separated by comma
        --- category (string): Name of the category in order to be used for saving 
        --- type (string) : Display buzzwords per class or as one buzzwords cloud
        --- save_or_not (boolean) : When 'True' it saves the images on the corresponding folder
        ----------------------------------------------------------------------
        This function calculates the loss percentages
        '''

        long_string = ','.join(text_values)
        # Create a WordCloud object
        wordcloud = WordCloud(width=800, height=400, background_color="white",
                              max_words=5000, contour_width=3, contour_color='steelblue')
        wordcloud = wordcloud.generate(long_string)
        # wordcloud.to_image()
        plt.figure(figsize=(20, 10))

        if(save_or_not):
            if(type == 'per_class'):
                wordcloud.to_file(
                    'visuals/buzzwords_class_' + category + '.png')
                print("The images have been saved at visuals folder.")
            elif(type == 'all_classes'):
                wordcloud.to_file('visuals/buzzwords_all_classes.png')
                plt.imshow(wordcloud)

    def find_ngrams(input_list, n):
        return list(zip(*(input_list[i:] for i in range(n))))

    def find_most_common_n_grams(articles_split_by_word, n):
        occurrences = {}
        for item in articles_split_by_word:

            ngrams_per_article = collections.Counter(
                EDA.find_ngrams(item, n))
            items_list = list(ngrams_per_article.most_common(n))
            words_list = []
            # print(items_list)
            if (items_list):
                for word in items_list[0][0]:
                    words_list.append(word)

                if(words_list):
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

    def calculate_loss_percentages(df_process_stats, len_current_df, initial_size):
        '''
        ------------------------- [Input Parameters] -------------------------
        --- df_process_stats: Dataframe consisted of the stats
        --- len_current_df (integer) : Lenght of the (current) df to be compared
        --- initial_size (integer)   : Lenght of the initial dataframe
        ----------------------------------------------------------------------
        This function calculates the loss percentages between the initial dataset of news compared to the current dataframe that will be given. All the calculations are stored in the df_process_stats dataframe and it displays the relative messages to the user.
        '''
        lossPercentage = []
        for index, row in df_process_stats.iterrows():
            temp = EDA.difference_percentage(
                row['Count_Pre_Processing'], row['Count_Post_Processing'])
            lossPercentage.append(str(temp)+"%")

        df_process_stats['Records_Loss'] = lossPercentage

        total_loss = round(
            (((len_current_df-initial_size)/initial_size)*100), 2)
        print("Total records pre-processing: " +
              str(df_process_stats['Count_Pre_Processing'].sum()))
        print("Total subtracted records: " +
              str(df_process_stats['Count_Post_Processing'].sum()-df_process_stats['Count_Pre_Processing'].sum()))
        print("Total records post-processing: " +
              str(df_process_stats['Count_Post_Processing'].sum()))

        print("Total loss: " + str(total_loss) + "% of the initial records")
        return df_process_stats

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

    def balance_dataset_distribution(df, min_quantile, max_quantile):
        '''
        https://www.kaggle.com/rafjaa/resampling-strategies-for-imbalanced-datasets
        https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/
        ------------------------- [Input Parameters] -------------------------
        --- df: Dataframe to balance
        --- min_quantile: A float number the minimum quantile value to extract
        --- max_quantile: A float number the maximum quantile value to extract
        ----------------------------------------------------------------------
        1) First we find the class with the fewest records and we keep the name and the number of records of it. 
        2) Secondly, for each class we retrieve all the records that are between the min and max values of quantiles that were given. 
        3) Lastly, we check if the retrieved number of records are less than the minority_class_number. If yes, then we take the 100% of the retrieved. If it is not, then we take the percentage of the class records that equals to the minority class (frac_percentage)
        In the end, we concatenate all the dataframes and we return the final dataframe.
        '''
        '''----- Find the minority class -----'''
        df_num_records = EDA.count_records_per_label(df, "num_records")
        df_num_records.sort_values(
            by='num_records', ascending=True, inplace=True)  # sort based on the number of records
        df_num_records.reset_index(
            drop=True, inplace=True)  # reset the indexes
        # get the 1st record since it's sorted in ascending order
        minority_class_name = df_num_records['Category'][0]
        minority_class_number = df_num_records['num_records'][0]

        '''----- Put all the records of the minority class in the final dataframe -----'''
        frames = []
        df_temp = df.loc[(df['Category'] == minority_class_name)]
        frames.append(df_temp)

        min_words = int(df.Text_TotalWords.quantile(min_quantile))
        max_words = int(df.Text_TotalWords.quantile(max_quantile))

        for class_name in df['Category'].unique():
            if (class_name != minority_class_name):  # escape the minority class

                # Retrieve all the records of a given class that are between the min and max of the quantiles
                df_temp = df.loc[(df['Text_TotalWords'] >= min_words) & (
                    df['Text_TotalWords'] <= max_words) & (df['Category'] == class_name)]
                if (len(df_temp) <= minority_class_number):
                    # If the class records are less that the minority class, then get the 100% of the records (frac=1)
                    df_temp = df_temp.sample(frac=1)
                else:
                    # find the percentage of a given class that represents the records of the minority class
                    frac_percentage = (
                        minority_class_number / len(df_temp))  # e.g. 0.75
                    df_temp = df_temp.sample(frac=frac_percentage)

                frames.append(df_temp)

        df_all_results = pd.concat(frames)
        frames = []
        del df_temp, df, df_num_records
        df_all_results.reset_index(drop=True, inplace=True)
        return(df_all_results)

    def print_most_common_words(articles_split_by_word, color, number):
        # credits to: https://www.kaggle.com/tanulsingh077/twitter-sentiment-extaction-analysis-eda-and-model/notebook
        top = Counter(
            [item for sublist in articles_split_by_word for item in sublist])
        temp = pd.DataFrame(top.most_common(number))
        temp.columns = ['Frequest_Words', '#Count']
        return temp.style.background_gradient(cmap=color)

    def models_barchart(df, chart_title):

        data = [go.Bar(x=df['Accuracy'],
                       y=df['Algorithm'],
                       name="Scores",
                       text=df['Accuracy'],
                       textposition='outside',
                       orientation='h',
                       texttemplate="<b>%{x:.2f}%</b>",
                       marker=dict(color=df['Accuracy'],
                                    colorscale='curl'))]

        layout = go.Layout(
            barmode='relative',
            title={
                'text': chart_title,
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            xaxis_title="% Accuracy",
            yaxis_title="Algorithm",
            xaxis=dict(range=[0, 85]),
            autosize=False,
            width=900,
            height=500,
            font=dict(size=14)
        )

        fig = go.Figure(data=data, layout=layout)
        iplot(fig)
