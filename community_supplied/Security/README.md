# Security management healthbot rules
#
** Synopsis **

This folder contains healthbot rules to check security based metrics and notify
when they are anomalous.

** Rule Index **

Rule1 - get-dev-key-state.rule - This rule checks the state of development keys
on the host and will notify if the state is unknown or they were unable to be
revoked. This rule only applies to specific platforms. Rule must be run as root.
Sensor type : iAgent
Input variables : N/A
Dependency file(s) : get-dev-key-state.yml get-dev-key-state.py

Rule2 - test-secure-boot-status.rule - This rule checks checks if secureboot is
enabled and enforced and will return with an error state otherwise. This rule
only applies to platforms where secureboot is available. Rule must be run as
root.
Sensor type: iAgent
Input variables : N/A
Dependency file(s): test-secure-boot-status.yml test-secure-boot-status.py
