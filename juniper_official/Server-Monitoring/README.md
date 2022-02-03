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
		 8) Rule check-node-time, collects current node time.
		 9) Rule check-system-reboot, checks if system has rebooted
		    in the last 5 minutes.

## Server-Monitoring rules

### Rule name: check-cpu-usage 
		> Description: "Collects system CPU statistics and notifies anomaly in case cpu utilization is above threshold"
		> Synopsis: "CPU Usage KPI"
		> Rule file name: check-cpu-usage.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if cpu usage is exceeding threshold default value for 3 offsets and raises red alarm,
		 else dashboard color is set to green.
		 Two input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.Default is 70.
		   2) "freq" is the interval between data points.Default is 60.
		
### Rule name: check-disk-read-usage 
		> Description: "Collects disk read information and notifies anomaly in case bytes-total,completed-total and time-seconds-total used percentage values are above threshold for 3 offsets"
		> Synopsis: "Disk read usage KPI"
		> Rule file name: check-disk-read-usage.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if disk read usage fields exceed threshold value and raises red alarm if
		 usage is more than threshold for 3 offsets else dashboard color is set to green.
		 Three input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		   2) "threshold-increase" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-increase value.
		   3) "freq" is the interval between data points.
		
		
### Rule name: check-disk-write-usage 
		> Description: "Collects disk write information and notifies anomaly in case bytes-total,completed-total and time-seconds-total used percentage values are above threshold for 3 offsets"
		> Synopsis: "Disk write usage KPI"
		> Rule file name: check-disk-write-usage.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if disk write usage fields exceed threshold value and raises red alarm if
		 usage is more than threshold for 3 offsets else dashboard color is set to green.
		 Three input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		   2) "threshold-increase" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-increase value.
		   3) "freq" is the interval between data points.
		
### Rule name: check-filesystem-usage 
		> Description: "Collects file system information and notifies anomaly in case device error percentage value are is threshold for 3 offsets"
		> Synopsis: "File  system kpi"
		> Rule file name: check-filesystem-usage.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if file sytem device error percent is exceeding threshold value and raises red alarm if
		 it is more than threshold for 3 offsets else dashboard color is set to green.
		 One input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		   2) "threshold-increase" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-increase value.
		   3) "freq" is the interval between data points.
### Rule name: check-load 
		> Description: "Collects system CPU statistics and notifies anomaly in case cpu utilization for 1min,5min and 15 mins are above threshold for 3 offsets"
		> Synopsis: "CPU load kpi "
		> Rule file name: check-load.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if cpu load average for 1min,5mins and 15mins is exceeding threshold and raises
		 red alarm if usage is more than threshold for 3 offsets else dashboard color is set to green.
		 One input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.Default is 70.
		
### Rule name: check-network-usage 
		> Description: "Collects Network statistics and notify anomaly in case transmit, receive and multicast error is above threshold for 3 offsets"
		> Synopsis: "Network usage KPI "
		> Rule file name: check-network-usage.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if network usage fields are exceeding threshold value and raises red alarm if
		 it is more than threshold for 3 offsets else dashboard color is set to green.
		
		 One input control detection.
		
		   1) "threshold" is used to check if the used percentage is
		      increasing by more than the threshold value.
		
### Rule name: check-node-memory 
		> Description: "Collects system Memory statistics and notifies anomaly in case free and inactive bytes increase is above threshold for 3 offsets"
		> Synopsis: "Memory kpi"
		> Rule file name: check-node-memory.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if node memory fields are increasing by more than threshold value, raises red
		 alarm if it is more than threshold for 3 offsets else dashboard color is set to green.
		 One input control detection.
		
		   1) "threshold-diff" is used to check if the difference of current and previous
		      values is increasing by more than the threshold-diff.
		
### Rule name: check-node-time 
		> Description: "Collects system current time and is referred to another rule"
		> Synopsis: "system current-time KPI"
		> Rule file name: check-node-time.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Collects current node time and is referenced by "check-system-reboot" rule
		
### Rule name: check-system-reboot 
		> Description: "Checks if system has rebooted  in the last 5 minutes"
		> Synopsis: "Boot-time KPI"
		> Rule file name: check-system-reboot.rule
		> Sensor type: server-monitoring 


		> Other vendor product support: linux 

		> More details:
		 Checks if system has rebooted in the last 5 minutes, raises red alarm if it
		 has rebooted else dashboard color is set to green.
		 One input control detection.
		
		   1) "frequency" is the duration between metrics.Default is 300s.
		
		
