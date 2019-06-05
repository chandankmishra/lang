# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
[2019-05-31 04:09:41: INFO]: /static/images/123.png | 403, message='Forbidden'
[2019-05-31 04:09:42: INFO]: /account/abc | 401, message='Unauthorized'
[2019-05-31 04:09:44: INFO]: /account/def | 401, message='Unauthorized'
[2019-05-31 04:09:45: INFO]: /static/resources/567.js | 301, message='Moved Permanently'
[2019-05-31 04:09:48: INFO]: /account/abc
[2019-05-31 04:09:50: ERROR]: /transfer/123 | 500, message='Internal error: foo has no method bar'
[2019-05-31 04:09:51: FATAL]: /pages/fetch/123 | 500, message='Out of memory: process shutting down’
[2019-05-31 04:10:21: INFO]: /static/images/123.png | 403, message='Forbidden'
[2019-05-31 04:10:22: INFO]: /static/images/123.png | 403, message='Forbidden'
[2019-05-31 04:10:22: INFO]: /static/resources/567.js | 301, message='Moved Permanently'

ALL < DEBUG < INFO < WARN < ERROR < FATAL < OFF
"""

def parse_valid_log(log):
    return True/False, LogClass/None

class LogCleanup:
    def __init__(self):
        self.invalid = 'UNKNOWN'

    def get_updated_msg(msg):
        # will use self.invalid
        return new_msg
    
    def cleanup_log_msg(self, input_msgs):
        '''
        Return: None
        '''
        for index, msg in enumerate(input_msgs):
            status, log_obj =  parse_valid_log(msg)
            if status is True:
                continue
            input_msgs[index] = self.get_updated_msg(msg)

class LogFilter:
    def __init__(self):
        pass
    
    def filter_log_msgs(self, input_msgs):
        '''
        Return:
            output_msgs     FATAL and ERRORs
            count           count of the FATAL msgs
        '''
        output_msgs = []
        fatal_count = 0
        for msg in input_msgs:
            if msg.find(': ERROR]:') != -1:
                output_msgs.append(msg)
            elif msg.find('FATAL]') != -1:
                output_msgs.append(msg)
                fatal_count += 1
            elif msg.find('OFF]') != -1:
                output_msgs.append(msg)
        return output_msgs, fatal_count
    

input_msgs = [
    "[2019-05-31 04:09:41: INFO]: /static/images/123.png | 403, message='Forbidden'",
    "[2019-05-31 04:09:42: INFO]: /account/abc | 401, message='Unauthorized'",
    "[2019-05-31 04:09:44: INFO]: /account/def | 401, message='Unauthorized'",
    "[2019-05-31 04:09:45: INFO]: /static/resources/567.js | 301, message='Moved Permanently'",
    "[2019-05-31 04:09:48: ]: /account/abc",
    "[2019-05-31 04:09:50: ERROR]: /transfer/123 | 500, message='Internal error: foo has no method bar'",
    "[2019-05-31 04:09:51: FATAL]: /pages/fetch/123 | 500, message='Out of memory: process shutting down’",
    "[2019-05-31 04:10:21: INFO]: /static/images/123.png | 403, message='Forbidden'",
    "[2019-05-31 04:10:22: INFO]: /static/images/123.png | 403, message='Forbidden'",
    "[2019-05-31 04:10:22: INFO]: /static/resources/567.js | 301, message='Moved Permanently'"
]


cleanupObj = LogCleanup()
cleanupObj.cleanup_log_msg(input_msgs)

filterObj = LogFilter()
output_msgs, fatal_count = filterObj.filter_log_msgs(input_msgs)
print ("fatal_count:", fatal_count)
print ("output_msgs:", output_msgs)


