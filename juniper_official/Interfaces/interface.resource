healthbot {
    topic interfaces {
        resource interface-optics {
            description "Interface optics resources";
            keys interface-name;
            field interface-name {
                type string;
                source {
                    rule linecard.optical/check-optical-interfaces {
                        field-name interface-name;
                    }
                    rule linecard.optical/check-optics-power-openconfig {
                        field-name interface-name;
                    }                
                }
            }
            depends-on chassis/fpc-temperature {
                term fpc-dependency {
                    with-capture-group interface-split {
                        expression "-(\d+)\/\d+\/\d+";
                        field-name "$interface-name";
                    }
                    locate-resource chassis/fpc-temperature {
                        label-as fpc;
                        with-capture-group fpc-split {
                            expression "(\d+)";
                            field-name fpc;
                        }
                        where {
                            matches-with "$interface-split-1" "$fpc-split-1";
                        }
                    }
                }
            }
        }
        resource interface {
            description "Interface resources depends on optics";
            keys interface-name;
            field interface-name {
                type string;
                source {
                    rule interface.statistics/check-interface-status {
                        field-name interface-name;
                    }
                }
                source {
                    rule interface.statistics/check-interface-flaps {
                        field-name interface-name;
                    }
                }
                source {
                    rule interface.statistics/check-in-errors {
                        field-name interface-name;
                    }
                }
                source {
                    rule interface.statistics/check-out-errors {
                        field-name interface-name;
                    }
                }
                source {
                    rule interface.statistics/check-in-traffic {
                        field-name interface-name;
                    }
                }
                source {
                    rule interface.statistics/check-out-traffic {
                        field-name interface-name;
                    }
                }                
                source {
                    rule interface.statistics/check-interface-status-netconf {
                        field-name interface-name;
                    }
                }                                                
                source {
                    rule interface.statistics/check-interface-flaps-netconf {
                        field-name name;
                    }
                }
                source {
                    rule interface.statistics/check-interface-auto-negotiation-netconf {
                        field-name name;
                    }
                }
                source {
                    rule interface.statistics/check-queue-depth-netconf {
                        field-name interface-name;
                    }
                }
                source {
                    rule system.statistics/check-system-input-queues {
                        field-name interface;
                    }
                }
                source {
                    rule system.statistics/check-system-output-queues {
                        field-name check-system-output-queues;
                    }
                }
                source {
                    rule interface.statistics/check-interface-errors-netconf {
                        field-name name;
                    }
                }
                source {
                    rule interface.statistics/check-in-errors-iagent {
                        field-name name;
                    }
                }
                source {
                    rule interface.statistics/check-in-traffic-iagent {
                        field-name name;
                    }
                }
                source {
                    rule interface.statistics/check-interface-flaps-iagent {
                        field-name name;
                    }
                }
                source {
                    rule interface.statistics/check-interface-status-iagent {
                        field-name name;
                    }
                }
                source {
                    rule interface.statistics/check-out-traffic-iagent {
                        field-name name;
                    }
                }
                
            }
            depends-on interfaces/interface-optics {
                term optics-dependency {
                    locate-resource interfaces/interface-optics {
                        label-as optics;
                        where {
                            matches-with "$interface-name" "$optics:interface-name";
                        }
                    }
                }
            }
            depends-on linecard/linecard {
                term fpc-dependency {
                    with-capture-group interface-split {
                        expression "-(\d+)\/\d+\/\d+";
                        field-name "$interface-name";
                    }
                    locate-resource linecard/linecard {
                        label-as fpc;
                        with-capture-group fpc-split {
                            expression "(\d+)";
                            field-name fpc-slot;
                        }
                        where {
                            matches-with "$interface-split-1" "$fpc-split-1";
                        }
                    }
                }
            }
            depends-on linecard/pfe {
                term fpc-dependency {
                    with-capture-group interface-split {
                        expression "-(\d+)\/\d+\/\d+";
                        field-name "$interface-name";
                    }
                    locate-resource linecard/pfe {
                        label-as pfe;
                        with-capture-group fpc-split {
                            expression "(\d+)";
                            field-name fpc-slot;
                        }
                        where {
                            matches-with "$interface-split-1" "$fpc-split-1";
                        }
                    }
                }
            }
        }
        resource sub-interface {
            description "Sub-interface resources depends on ifd";
            keys [ interface-name sub-interface-index ];
            field interface-name {
                type string;
                source {
                    rule interface.statistics/check-ifl-status {
                        field-name interface-name;
                    }
                }
                source {
                    rule interface.statistics/check-ifl-in-traffic {
                        field-name interface-name;
                    }
                }
                source {
                    rule interface.statistics/check-ifl-out-traffic {
                        field-name interface-name;
                    }
                }
            }
            field sub-interface-index {
                type string;
                source {
                    rule interface.statistics/check-ifl-status {
                        field-name sub-interface-index;
                    }
                }
                source {
                    rule interface.statistics/check-ifl-in-traffic {
                        field-name sub-interface-index;
                    }
                }
                source {
                    rule interface.statistics/check-ifl-out-traffic {
                        field-name sub-interface-index;
                    }
                }
            }
            depends-on interfaces/interface {
                term ifd-dependency {
                    locate-resource interfaces/interface {
                        label-as ifd;
                        where {
                            matches-with "$interface-name" "$ifd:interface-name";
                        }
                    }
                }
            }
        }
        resource lacp {
            keys [ interface-name ];
            field interface-name {
                type string;
                source {
                    rule protocol.lacp/check-lacp-state-netconf {
                        field-name member-if-name;
                    }
                }				
                source {
                    rule protocol.lacp/check-lacp-statistics-openconfig {
                        field-name interface-name;
                    }
                }
            }
            depends-on interfaces/interface {
                term ifl-dependency {
                    locate-resource interfaces/interface {
                        label-as ifd;
                        where {
                            matches-with "$interface-name" "$ifd:interface-name";
                        }
                    }
                }
            }
        }
    }
}