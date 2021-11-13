log_file = open("um-server-01.txt") # This line connects this python file to um-server-01.tx file and names it log_file.


def sales_reports(log_file): # A function that takes a log file as its only argument.
    for line in log_file:  # This line goes through the file and returns each individual line (like a for loop).
        line = line.rstrip() # This line removes the trailing characters (default spaces).
        day = line[0:3]  # This line specifies and returns the day.
        if day == "Mon": # This line specifies to only return the day if its Tuesday.
            print(line) # This line prints the entire line that has a Tuesday as its day. (except now its Monday)


sales_reports(log_file)  # The function is invoked with the log_file
