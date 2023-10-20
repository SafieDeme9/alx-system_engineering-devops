# POSTMORTEM : Nginx server configuration issue

October 19, 2023

By Safietou Deme


## Issue Summary

From 3:00 PM to 4:00 PM, we were getting a huge amount of failed requests resulting in server instability and degraded performance. The server was not keeping up woth the number of requests arriving. The outage was cause by the lack of available file descriptors.

## Timeline 

3:00 PM: Initial report of server performance degradation 
3:05 PM: Conducted benchmark tests to simulate HTTP requests to the server. Made 2000 requests to my server with 100 requests at a time. 943 requests failed.
3:15 PM: The team began investigating the issue by checking server logs and resource usage. Got "Too many open files" error while checking error logs.
3:30 PM: Determined that the error was related to the file descriptor limit.
3:45 PM: checked the hard and soft values for the number of file handles and open files. Found nothing for nginx in /etc/security/limits.conf.
3:50 PM: Increased the limits for the user or group that runs Nginx. Did not run.
3:55 PM: Check the /etc/default/nginx configuration file saw that the limit where 15 changed it to 4096.
4:00 PM: Conducted benchmark tests to ensure the issue was resolved. 0 request failed.

## Root cause and resolution

The root cause of the incident was identified as a low file descriptor limit (ulimit) for the Nginx service. This limit restricted the number of open files, which proved insufficient to handle the traffic load and caused the server to fail in processing requests.


At 3:00 PM it was reported to us
