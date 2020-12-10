# HealthBot Security KPI rules and playbooks

## Security playbooks

## Security rules

### Rule name: get-dev-key-status 
		> Description: "Determines if development keys have been revoked"
		> Synopsis: "State of development keys"
		> Rule file name: get-dev-key-state.rule

		> Supported products: MX 
		> Supported products: NFX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 


		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks if development keys have been left on the system.
		
		 If development keys were present, this rule will report the results
		 of the attempted revocation as Successful or a Failure.
		 This rule relies on a file present in 19.3R1 and further.
### Rule name: check-secureboot-status 
		> Description: "Checks that secure boot is running and enforced"
		> Synopsis: "System secure boot status"
		> Rule file name: test-secure-boot-status.rule

		> Supported products: EX 
		> Supported products: MX 
		> Supported products: NFX 
		> Supported products: PTX 
		> Supported products: QFX 
		> Supported products: SRX 

			> Supported platforms: [ EX4650-48Y EX9251 EX9253 ];
			> Supported platforms: [ MX10003 MX10008 MX2008 MX2010 MX2020 MX204 MX240 MX480 MX960 ];
			> Supported platforms: NFX250;
			> Supported platforms: [ PTX10008 PTX10016 PTX3000 PTX5000 ];
			> Supported platforms: [ QFX10002-60C QFX10008 QFX10016 QFX5110 QFX5120-48Y ];
			> Supported platforms: [ SRX1500 SRX4600 ];

		> Supported healthbot version: 1.0.1
		> Detals:
		 This rule checks if secure boot is running and enforced and returns
		 an error if it is not.
		 This rule relies on a file present in 19.3R1 and beyond.
		 This rule is only applicible to devices where secure boot is capable.
		 If this rule is run on a device that is incapable of secure boot,
		 the result will be "secureboot status is unknonw" and the rule should be
		 removed.
