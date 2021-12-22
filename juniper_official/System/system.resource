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
    }
}
