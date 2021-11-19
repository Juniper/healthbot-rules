healthbot {
    topic protocols {
        resource isis {
            description "Isis resources depends on sub-interface";
            keys [ interface-name ];
            field system-id {
                type string;
                source {
                    rule protocol.isis/check-isis-adjacencies {
                        field-name system-id;
                    }
                }
            }
            field interface-name {
                type string;
                source {
                    rule protocol.isis/check-isis-adjacencies {
                        field-name interface-id;
                    }
                }
                source {
                    rule protocol.isis/check-isis-statistics {
                        field-name interface-name;
                    }
                }
            }            
            depends-on interfaces/sub-interface {
                term ifl-dependency {
                    with-capture-group isis-interface-split {
                        expression "(.*)\.(\d+)";
                        field-name "$interface-name";
                    }
                    locate-resource interfaces/sub-interface {
                        label-as ifl;
                        where {
                            matches-with "$isis-interface-split-1" "$ifl:interface-name";
                            matches-with "$isis-interface-split-2" "$ifl:sub-interface-index";
                        }
                    }
                }
            }
        }
    }
}