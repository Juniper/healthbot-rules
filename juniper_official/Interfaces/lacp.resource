healthbot {
    topic protocols {
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