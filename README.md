# Azure AD User Enumeration Tool

The Azure AD User Enumeration Tool is a Python script that allows you to enumerate valid Azure AD user email IDs. By providing a file containing names, the tool will attempt to find the corresponding valid email IDs of users in Azure AD.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/NotSoSecure/AzUserEnum.git```

2. Navigate to the project directory:
    ```
    cd azure-ad-user-enumeration
    ```

## Prerequisites
Before running the script, ensure that you have the following:

- Valid AWS IAM user credentials with API Gateway access.
- An API Gateway created in your AWS account.

To configure your AWS credentials and CLI, run the following command and provide the necessary information:

```
aws configure
```

## Usage
1. Prepare a file named `users.txt` containing the names of users for enumeration, with each name on a new line.

2. Run the script:
   ```
   python AzUserEnum.py -f users.txt -d victim.cloud
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
   admin@victim.cloud False
   support@victim.cloud False
   Ethan@victim.cloud False
   Olivia@victim.cloud False
   Liam@victim.cloud False
   Lucas@victim.cloud False
   Harper@victim.cloud False
   Caden@victim.cloud False
   bob@victim.cloud True
   Charlotte@victim.cloud False
   Grayson@victim.cloud False
   ---------------------------------------
   [+] List of vaild Emails
   ---------------------------------------
   bob@victim.cloud
   
   --- 3.62 seconds ---
   ```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please create a pull request or open an issue with your suggestions or proposed improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

* [Raunak Parmar](https://www.linkedin.com/in/trouble1raunak/)
