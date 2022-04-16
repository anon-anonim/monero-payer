import multiprocessing

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() + 1
loglevel = 'info'
accesslog = '-'
errorlog = '-'
