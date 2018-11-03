# Chassis management healthbot key performance indicators
# 
** Synopsis **

This folder contains healthbot rules and playbooks to check the chassis health and notify when anomaly

** Rule Index **

Rule1 – chassis-fan-health.rule – This rule checks health of fan and notify in case any of the health monitored fields crosses threshold   
Sensor type : iAgent    
Input variables : N/A    
Dependency file(s) : chassis-fan.yml    

Rule2 – chassis-temperature.rule – This rule checks health of whole chassis temperature and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : chassis_temperature_high_threshold(default value 55), chassis_temperature_low_threshold(default value 45)   
Dependency file(s): No   

Rule3 – fpc-temperature.rule – This rule checks health of FPC temperature and notify in case any of the health monitored fields crosses threshold    
sensor type: open-config   
Input variables : FPC_Slot_No(default value 0-9), FPC_Temperature_Higher_Threshold(default value 55), FPC_Temperature_Lower_Threshold(default value 45)   
Dependency file(s) : No   

Rule4 – pem-power-usage.rule –  This rule checks pem status and power usage and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : pem_power_usage_threshold(default value 888888880)   
Dependency file(s) : used-percentage.py   

Rule5 – re-cpu-temperature.rule – This rule checks health of RE CPU temperature and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : RE_CPU_Temperature_Higher_Threshold(default value 55), RE_CPU_Temperature_Lower_Threshold(default value 45), RE_Slot_No(default value 0-1)   
Dependency file(s) : No   

Rule6 – system-power-usage.rule – This rule checks system power usage and notify in case any of the health monitored fields crosses threshold   
sensor type: open-config   
Input variables : system_power_usage_threshold(default value 20)   
Dependency file(s) : used-percentage.py   

Rule7 – zone-power-usage.rule – This rule checks health of pem power zones usage and notify in case any of the health monitored fields crosses threshold   
sensor type: iAgent   
Input variables : zone_power_usage_threshold(default value 80)   
Dependency file(s) : used-percentage.py   


Playbook – chassis-kpis.playbook – This playbook checks health of chassis and notify in case any of the health monitored fields crosses threshold   
This playbook contains following rules:-   
chassis.fan/check-fan-health    
chassis.temperatures/check-fpc-temperature    
chassis.power/check-pem-power-usage    
chassis.power/check-system-power-usage    
chassis.power/check-zone-power-usage    
chassis.temperatures/check-chassis-temperature    
chassis.temperatures/check-re-cpu-temperature    
chassis.temperatures/check-re-temperature   

