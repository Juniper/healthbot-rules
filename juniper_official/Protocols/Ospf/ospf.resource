healthbot {
    topic protocols {
        resource ospf {
            description "Ospf resources depends on interfaces within device and device-group";
            keys [ interface-name neighbor-id ];
            field interface-name {
                type string;
                source {
                    rule protocol.ospf/check-ospf-neighbor-information {
                        field-name interface-name;
                    }
                }
            }
            field neighbor-id {
                type string;
                source {
                    rule protocol.ospf/check-ospf-neighbor-information {
                        field-name neighbor-id;
                    }
                }
            }
            field dr-address {
                type string;
                source {
                    rule protocol.ospf/check-ospf-neighbor-information {
                        field-name dr-address;
                    }
                }
            }
            depends-on interfaces/sub-interface {
                term ifl-dependency {
                    with-capture-group ospf-interface-split {
                        expression "(.*)\.(\d+)";
                        field-name "$interface-name";
                    }
                    locate-resource interfaces/sub-interface {
                        label-as ifl;
                        where {
                            matches-with "$ospf-interface-split-1" "$ifl:interface-name";
                            matches-with "$ospf-interface-split-2" "$ifl:sub-interface-index";
                        }
                    }
                }
                term ifl-remote-dependency {
                	for-every-device {
            			label-as remote-device;
                    }
                    locate-resource remote-device:protocols/routing-instance {
                        label-as remote-routing-instance;
                        where {
                            matches-with "$neighbor-id" "$remote-routing-instance:router-id";
                        }
                    }
                    locate-resource protocol/routing-instance {
                        label-as local-routing-instance;
                    }
                    locate-resource remote-device:protocols/ospf {
                        label-as remote-ospf;
                        where {
                            matches-with "$local-routing-instance:router-id" "$remote-ospf:neighbor-id";
                            matches-with "$dr-address" "$remote-ospf:dr-address";
                        }
                    }
                    locate-resource remote-device:interfaces/sub-interface {
                        label-as remote-ifl;
                        with-capture-group ospf-remote-interface-split {
                        	expression "(.*)\.(\d+)";
                        	field-name "$remote-ospf:interface-name";
                        }
                        where {
                            matches-with "$ospf-remote-interface-split-1" "$remote-ifl:interface-name";
                            matches-with "$ospf-remote-interface-split-2" "$remote-ifl:sub-interface-index";
                        }
                    }
                }
            }
            depends-on interfaces/interface {
                term ifd-dependency {
                    with-capture-group ospf-interface-split {
                        expression "(.*)\.\d+";
                        field-name "$interface-name";
                    }
                    locate-resource interfaces/interface {
                        label-as ifd;
                        where {
                            matches-with "$ospf-interface-split-1" "$ifd:interface-name";
                        }
                    }
                }
            }
        }
    }
}
