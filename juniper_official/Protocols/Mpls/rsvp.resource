healthbot {
    topic protocols {
        resource rsvp {
            description "Rsvp resources depends on sub-interface";
            keys [ interface-name];
            field interface-name {
                type string;
                source {
                    rule protocol.mpls/check-rsvp-neighbor-state-oc {
                        field-name neighbor-interface;
                    }
                }
                source {
                    rule protocol.mpls/check-te-rsvp-interface-errors-oc {
                        field-name te-interface;
                    }
                }
            }
            field neighbor-address {
                type string;
                source {
                    rule protocol.mpls/check-rsvp-neighbor-state-oc {
                        field-name neighbor-address;
                    }
                }
            }
            depends-on interfaces/sub-interface {
                term ifl-dependency {
                    with-capture-group rsvp-interface-split {
                        expression "(.*)\.(\d+)";
                        field-name "$interface-name";
                    }
                    locate-resource interfaces/sub-interface {
                        label-as rsvp;
                        where {
                            matches-with "$rsvp-interface-split-1" "$rsvp:interface-name";
                            matches-with "$rsvp-interface-split-2" "$rsvp:sub-interface-index";
                        }
                    }
                }
            }
        }
    }
}