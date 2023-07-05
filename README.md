# Azure AD User Enumeration Tool

The Azure AD User Enumeration Tool is a Python script that allows you to enumerate valid Azure AD user email IDs. By providing a file containing names, the tool will attempt to find the corresponding valid email IDs of users in Azure AD.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/NotSoSecure/AzUserEnum.git
   ```

2. Navigate to the project directory:
    ```
    cd azure-ad-user-enumeration
    ```

## Prerequisites
Before running the script, ensure that you have the following:

- Valid AWS IAM user credentials with API Gateway access.
    - Go to the AWS Management Console.
    - Open the IAM (Identity and Access Management) service.
    - In the left navigation pane, click on "Users" to view the list of IAM users.
    - Locate the IAM user for which you want to grant API Gateway access and click on its name to open the user's details.
    - In the "Permissions" tab, click on the "Add permissions" button.
    - Select "Attach existing policies directly" to associate an existing policy with the user.
    - In the search box, type "AmazonAPIGatewayAdministrator" and select the policy from the list.
    - click on the "Next: Review" button.
    - Review the information and make sure it is correct. Then click on the "Add permissions" button to grant API Gateway access to the IAM user.

- An API Gateway need to be created in your AWS account.
   - Open the API Gateway service from the list of available services.
   - Click on "Create API" to start creating a new API.
   - Choose the type of API you want to create. You can select either REST or WebSocket API. For this example, let's choose REST API.
   - Select the "New API" option and give your API a name.
   - Choose the endpoint type for your API. You can choose either regional or edge-optimized. Regional endpoints are recommended for most use cases.
   - Click on "Create API" to create your API.

To configure your AWS credentials and CLI, run the following command and provide the necessary information:

```
aws configure
```

## Usage
1. Prepare a file named `users.txt` containing the names of users for enumeration, with each name on a new line.

2. Run the script:
   ```
   python AzUserEnum.py -f users.txt -d azurecloud.com
   ```
   The script will attempt to find valid email IDs for each name in Azure AD.

3. The script will output the valid email IDs found for each name, or indicate if no valid email ID was found.
   ```
                      _    _                       ______
        /\           | |  | |                     |  ____|
       /  \     ____ | |  | |  ___    ___   _ __  | |__     _ __    _   _   _ __ ___
      / /\ \   |_  / | |  | | / __|  / _ \ | '__| |  __|   | '_ \  | | | | | '_ ` _ \
     / ____ \   / /  | |__| | \__ \ |  __/ | |    | |____  | | | | | |_| | | | | | | |
    /_/    \_\ /___|  \____/  |___/  \___| |_|    |______| |_| |_|  \__,_| |_| |_| |_|
    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    @trouble1_raunak
   
   
   
   Verifying...
   admin@azurecloud.com False
   support@azurecloud.com False
   Ethan@azurecloud.com False
   Olivia@azurecloud.com False
   Liam@azurecloud.com False
   Lucas@azurecloud.com True
   Harper@azurecloud.com False
   Caden@azurecloud.com False
   steave@azurecloud.com True
   Charlotte@azurecloud.com False
   Grayson@azurecloud.com True
   ---------------------------------------
   [+] List of vaild Emails
   ---------------------------------------
   steave@azurecloud.com
   Lucas@azurecloud.com
   Grayson@azurecloud.com
   
   --- 3.62 seconds ---
   ```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please create a pull request or open an issue with your suggestions or proposed improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

* [Raunak Parmar](https://www.linkedin.com/in/trouble1raunak/)
