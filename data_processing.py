# Python library imports
import itertools
import operator
from collections import defaultdict
import pandas as pd


# Local library imports
from charts import Charts
import graph


class DataProcessing:
    """
    This class provides different methods to analyse a dataframe object (df).
    This df is also used to initialise the class.
    """

    def __init__(self, df):
        """A dataframe object is set as the class constructor."""
        self.df = df

    # Country to continents mapping
    CONTINENTS_MAP = {
        'AF': 'AS',
        'AX': 'EU',
        'AL': 'EU',
        'DZ': 'AF',
        'AS': 'OC',
        'AD': 'EU',
        'AO': 'AF',
        'AI': 'NA',
        'AQ': 'AN',
        'AG': 'NA',
        'AR': 'SA',
        'AM': 'AS',
        'AW': 'NA',
        'AU': 'OC',
        'AT': 'EU',
        'AZ': 'AS',
        'BS': 'NA',
        'BH': 'AS',
        'BD': 'AS',
        'BB': 'NA',
        'BY': 'EU',
        'BE': 'EU',
        'BZ': 'NA',
        'BJ': 'AF',
        'BM': 'NA',
        'BT': 'AS',
        'BO': 'SA',
        'BQ': 'NA',
        'BA': 'EU',
        'BW': 'AF',
        'BV': 'AN',
        'BR': 'SA',
        'IO': 'AS',
        'VG': 'NA',
        'BN': 'AS',
        'BG': 'EU',
        'BF': 'AF',
        'BI': 'AF',
        'KH': 'AS',
        'CM': 'AF',
        'CA': 'NA',
        'CV': 'AF',
        'KY': 'NA',
        'CF': 'AF',
        'TD': 'AF',
        'CL': 'SA',
        'CN': 'AS',
        'CX': 'AS',
        'CC': 'AS',
        'CO': 'SA',
        'KM': 'AF',
        'CD': 'AF',
        'CG': 'AF',
        'CK': 'OC',
        'CR': 'NA',
        'CI': 'AF',
        'HR': 'EU',
        'CU': 'NA',
        'CW': 'NA',
        'CY': 'AS',
        'CZ': 'EU',
        'DK': 'EU',
        'DJ': 'AF',
        'DM': 'NA',
        'DO': 'NA',
        'EC': 'SA',
        'EG': 'AF',
        'SV': 'NA',
        'GQ': 'AF',
        'ER': 'AF',
        'EE': 'EU',
        'ET': 'AF',
        'FO': 'EU',
        'FK': 'SA',
        'FJ': 'OC',
        'FI': 'EU',
        'FR': 'EU',
        'GF': 'SA',
        'PF': 'OC',
        'TF': 'AN',
        'GA': 'AF',
        'GM': 'AF',
        'GE': 'AS',
        'DE': 'EU',
        'GH': 'AF',
        'GI': 'EU',
        'GR': 'EU',
        'GL': 'NA',
        'GD': 'NA',
        'GP': 'NA',
        'GU': 'OC',
        'GT': 'NA',
        'GG': 'EU',
        'GN': 'AF',
        'GW': 'AF',
        'GY': 'SA',
        'HT': 'NA',
        'HM': 'AN',
        'VA': 'EU',
        'HN': 'NA',
        'HK': 'AS',
        'HU': 'EU',
        'IS': 'EU',
        'IN': 'AS',
        'ID': 'AS',
        'IR': 'AS',
        'IQ': 'AS',
        'IE': 'EU',
        'IM': 'EU',
        'IL': 'AS',
        'IT': 'EU',
        'JM': 'NA',
        'JP': 'AS',
        'JE': 'EU',
        'JO': 'AS',
        'KZ': 'AS',
        'KE': 'AF',
        'KI': 'OC',
        'KP': 'AS',
        'KR': 'AS',
        'KW': 'AS',
        'KG': 'AS',
        'LA': 'AS',
        'LV': 'EU',
        'LB': 'AS',
        'LS': 'AF',
        'LR': 'AF',
        'LY': 'AF',
        'LI': 'EU',
        'LT': 'EU',
        'LU': 'EU',
        'MO': 'AS',
        'MK': 'EU',
        'MG': 'AF',
        'MW': 'AF',
        'MY': 'AS',
        'MV': 'AS',
        'ML': 'AF',
        'MT': 'EU',
        'MH': 'OC',
        'MQ': 'NA',
        'MR': 'AF',
        'MU': 'AF',
        'YT': 'AF',
        'MX': 'NA',
        'FM': 'OC',
        'MD': 'EU',
        'MC': 'EU',
        'MN': 'AS',
        'ME': 'EU',
        'MS': 'NA',
        'MA': 'AF',
        'MZ': 'AF',
        'MM': 'AS',
        'NA': 'AF',
        'NR': 'OC',
        'NP': 'AS',
        'NL': 'EU',
        'NC': 'OC',
        'NZ': 'OC',
        'NI': 'NA',
        'NE': 'AF',
        'NG': 'AF',
        'NU': 'OC',
        'NF': 'OC',
        'MP': 'OC',
        'NO': 'EU',
        'OM': 'AS',
        'PK': 'AS',
        'PW': 'OC',
        'PS': 'AS',
        'PA': 'NA',
        'PG': 'OC',
        'PY': 'SA',
        'PE': 'SA',
        'PH': 'AS',
        'PN': 'OC',
        'PL': 'EU',
        'PT': 'EU',
        'PR': 'NA',
        'QA': 'AS',
        'RE': 'AF',
        'RO': 'EU',
        'RU': 'EU',
        'RW': 'AF',
        'BL': 'NA',
        'SH': 'AF',
        'KN': 'NA',
        'LC': 'NA',
        'MF': 'NA',
        'PM': 'NA',
        'VC': 'NA',
        'WS': 'OC',
        'SM': 'EU',
        'ST': 'AF',
        'SA': 'AS',
        'SN': 'AF',
        'RS': 'EU',
        'SC': 'AF',
        'SL': 'AF',
        'SG': 'AS',
        'SX': 'NA',
        'SK': 'EU',
        'SI': 'EU',
        'SB': 'OC',
        'SO': 'AF',
        'ZA': 'AF',
        'GS': 'AN',
        'SS': 'AF',
        'ES': 'EU',
        'LK': 'AS',
        'SD': 'AF',
        'SR': 'SA',
        'SJ': 'EU',
        'SZ': 'AF',
        'SE': 'EU',
        'CH': 'EU',
        'SY': 'AS',
        'TW': 'AS',
        'TJ': 'AS',
        'TZ': 'AF',
        'TH': 'AS',
        'TL': 'AS',
        'TG': 'AF',
        'TK': 'OC',
        'TO': 'OC',
        'TT': 'NA',
        'TN': 'AF',
        'TR': 'AS',
        'TM': 'AS',
        'TC': 'NA',
        'TV': 'OC',
        'UG': 'AF',
        'UA': 'EU',
        'AE': 'AS',
        'GB': 'EU',
        'US': 'NA',
        'UM': 'OC',
        'VI': 'NA',
        'UY': 'SA',
        'UZ': 'AS',
        'VU': 'OC',
        'VE': 'SA',
        'VN': 'AS',
        'WF': 'OC',
        'EH': 'AF',
        'YE': 'AS',
        'ZM': 'AF',
        'ZW': 'AF'
    }

    @staticmethod
    def _format_useragent(useragent: str):
        """
        *This function is now unused*

        Formats the useragent string and returns the browser name

        This function is private and static, hence it is visible only to members of this class.
        :param useragent: A useragent string
        """
        return useragent.split("/")[0]

    @staticmethod
    def _format_time(milliseconds: int):
        """
        Formats the the readtime from milliseconds to human readable.

        This function is private and static, hence it is visible only to members of this class.

        :param milliseconds: Time in milliseconds
        :returns: An days hours minutes and seconds representation of time.
        """
        time = milliseconds / 1000
        day = time // (24 * 3600)
        time = time % (24 * 3600)
        hour = time // 3600
        time %= 3600
        minutes = time // 60
        time %= 60
        seconds = time

        return "%dd : %dh : %dm : %ds" % (day, hour, minutes, seconds)

    @staticmethod
    def _count_occurrences(data: pd.Series):
        """
        Takes in a series object and counts the number of rows for a value they
        contain.
        This function's result is used in plotting of a series as a histogram.

        This function is private and static, hence it is visible only to members of this class.
        :param data: A Pandas series object.
        :returns: A dictionary with the row name as key and it's occurrences as the value.
        """
        # Count the number of occurences of a value and save it into a column counts
        data = data.value_counts(ascending=False).reset_index(name='counts')
        # Define two columns 'value' and 'counts' in the data series.
        data.columns = ['value', 'counts']
        # Remove any zero count columns (Since we won't be plotting zero height bars)
        data = data[data.counts != 0]
        # Use zip to combine two columns and then add them into a dictionary
        result = dict(zip(data.value, data.counts))
        # Return the dictionary
        return result

    def is_not_none(self):
        """
        Checks if the dataframe is None.

        :returns: True for if dataframe is loaded, False otherwise.
        """
        if self.df is None:
            return False
        else:
            return True

    def histogram_country(self, doc_id: str):
        """
        Creates a histogram of visitors from different countries for a given document UUID

        :param doc_id: The input document
        """
        # Filter data to get rows only where the value of doc_id in the column exists into a series object.
        sorted_df = self.df[self.df["subject_doc_id"] == doc_id].loc[:, ["visitor_country"]]
        # Get the number of occurrences for a country for the series object in the form of a dictionary
        df_dictionary = self._count_occurrences(sorted_df)
        # Plot the data
        Charts(df_dictionary, "No. of visitors by country", "Countries", "Visitors").plot_histogram()

    def histogram_continent(self, doc_id: str):
        """
        Creates a histogram of visitors from different continents for a given document UUID.

        :param doc_id: The input document
        """
        # Filter data to get rows only where the value of doc_id in the column exists.
        sorted_df = self.df[self.df["subject_doc_id"] == doc_id].loc[:, ["visitor_country"]]
        # A series object that contains the continents for that country by mapping the country value
        # to the continent value
        sorted_df = sorted_df["visitor_country"].apply(lambda x: self.CONTINENTS_MAP.get(x))
        # Get the occurrences of a continents in the form of a dictionary
        df_dictionary = self._count_occurrences(sorted_df)
        # # Plot the data
        Charts(df_dictionary, "No. of visitors by continent", "Continents", "Visitors").plot_histogram()

    def histogram_browsers_a(self):
        """
        Creates a histogram of visitors from different browsers but without formatting the browser name
        """
        # Get the occurrences of a browser in the form of a dictionary
        df_dictionary = self._count_occurrences(self.df["visitor_useragent"])
        # Plot the data
        Charts(df_dictionary, "No. of visitors by browsers (Verbose)", "Browsers", "Visitors").plot_histogram()

    def histogram_browsers_b(self):
        """
        Creates a histogram of visitors from different browsers
        """
        # Filter the dataset for using only the browser column into a series.
        sorted_df = self.df["visitor_useragent"].str.split("/").str[0]
        # Get the occurrences of a browser in the form of a dictionary
        df_dictionary = self._count_occurrences(sorted_df)
        # Plot the data
        Charts(df_dictionary, "No. of visitors by browsers (Formatted)", "Browsers", "Visitors").plot_histogram()

    def visitor_readtimes(self):
        """
        Gets the reader profiles for the dataframe.

        :returns: A dictionary containing reader profiles of visitor UUIDs (keys) against their total read times (values)
        """
        # Filter the rows where only type of event_type is 'pagereadtime' (there are other events in the issuu
        # documentation as well, thats why)
        df2 = self.df[self.df["event_type"] == "pagereadtime"].loc[:, ["visitor_uuid", "event_readtime"]]
        # Sum the readtimes for all visitors, sorts them based on their read times and then saves the top 10 highest
        # readers by sorting it in descending order into a dataframe.
        df3 = df2.groupby("visitor_uuid")["event_readtime"].sum().reset_index()
        # Sort the values from the highest to the lowest and get the top 10 documents.
        df4 = df3.sort_values(by="event_readtime", ascending=False).head(10)
        # Return a pair of the reader as key and their total read time from the dataframe
        result = dict(zip(df4.visitor_uuid, df4.event_readtime.apply(lambda x: self._format_time(x))))
        return result

    def get_relevant_readers(self, doc_id: str, user_id: str):
        """
        Gets the readers for a documents

        :param doc_id: The input document ID
        :param user_id: The input user ID
        :returns: A set of readers who have read the given document.
        """
        # A dataframe containing the rows only where the given document id exists.
        sorted_df = self.df[(self.df["subject_doc_id"] == doc_id) & (self.df["event_type"] == "read")].loc[:,
                    ["visitor_uuid"]]
        # Covert dataframe to dictionary to iterate through rows faster. 'records' converts
        df_dictionary = sorted_df.to_dict('records')
        # A list containing readers for a given document, set() as we don't want to have duplicate readers values in it.
        readers = set()
        # For every row in the dictionary
        for row in df_dictionary:
            if user_id != row["visitor_uuid"]:
                readers.add(row["visitor_uuid"])
        return readers

    def get_documents(self, readers: set):
        """
        Gets the documents for a set of readers in a dictionary

        :param readers: Set of readers who have read a document
        :return: Dictionary containing a reader and the documents they have read.
        """
        # Initialise a dictionary 'result' to contain reader and the set of documents they have read.
        result = dict()
        for reader in readers:
            #  A dataframe with rows of only that reader
            sorted_df = self.df[(self.df["visitor_uuid"] == reader) & (self.df["event_type"] == "read")].loc[:,
                        ["subject_doc_id"]]
            # Drop any null (NA) values from the dataframe
            sorted_df = sorted_df[sorted_df["subject_doc_id"].notna()]
            # Covert dataframe to dictionary to iterate through rows faster. 'records' converts
            df_dictionary = sorted_df.to_dict('records')
            # A documents list containing documents read by that reader
            documents = set()
            # Iterate through rows
            for row in df_dictionary:
                # Add a document(s) to the set
                documents.add(row["subject_doc_id"])
            # Add the list of documents for the reader
            result.update({reader: documents})
        return result

    # HIGHER ORDER VERSION
    @staticmethod
    def sorting_with_higher_order(dictionary: dict, sorting_function):
        """
        Return the most favourite documents with document and their count as key value pairs, using a decorator function argument.
        The top 10 results are returned.

        :param dictionary: The dictionary containing the document as key and the documents they have read in a set as values
        :param sorting_function: The decorator function
        :param dictionary containing document's and their documents:
        :return: top 10 documents with their count
        """
        # Set which will contain all documents read by all readers
        documents = set()
        # Iterate over the 'dictionary' documents
        for document in dictionary.keys():
            # Add the documents in the dictionary documents to the documents set.
            documents = documents | set(dictionary[document])
        # Dictionary that contains the document and the the number of times the document occurs
        document_count = dict()
        # Iterate through the documents
        for document in documents:
            # For each document, use the sorting function to get the number of times that document has been read in the dictionary
            # This is done using the sorting function.
            document_count.update({document: sorting_function(document, dictionary)})
        # Sorts the dictionary document_count based on the number of occurrences, the count value
        document_count = dict(sorted(document_count.items(), key=operator.itemgetter(1), reverse=True))
        # Gets the first 10 pairs from the sorted_documents dictionary
        document_count = dict(itertools.islice(document_count.items(), 11))
        return document_count

    # THE HIGHER ORDER SORTING FUNCTION
    @staticmethod
    def get_document_counts(doc_id, dictionary):
        """
        A decorator functIon which takes in the document ID and a dictionary and then finds out the number of times that document ID
        is found in the dictionary's values. This is the sorting function.

        :param doc_id: The document ID
        :param dictionary: The dictionary containing readers as key and the set of documents they have read as values
        :return: The number of times the document is found in the dictionary's values.
        """
        # The number of times the document is found
        count = 0
        # Iterate through the dictionary's keys
        for reader in dictionary.keys():
            # Check if the document is found in the values of the dictionary for that reader key
            if doc_id in dictionary[reader]:
                # Increment the count for a document found
                count += 1
        # Return the count
        return count

    # UNUSED IMPLEMENTATION AND NON-HIGHER ORDER VERSION, THIS FUNCTION IS NO LONGER USED.
    # THE FUNCTION sorting_with_higher_order(dictionary, sorting_function) is used now.
    @staticmethod
    def old_sorting_function(dictionary: dict):
        """
        **THIS FUNCTION IS DEPRECATED**

        Sorts the dictionary containing readers and their read documents in the order of the most documents they have been read first.
        The top 10 results are returned.

        :param dictionary:
        :param dictionary containing reader's and their documents:
        :return top 10 documents:
        """
        set_of_documents = []
        for reader, documents in dictionary.items():
            for document in documents:
                set_of_documents.append(document)
        # Dictionary document_count to store the document as key and it's count as value from the documents dictionary
        document_count = dict()
        # Gets the document as key and it's number of occurrences into a dictionary document_count as value
        [document_count.update({document: document_count.get(document, 0) + 1}) for document in set_of_documents]
        # Sorts the dictionary document_count based on the number of occurrences
        sorted_document_count = dict(sorted(document_count.items(), key=operator.itemgetter(1), reverse=True))
        # Gets the first 10 pairs from the sorted_documents dictionary
        top_10 = dict(itertools.islice(sorted_document_count.items(), 11))
        return top_10

    @staticmethod
    def sort_graph_nodes(dictionary: dict):
        """
        This function takes in a dictionary of readers and the set of documents they have read and then returns a version of this dictionary
        which contain only the top 10 most read documents by their readers.

        :param dictionary: A dictionary containing reader's and their documents
        :returns: The same modified dictionary but with most read document's by the readers
        """
        # Dictionary which contains a document and a set of readers who have read that document as key value pairs.
        documents_readers = defaultdict(set)
        # This loop adds for each document in the dictionary, a set of it's readers to the documents_readers dictionary.
        for readers, documents in sorted(dictionary.items()):
            # Iterate through set of documents
            for document in documents:
                # Add document as key a the set of readers as value
                documents_readers[document].add(readers)

        # Sorts the dictionary documents_readers based on the len of readers.
        sorted_documents_readers = dict(sorted(documents_readers.items(), key=lambda i: len(i[1]), reverse=True))
        # Gets the first 10 pairs from the sorted_documents_readers dictionary
        top_10 = dict(itertools.islice(sorted_documents_readers.items(), 11))

        # A dictionary which contains the reader and the set of document's they have read as key value pairs.
        readers_documents = defaultdict(set)
        # This loop adds for each reader, a set of it's documents they have read to the readers_documents dictionary.
        # This loop will use the sorted top 10 values.
        for document, readers in sorted(top_10.items()):
            # Iterate through set of readers
            for reader in readers:
                # Add reader as key a the set of documents as value
                readers_documents[reader].add(document)
        return readers_documents

    def run_task_5(self, doc_id: str, user_id: str):
        """
        A method to run the task 5 using methods and functions written in this class

        :param doc_id: The input document ID
        :param user_id: The input user ID
        :return: A tuple containing the readers set and the output, a dictionary containing the sorted
        readers and the documents they have read.
        """
        readers = self.get_relevant_readers(doc_id, user_id)
        d = self.get_documents(readers)
        # We pass in the dictionary of readers and the documents they have read and the sorting function to the function sorting_with_higher_order
        output = self.sorting_with_higher_order(d, sorting_function=self.get_document_counts)
        # Return a tuple to print task 5 data.
        return readers, output

    def run_task_6(self, doc_id: str, user_id: str):
        """
        A method to run the task 6 using methods and functions written in this class. It simply displays the graph.

        :param doc_id: The input document ID
        :param user_id: The input user ID
        """
        readers = self.get_relevant_readers(doc_id, user_id)
        d = self.get_documents(readers)
        out = self.sort_graph_nodes(d)
        out[user_id] = {doc_id}
        graph.draw_graph(out, doc_id, user_id)
