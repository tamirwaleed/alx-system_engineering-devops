Postmortem: Outage on September 20th, 2024 (UTC+2)

Issue Summary
Duration:  
The outage occurred from 10:05 AM to 11:45 AM UTC+2 on September 20th, 2024, lasting 1 hour and 40 minutes.

Impact:  
The service slowdown affected approximately 40% of users across the platform. Users experienced high latency, with page load times exceeding 10 seconds, and intermittent failures when accessing certain core functionalities, particularly in processing payments and user account login.

Root Cause:  
A misconfiguration in the database connection pool led to the system exhausting available connections, causing bottlenecks in data retrieval processes.

---

Timeline

- 10:05 AM: Monitoring system triggered an alert due to increased latency in user requests.
- 10:10 AM: Engineer noticed a spike in error rates and began investigating the database server.
- 10:15 AM: Database performance metrics checked, indicating high connection wait times.
- 10:30 AM: Assumed the root cause to be excessive load and scaled additional database resources.
- 10:40 AM: Investigation revealed no improvement after scaling; team escalated the incident to the DB administration team.
- 11:00 AM: DBA team discovered misconfigured connection pool settings causing the exhaustion of available connections.
- 11:15 AM: Connection pool settings were updated, increasing the limit and optimizing the release of unused connections.
- 11:30 AM: Services gradually returned to normal after restarting affected application services.
- 11:45 AM: Full service restored, all systems operational.

---

Root Cause and Resolution

Root Cause:  
The incident was caused by a misconfiguration in the database connection pool settings. Specifically, the maximum connection limit was set too low to handle the peak traffic, leading to a situation where the application could not retrieve data from the database due to exhausted connections. Additionally, connections were not being released back to the pool promptly, worsening the situation and causing cascading failures across multiple services reliant on the database.

Resolution:  
The database connection pool settings were updated to increase the maximum number of connections. The pool’s timeout settings were adjusted to ensure unused connections were promptly released back into the pool. A restart of the application services was required to apply the updated configurations and clear stuck connections. Post-restart, the services stabilized, and normal operations resumed.

---

Corrective and Preventative Measures

Improvements/Fixes:
- A full audit of database connection pool settings across all services is needed to ensure configurations are appropriately set for peak loads.
- Enhancements to monitoring need to be made to track connection pool usage and alert when thresholds are being approached.

Tasks:
1. Audit connection pool settings: Review and optimize connection pool settings for all services.
2. Increase connection pool monitoring: Implement additional metrics to monitor connection pool usage, alerting before exhaustion occurs.
3. Patch application services: Ensure services are releasing connections back to the pool in a timely manner.
4. Run load tests: Perform stress tests to simulate peak usage scenarios and confirm the system can handle expected loads.
5. Update incident response playbook: Add procedures for investigating connection pool issues as part of standard incident response.

By implementing these steps, we aim to prevent similar outages and improve the system's resilience under heavy load conditions.
