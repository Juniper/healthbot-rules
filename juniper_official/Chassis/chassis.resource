healthbot {
    topic chassis {
        resource fan {
            description "Chassis fan resources";
            keys [ fan-name ];
            field fan-name {
                type string;
                source {
                    rule chassis.fan/check-fan-health {
                        field-name name;
                    }
                }
            }
        }
        resource chassis-temperature {
            description "Chassis temperature resources depends on chassis fan health";
            keys [ chassis-name ];
            field chassis-name {
                type string;
                source {
                    rule chassis.temperatures/check-chassis-temperature {
                        field-name chassis-name;
                    }
                }
            }    
            depends-on chassis/fan {
                term fan-dependency {
                    locate-resource chassis/fan {
                        label-as fan;
                        where {
                            matches-with "true" "true";
                        }
                    }
                }
            }
        }
        resource re-temperature {
            description "Routing engine temperature resources depends on chassis temperature";
            keys [ routing-engine ];
            field routing-engine {
                type string;
                source {
                    rule chassis.temperatures/check-re-temperature {
                        field-name routing-engine;
                    }
                }
            }    
            depends-on chassis/chassis-temperature {
                term chassis-temperature-dependency {
                    locate-resource chassis/chassis-temperature {
                        label-as chassis-temperature;
                        where {
                            matches-with "true" "true";
                        }
                    }
                }
            }
        }
        resource re-cpu-temperature {
            description "Routing engine cpu temperature resources depends on re temperature";
            keys [ routing-engine ];
            field routing-engine {
                type string;
                source {
                    rule chassis.temperatures/check-re-cpu-temperature {
                    	field-name routing-engine;
                    }
                }
            }    
            depends-on chassis/re-temperature {
                term re-temperature-dependency {
                    locate-resource chassis/re-temperature {
                        label-as chassis-re-temperature;
                        where {
                            matches-with "true" "true";
                        }
                    }
                }
            }
        }
        resource fpc-temperature {
            description "Fpc temperature resources depends on chassis temperature";
            keys [ fpc ];
            field fpc {
                type string;
                source {
                    rule chassis.temperatures/check-fpc-temperature {
                        field-name fpc;
                    }
                }
            }    
            depends-on chassis/chassis-temperature {
                term chassis-temperature-dependency {
                    locate-resource chassis/chassis-temperature {
                        label-as chassis-re-temperature;
                        where {
                            matches-with "true" "true";
                        }
                    }
                }
            }
        }
        resource system-power {
            field system-power-remaining-in-percentage {
                type string;
                source {
                    rule chassis.power/check-system-power-usage {
                        field-name system-power-remaining-in-percentage;
                    }
                }
			}
            depends-on chassis/zone-power {
                term zone-power-dependency {
                    locate-resource chassis/zone-power {
                        label-as system-power;
                        where {
                            matches-with "true" "true";
                        }
                    }						
                }
            }			
        }
        resource zone-power {
            keys [ zone ];		
            field zone {
                type string;
                source {
                    rule chassis.power/check-zone-power-usage {
                        field-name zone;
                    }
                }
			}
            depends-on chassis/pem-power {
                term pem-power-dependency {
                    locate-resource chassis/pem-power {
                        label-as pem-power;
                        where {
                            matches-with "true" "true";
                        }
                    }						
                }
            }			
        }		
        resource pem-power {
            keys [ pem-slot ];		
            field pem-slot {
                type string;
                source {
                    rule chassis.power/check-pem-power-usage {
                        field-name pem-slot;
                    }
                }
			}
            depends-on chassis/chassis-temperature {
                term temperature-dependency {
                    locate-resource chassis/chassis-temperature {
                        label-as temperature;
                        where {
                            matches-with "true" "true";
                        }
                    }						
                }
            }
        }		
    }
}