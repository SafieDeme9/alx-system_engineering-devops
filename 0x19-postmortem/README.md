
# POSTMORTEM: Nginx server configuration issue

October 19, 2023

By Safietou Deme
![image](https://github.com/SafieDeme9/alx-system_engineering-devops/assets/62291831/c754d95d-f42d-4a84-adca-94df8a504957)



## Issue Summary

From 3:00 PM to 4:00 PM, we were getting a huge amount of failed requests resulting in server instability and degraded performance. The server was not keeping up with the number of requests arriving. The outage was caused by the lack of available file descriptors.

## Timeline 

3:00 PM: Initial report of server performance degradation

3:05 PM: Conducted benchmark tests to simulate HTTP requests to the server. Made 2000 requests to my server with 100 requests at a time. 943 requests failed.

3:15 PM: The team began investigating the issue by checking server logs and resource usage. Got a "Too many open files" error while checking error logs.

3:30 PM: Determined that the error was related to the file descriptor limit.

3:45 PM: checked the hard and soft values for the number of file handles and open files. Found nothing for nginx in /etc/security/limits.conf.

3:50 PM: Increased the limits for the user or group that runs Nginx. Did not run.

3:55 PM: Checked the /etc/default/nginx configuration file and saw that the limit where 15 changed to 4096.

4:00 PM: Conducted benchmark tests to ensure the issue was resolved. 0 requests failed.

## Root cause and resolution

The root cause of the incident was identified as a low file descriptor limit (limit) for the Nginx service. This limit restricted the number of open files, which proved insufficient to handle the traffic load and caused the server to fail in processing requests.

To resolve the issue, the team took the following immediate actions:

Increased the file descriptor limit in the Nginx configuration (/etc/default/nginx) from 15 to 4096.

Ran benchmark tests to verify that the server could handle the expected traffic load without errors.

## Corrective and preventative measures
To prevent similar issues in the future, the following preventive measures have been identified and will be implemented:

Regular Monitoring: Implement continuous monitoring of server resources, log files, and web server performance to detect and address issues proactively.

Automated Configuration Management: Expand the use of configuration management tools like Puppet to automate system configuration changes, including those affecting resource limits.

Resource Scaling: Review and adjust resource limits (e.g., file descriptor limits) to match expected traffic loads and server requirements.

Periodic Reviews: Conduct regular reviews of Nginx configurations and server settings to ensure they are optimized for current workloads.

Documentation: Maintain and update documentation detailing important system configurations and processes.
