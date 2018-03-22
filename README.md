How to write rules

Please follow the DATA model user guide present https://junipernetworks.sharepoint.com/:w:/r/sites/iceberg-dev-planner/_layouts/15/doc.aspx?sourcedoc=%7B2ea1add1-e2c7-405d-9ae8-a4ca9bcbc793%7D&action=edit&uid=%7B2EA1ADD1-E2C7-405D-9AE8-A4CA9BCBC793%7D&ListItemId=69&ListId=%7BF3778718-EBDE-41A7-8C45-A231942D80E7%7D&odsp=1&env=prod
Submit only the .conf files

How to contribute

- Only juniper employees can contribute to the 'Juniper_Official' folder. Pull request raised by any other contributor will be automatically closed. 
- Juniper employee needs to subscribe to the alias 'jfit-rules-official'
- Rest of the community contribution will go to the 'Community_Supplied' folder

Automated Testing

- CI pipeline is run for every submitted and updated pull request. Reviewer will only review the rules after it passes the automated syntax testing.
- Any syntax error occured on all the changed files will be reported back as a review comment.
- CI pipeline can also be triggered by commenting 'Jenkins please retry a build' on the pull request
