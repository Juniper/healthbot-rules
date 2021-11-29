healthbot {
    topic protocols {
        resource lldp {
            description "Lldp resources depends on interface";
            keys [ interface-name ];
            field interface-name {
                type string;
                source {
                    rule protocol.lldp/check-lldp-session {
                        field-name interface-name;
                    }
                }
                source {
                    rule protocol.lldp/check-lldp-session-statistics {
                        field-name interface-name;
                    }
                }
                source {
                    rule protocol.lldp/get-lldp-state {
                        field-name interface-name;
                    }
                }
            }
            depends-on interfaces/interface {
                term lldp-dependency {
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