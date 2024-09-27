#log_Scanner.py



#https://www.geeksforgeeks.org/parse-and-clean-log-files-in-python/ 
#https://stackoverflow.com/questions/16017419/python-read-log-files-and-get-lines-containing-specific-words
#https://blog.sentry.io/logging-in-python-a-developers-guide/
#https://medium.com/@jacksonsiachan/application-log-monitoring-and-parsing-using-python-95242135e047

import re 
from collections import defaultdict
from datetime import datetime
import os

# Paths to the log files
log_file_paths = [
    'C:/Users/cjsm1/OneDrive/Desktop/logs/access.log',
    'C:/Users/cjsm1/OneDrive/Desktop/logs/apache_logs.log',
    'C:/Users/cjsm1/OneDrive/Desktop/logs/audit.log'
]

# Threshold for failed login attempts
threshold_failed_logins=10

#sensitive info
sensitive_resources = ['/admin', '/settings', '/confidential']

def parse_log_line(line):
    """Parse a log line and return a dictionary with its details."""
    pattern = (r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>.*?)\] '
               r'"(?P<method>\S+) (?P<path>\S+) HTTP/\d\.\d" '
               r'(?P<status>\d+) (?P<size>\d+|-)')
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None

def is_failed_login(log_entry):
    """ failed login attempt is 401 - checks if entry is failed login"""
    return log_entry and log_entry['status'] == '401'

#new code
def is_sensitive_access(log_entry):
    return log_entry and log_entry['path'] in sensitive_resources

def is_unusual_time(log_entry):
    if log_entry:
        time_str = log_entry['time'].split()[0]
        log_time = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S')
        # Define normal business hours (e.g., 8 AM to 6 PM)
        start_time = log_time.replace(hour=8, minute=0, second=0, microsecond=0)
        end_time = log_time.replace(hour=18, minute=0, second=0, microsecond=0)
        return not (start_time <= log_time <= end_time)
    return False #end of new

def read_log_files(paths):
    """Read and parse multiple log files."""
    if not os.path.isfile(path):
        raise FileNotFoundError(f"The file '{path}' does not exist.")
    with open(path, 'r') as file:
        lines = file.readlines()
    return [parse_log_line(line) for line in lines]

'''  older method.
    all_log_entries = []
    for path in paths:
        if os.path.isfile(path):
            try:
                with open(path, 'r') as file:
                    lines = file.readlines()
                log_entries = [parse_log_line(line) for line in lines]
                all_log_entries.extend(log_entries)
            except Exception as e:
                print(f"Error reading file {path}: {e}")
        else:
            print(f"Error: The file '{path}' does not exist.")
    return all_log_entries  '''


def monitor_log_file(log_entries, threshold):
    """Monitor the log entries for unusual traffic."""
    failed_logins = defaultdict(int)
    #new code 
    sensitive_access = defaultdict(int)
    unusual_times = defaultdict(int)

    for path in file_paths:
        try:
            log_entries = read_log_file(path)
            for entry in log_entries:
                if is_failed_login(entry):
                    failed_logins[entry['ip']] += 1
                if is_sensitive_access(entry):
                    sensitive_access[entry['ip']] += 1
                if is_unusual_time(entry):
                    unusual_times[entry['ip']] += 1
        except FileNotFoundError as fnfe:
            print(fnfe)
        except Exception as e:
            print(f"An error occurred while reading the file '{path}': {e}")

    return failed_logins, sensitive_access, unusual_times
    #end of new code
  #alert = False
    '''
    for ip, count in failed_logins.items():
        if count > threshold:
            alert = True
            print(f"Alert: {count} failed login attempts from IP {ip}")

    return alert, failed_logins

def generate_report(failed_logins):
     older method to Generate a report of the monitoring activity
    report = "Failed Login Attempts Report\n"
    report += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    report += "IP Address       | Failed Attempts\n"
    report += "-" * 30 + "\n"
    for ip, count in failed_logins.items():
        report += f"{ip:<15} | {count}\n"   '''

def generate_report(failed_logins, sensitive_access, unusual_times):
    report = "Log Monitoring Report\n"
    report += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"

    report += "Failed Login Attempts\n"
    report += "IP Address       | Failed Attempts\n"
    report += "-" * 30 + "\n"
    for ip, count in failed_logins.items():
        report += f"{ip:<15} | {count}\n"

    report += "\nSensitive Resource Access\n"
    report += "IP Address       | Access Attempts\n"
    report += "-" * 30 + "\n"
    for ip, count in sensitive_access.items():
        report += f"{ip:<15} | {count}\n"

    report += "\nUnusual Login Times\n"
    report += "IP Address       | Unusual Times\n"
    report += "-" * 30 + "\n"
    for ip, count in unusual_times.items():
        report += f"{ip:<15} | {count}\n"

    return report

# Main workflow
    '''
    log_entries = read_log_files(log_file_paths)
    alert, failed_logins = monitor_log_file(log_entries, threshold)
    report = generate_report(failed_logins)'''

# Main workflow
failed_logins, sensitive_access, unusual_times = monitor_log_file(log_file_paths)
report = generate_report(failed_logins, sensitive_access, unusual_times)


# Print the report
print(report)

# Save the report to a file
report_path = 'C:/Users/cjsm1/OneDrive/Desktop/logs/failed_login_report.txt'
with open(report_path,'w') as file:
   file.write(report)
