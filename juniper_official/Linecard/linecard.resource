healthbot {
    topic linecard {
        resource linecard {
            description "FPC resources";
            keys [ fpc-slot ];
            field fpc-slot {
                type string;
                source {
                    rule linecard.fpc.resource/monitor-denied-count {
                        field-name fpc-slot;
                    }
                }
                source {
                    rule linecard.fpc.resource/monitor-heap-memory {
                        field-name fpc-slot;
                    }
                }
                source {
                    rule linecard.fpc.resource/monitor-round-trip-time {
                        field-name fpc-slot;
                    }
                }
                source {
                    rule linecard.pfe.wedge/check-pfe-eachip-events {
                        field-name fpcnumber;
                    }
                }
                source {
                    rule linecard.pfe.wedge/check-pfe-luchip-events {
                        field-name fpcnumber;
                    }
                }
                source {
                    rule linecard.pfe.wedge/check-pfe-lueachip-events {
                        field-name fpcnumber;
                    }
                }
                source {
                    rule linecard.pfe.wedge/check-pfe-mqchip-events {
                        field-name fpcnumber;
                    }
                }
                source {
                    rule linecard.pfe.wedge/check-pfe-fpc-events {
                        field-name fpcnumber;
                    }
                }
                source {
                    rule linecard.pfe.wedge/check-pfe-wedge-events {
                        field-name fpcnumber;
                    }
                }
                source {
                    rule linecard.statistics/check-center-chip-fabric-in {
                        field-name target;
                    }
                }
                source {
                    rule linecard.statistics/check-center-chip-fabric-in-errors {
                        field-name target;
                    }
                }
                source {
                    rule linecard.statistics/check-center-chip-lookup-out {
                        field-name target;
                    }
                }
                source {
                    rule linecard.statistics/check-center-chip-lookup-in {
                        field-name target;
                    }
                }
            }
        }
        resource pfe {
            description "FPC PFE resources";
            keys [ fpc-slot pfe-num ];
            field fpc-slot {
                type string;
                source {
                    rule linecard.pfe/check-pfe-discards {
                        field-name fpc-no;
                    }
                }
                source {
                    rule linecard.pfe.resource/monitor-cos-queues-utilization {
                        field-name fpc-slot;
                    }
                }
                source {
                    rule linecard.pfe.resource/monitor-counter-and-expansion-memory {
                        field-name fpc-slot;
                    }
                }
                source {
                    rule linecard.pfe.resource/monitor-firewall-nh-encap-memory {
                        field-name fpc-slot;
                    }
                }
            }
            field pfe-num {
                type string;
                source {
                    rule linecard.pfe/check-pfe-discards {
                        field-name pfe-no;
                    }
                }
                source {
                    rule linecard.pfe.resource/monitor-cos-queues-utilization {
                        field-name pfe-num;
                    }
                }
                source {
                    rule linecard.pfe.resource/monitor-counter-and-expansion-memory {
                        field-name pfe-num;
                    }
                }
                source {
                    rule linecard.pfe.resource/monitor-firewall-nh-encap-memory {
                        field-name pfe-num;
                    }
                }
            }
            depends-on linecard/linecard {
                term fpc-dependency {
                    locate-resource linecard/linecard {
                        label-as fpc;
                        where {
                            matches-with "$fpc-slot" "$fpc:fpc-slot";
                        }
                    }
                }
            }
        }
    }
}