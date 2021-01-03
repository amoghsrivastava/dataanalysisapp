# Python library imports
import argparse
import time

# Local library imports
import file_manager as fm
import data_processing as pr


def main():
    parser = argparse.ArgumentParser(description="Python Data Analysis App",
                                     epilog="A simple data intensive python app built for F20SC Coursework 2")
    parser.add_argument("-u", "--userid", type=str, help="A visitor/reader UUID", metavar="", default="")
    parser.add_argument("-d", "--docid", type=str, help="A document UUID", metavar="")
    parser.add_argument("-t", "--task", type=str, help="The task you want to run", metavar="",
                        choices=["2a", "2b", "3a", "3b", "4", "5", "6"], required=True)
    parser.add_argument("-f", "--file", type=str, help="The path of the JSON file with the data to be analysed",
                        metavar="", required=True)
    args = parser.parse_args()
    start_time = time.time()
    run(args)
    print("")
    print("Task %s completed in: %s seconds" % (args.task, round((time.time() - start_time), 3)))


def run(args):
    print("")  # Leave a gap
    print("Starting task %s" % args.task)
    # If the task value is 2a, then run
    if args.task == "2a":
        # Create file object
        f = fm.FileManager(args.file)
        # Create the dataframe
        df = f.parse_json_dataframe()
        # If the df was not empty, then run this
        if not df.empty:
            # Send it to dataprocessing,
            dataset = pr.DataProcessing(df)
            # Run the task for 2a.
            dataset.histogram_country(args.docid)
    # If the task value is 2b, then run
    elif args.task == "2b":
        f = fm.FileManager(args.file)
        df = f.parse_json_dataframe()
        if not df.empty:
            dataset = pr.DataProcessing(df)
            dataset.histogram_continent(args.docid)
    elif args.task == "3a":
        f = fm.FileManager(args.file)
        df = f.parse_json_dataframe()
        if not df.empty:
            dataset = pr.DataProcessing(df)
            dataset.histogram_browsers_a()
    elif args.task == "3b":
        f = fm.FileManager(args.file)
        df = f.parse_json_dataframe()
        if not df.empty:
            dataset = pr.DataProcessing(df)
            dataset.histogram_browsers_b()
    elif args.task == "4":
        f = fm.FileManager(args.file)
        df = f.parse_json_dataframe()
        if not df.empty:
            dataset = pr.DataProcessing(df)
            output = dataset.visitor_readtimes()
            print("Reader(s):        |  Total readtime(s): ")
            print("------------------------------------------------")
            for k, v in output.items():
                print('%s  |  %s' % (k, v))
    elif args.task == "5":
        f = fm.FileManager(args.file)
        df = f.parse_json_dataframe()
        if not df.empty:
            dataset = pr.DataProcessing(df)
            readers, output = dataset.run_task_5(args.docid, args.userid)
            print("Relevant readers for the document:")
            print("Reader(s)  ")
            print("-----------")
            for reader in readers:
                print("%s      |" % reader[-4:])
            print("")
            print("Top 10 most read (also-like) documents: ")
            print("Document(s)  |   Times Read")
            print("----------------------------")
            for documents, count in output.items():
                if documents[-4:] == args.docid[-4:]:
                    print("%s (*)     |   %s" % (documents[-4:], count))
                else:
                    print("%s         |   %s" % (documents[-4:], count))
            print("Where (*) is the input document.")
    elif args.task == "6":
        f = fm.FileManager(args.file)
        dataset = pr.DataProcessing(f.parse_json_dataframe())
        dataset.run_task_6(args.docid, args.userid)
    else:
        return "No conditions set"


if __name__ == '__main__':
    # Program starts here.
    main()
