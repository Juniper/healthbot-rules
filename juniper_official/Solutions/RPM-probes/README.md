# RPM Probes for SLA monitoring

This solution leverages the combining power of JUNOS Automation, JUNOS Telemetry and HealthBot to deliver a simple solution to perform SLA validation across the network.

The example topology used in this solution is shown in the picture below:

[Example Topology](pictures/Example_topology.png)

There are few elements of this solutions that require to be explained:


## SLA

The SLA monitoring systems monitors whether a SLA of 6-nines and 5-nines have been breached between two points of tests (i.e., between two probes).

A breach of the 6-nines SLA will trigger an YELLOW alarm while a breach on the 5-nines SLA will trigger a RED alarm. If the SLA is higher than 6-nines, it will trigger a GREEN alarm.

The probes can be designed according to your need. The probe configuration provided here as an example can be adapted to distribute them according to your needs.

However, it is important to keep probe-count and probe-interval as defined in the examples as this information is used to infer the outage time (i.e., how long the outage was).

Additionally, the SLA is calculated over the period of 1-YEAR. Hence, it is important to configure your retention policy to 1-YEAR (if using in production).

> Note: this can be worked around if the InfluxDB query defined in the UDF `cumm-pkt-loss-from-db.py` is adjusted to be performed within a particular time-frame.
> Note2: this behaviour is a design decision in order to keep things simple


## Custom OpenConfig sensor for RPM probes

This solution relies on a model driven OC telemetry sensor. Consequently, you must install the YANG on each VMX/MX where the RPM probe will be running.

[OC YANG model file](oc_yang_model/xmlproxyd_rpm.yang)

To install the YANG model, follow the instructions below:

1) Upload the YANG model to the router

```
scp xmlproxyd_rpm.yang <user>@<router>:
```

2) Load the YANG model

```
request system yang add package rpm module xmlproxyd_rpm.yang proxy-xml
```

3) Verify the model was loaded

```
jcluser@pe1> show system yang package
Package ID            :rpm
XML Proxy YANG Module(s) :xmlproxyd_rpm.yang
```


## gRPC must be enabled in the routers where the RPM probes are running

To enable gRPC in the router, use the configuration below:

```
system {
    services {
        extension-service {
            request-response {
                grpc {
                    clear-text;
                }
            }
        }
    }
}
```


## RPM probe configuration

The probe configuration for each of the probes in the example topology are listed here.

> Note: both PE1 and PE2 also run RPM probes

[Probe configuration for PE1](probes_configuration/pe1.cnf)

[Probe configuration for PE2](probes_configuration/pe2.cnf)

[Probe configuration for probe1](probes_configuration/probe1.cnf)

[Probe configuration for probe2](probes_configuration/probe2.cnf)

[Probe configuration for probe3](probes_configuration/probe3.cnf)

[Probe configuration for probe4](probes_configuration/probe4.cnf)

[Probe configuration for probe5](probes_configuration/probe5.cnf)

[Probe configuration for probe6](probes_configuration/probe6.cnf)


## HealthBot UDF

This HealthBot playbook uses two user defined functions. 

Make sure you upload both files to `/var/local/healthbot/input` directory before running the playbook.

[Cummulative packet loss from DB](udf/cumm-pkt-loss-from-db.py)

[SLA](udf/sla.py)


## Behaviour if the probe goes offline (RED vs GREY)

If the probe goes offline, instead of a RED alarm, the probe will turn grey. 

One way to avoid the scenario above is by configuring the OpenConfig subscription to the probes via the management address (fxp0).
Of course this assumes that you have both an inline path and out-of-band path to the probe.

However, the probe will still turn grey when it is completely offline (both inline and out-of-band paths).

Check out the suggested traffic flow for the probes here: [Traffic Flow](pictures/6.Topology_traffic_flow.png)



# Playbook and rule files

[RPM probe solution file](rpm-probe.playbook)

[RPM probe rule file](rpm-probe.rule)


# Screenshots of the playbook in action

[1: Playbook deployed to device group PROBES](pictures/1.Playbook-deployed-to-PROBES-device-group.png)

[2: SLA is all GREEN as no outages have happened so far](pictures/2.SLA_is_all_green_as_no_outages_have_occurred.png)

[3: Probe3 went offline. SLA of 6-nines is the first one to be breached](pictures/3.Probe3_went_offline_first_SLA_to_breach_is_6_nines.png)

[4: Details of the breached SLA](pictures/4.Details_of_the_SLA_breach.png)

[5: After just over 5 minutes, the 5-nines SLA gets breached](pictures/5.After_just_over_5_minutes_the_5_nines_SLA_gets_breached.png)


