# HealthBot Server-Monitoring KPI rules and playbooks

## Server-Monitoring playbooks
### Playbook name: server-monitoring 
		> Description: "Playbook to monitor cpu,memory,disk read/write,file-system,network and node-time using Sensor monitoring ingest"
		> Synopsis: "Sensor monitoring KPI"
		> Playbook file name: server-monitoring.playbook
		> Details:
		 Playbook contains 8 rules which detects anomaly
		 and notifies when anomalies are found.
		
		 1) Rule check-cpu-usage checks for anomalies
		    in cpu usage and notifies on the dashboard.
		 2) Rule check-disk-read-usage checks for anomalies
		    in disk read usage and notifies on the dashboard.
		 3) Rule check-disk-write-usage checks for anomalies
		    in disk write usage and notifies on the dashboard.
		 4) Rule check-filesystem-usage checks for anomalies
		    in filesystem usage and notifies on the dashboard.
		 5) Rule check-load checks for anomalies
		    in cpu load and notifies on the dashboard.
		 6) Rule check-network-usage checks for anomalies
		    in network usage and notifies on the dashboard.
		 7) Rule check-node-memory checks for anomalies
		    in node memory and notifies on the dashboard.
		 8) Rule check-node-time checks for anomalies in node time
		    and notifies on the dashboard.

## Server-Monitoring rules

### Rule name: check-cpu-usage 
		> Description: "Checks CPU total seconds"
		> Synopsis: "CPU Usage KPI"
		> Rule file name: check-cpu-usage.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if cpu usage is exceeding threshold value and raises alarm.
		
		 Two input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		   2) "freq" is the interval between data points.
		
### Rule name: check-disk-read-usage 
		> Description: "Disk read information"

		> Rule file name: check-disk-read-usage.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if disk read usage fields exceed threshold value and raises alarm.
		 Three input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		   2) "threshold-increase" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-increase value.
		   3) "freq" is the interval between data points.
		
		
### Rule name: check-disk-write-usage 
		> Description: "Disk write information"

		> Rule file name: check-disk-write-usage.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if disk write usage fields exceed threshold value and raises alarm.
		 Three input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		   2) "threshold-increase" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-increase value.
		   3) "freq" is the interval between data points.
		
### Rule name: check-filesystem-usage 
		> Description: "Checks file sytem usage"
		> Synopsis: "File  system kpi"
		> Rule file name: check-filesystem-usage.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if file sytem usage is exceeding threshold value and
		 raises alarm.
		 One input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		   2) "threshold-increase" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-increase value.
		   3) "freq" is the interval between data points.
### Rule name: check-load 
		> Description: "CPU load average for 1min,5min and 15 mins"
		> Synopsis: "CPU load kpi "
		> Rule file name: check-load.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if cpu load average for 1min,5mins and 15mins is exceeding threshold
		 value and raises alarm.
		 One input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasinng by more than the threshold value.
		
### Rule name: check-network-usage 
		> Description: ""

		> Rule file name: check-network-usage.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if network usage fields are exceeding threshold value and raises alarm.
		
		 One input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		
### Rule name: check-node-memory 
		> Description: "Check node memory"
		> Synopsis: "Memory kpi"
		> Rule file name: check-node-memory.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if node memory fields are increasing by more than threshold value and
		 raises alarm when anomalies are present.
		 One input control detection.
		
		   1) "threshold-diff" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-diff.
		
### Rule name: check-node-time 
		> Description: "Checks system time is increasing "

		> Rule file name: check-node-time.rule
		> Sensor type: server-monitoring 




		> More details:
		 Checks if node time is increasing every minute else raises alarm
		
