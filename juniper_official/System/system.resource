healthbot {
    topic system {
        resource system-storage {
            description "System storage resources";
            keys [ mounted-on filesystem-name ];
            field mounted-on {
                type string;
                source {
                    rule system.storage/check-storage {
                        field-name mounted-on;
                    }
                }
                source {
                    rule system.statistics/check-system-storage-capacity {
                        field-name system-storage-mountpoint;
                    }
                }
            }
            field filesystem-name {
                type string;
                source {
                    rule system.storage/check-storage {
                        field-name filesystem-name;
                    }
                }
                source {
                    rule system.statistics/check-system-storage-capacity {
                        field-name filesystem-name;
                    }
                }
            }
        }
        resource system-memory {
            description "System memory resources depends on storage incase of virtual memory";
            keys [ routing-engine ];
            field routing-engine {
                type string;
                source {
                    rule system.memory/check-system-memory {
                        field-name routing-engine;
                    }
                }
                source {
                    rule system.cpu.memory/check-system-cpu-memory-snmp {
                        field-name description;
                    }
                }          
            }
            depends-on system/system-storage {
                term storage-dependency {
                    locate-resource system/system-storage {
                        label-as storage;
                        where {
                            matches-with "true" "true";
                        }
                    }
                }
            }
        }
        resource processes-memory {
            description "Processes memory resources depends on system memory";
            keys [ daemon ];
            field daemon {
                type string;
                source {
                    rule system.processes/check-process-memory{
                        field-name daemon;
                    }
                }
                source {
                    rule system/check-system-process-memory{
                        field-name cmd;
                    }
                }
            }
            field pid {
                type string;
                source {
                    rule system.processes/check-process-memory{
                        field-name pid;
                    }
                }
            }
            depends-on system/system-memory {
                term system-memory-dependency {
                    locate-resource system/system-memory {
                        label-as system-memory;
                        where {
                            matches-with "true" "true";
                        }
                    }
                }
            }
        }
        resource system-cpu {
            description "System cpu resources";
            keys [ routing-engine ];
            field routing-engine {
                type string;
                source {
                    rule system.cpu/check-system-cpu {
                        field-name routing-engine;
                    }
                }
                source {
                    rule system.cpu/check-system-cpu-load-average {
                        field-name slot;
                    }
                }     
                source {
                    rule system.cpu.memory/check-system-cpu-memory-snmp {
                        field-name description;
                    }
                }          
                source {
                    rule system.statistics/check-routing-engine-cpu-utilization {
                        field-name slot;
                    }
                }       
            }
        }
        resource processes-cpu {
            description "Processes cpu depends on system cpu";
            keys [ daemon ];
            field daemon {
                type string;
                source {
                    rule system.processes/check-process-cpu{
                        field-name daemon;
                    }
                }
            }
            field pid {
                type string;
                source {
                    rule system.processes/check-process-cpu{
                        field-name pid;
                    }
                }
            }
            depends-on system/system-cpu {
                term storage-dependency {
                    locate-resource system/system-cpu {
                        label-as cpu;
                        where {
                            matches-with "true" "true";
                        }
                    }
                }
            }
        }
    }
}