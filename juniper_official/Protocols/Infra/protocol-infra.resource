healthbot {
    topic protocols {
        resource routing-instance {
            description "Routing instance resources";
            keys [ instance-name router-id ];
            field instance-name {
                type string;
                source {
                    rule protocol.infra/get-instance-details {
                        field-name instance-name;
                    }
                }
            }
            field router-id {
                type string;
                source {
                    rule protocol.infra/get-instance-details {
                        field-name router-id;
                    }
                }
            }
        }
	}
}