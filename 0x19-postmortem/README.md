## Postmortem

Learning how to write an Incident Report, also referred to as a Postmortem. This postmortem follows the guidelines used closely by Google engineers to file reports. The report is made up of five parts: an issue summary, a timeline, root cause analysis, resolution and recovery, and corrective and preventative measures. Let's review each of these parts in detail.

### Issue Summary

A short summary of the incident, detailing:
- Duration: [start time] to [end time] (UTC)
- Impact: Most user requests resulted in 500 errors; at peak, 100% error rate.
- Root Cause: [Brief statement of the root cause]

### Timeline

- Timezone: [Specify timezone]
- Outage Duration: [Start time] to [End time] (UTC)
-  [Start time] - Outage began
-  [Notification time] - Staff was notified
-  [Actions/events] - Description of actions taken or events during outage
-  [Restoration time] - Service was restored

### Root Cause

Detailed explanation of the root cause without sugarcoating. Include:
- Sequence of events leading to the incident
- Factors contributing to the incident

### Resolution and Recovery

Detailed explanation of the actions taken to resolve the issue:
- Actions taken: [List actions with times]
- Recovery process: [Description of recovery process]

### Corrective and Preventative Measures

List of corrective actions taken and preventative measures for the future:
- Preventative measures: [List ways to prevent recurrence]
- Lessons learned: What can be improved for handling similar incidents in the future?
