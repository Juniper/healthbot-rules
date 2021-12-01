healthbot {
    topic protocols {
        resource mpls-rsvp-lsp {
            description "Mpls lsp resources depends on rsvp";
            keys [ interface-name lsp-name];
            field lsp-name {
                type string;
                source {
                    rule protocol.mpls/check-lsp-state-oc {
                        field-name lsp-name;
                    }
                }
            }
            depends-on protocols/rsvp {
                term rsvp-neighbor-dependency {
                    locate-resource protocols/rsvp {
                        label-as rsvp-neighbor;
                        where {
                            matches-with "$interface-name" "$rsvp-neighbor:interface-name";
                        }
                    }
                }
            }
        }
    }
}