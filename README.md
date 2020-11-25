# sam-python-crud-sample

![Github Workflow](https://github.com/aws-samples/sam-python-crud-sample/workflows/Python%20package/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This project is an example of lambda, SAM, dynamodb. This repository contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- src - Code for the application's Lambda function.
- events - Examples of invocation events that you can use to invoke the function.
- tests - Unit tests for the application code.
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions, an API Gateway API and DynamoDB. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project.

### Prerequisites

- git
- make
- python 3.7
- pip
- virtualenv
- vscode
- docker [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)
- SAM CLI [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

### Installing

First of all you need to clone this repository:

``` bash
git clone https://github.com/aws-samples/sam-python-crud-sample.git
```

After clone it, access the folder and you'll need to create a docker network and launch the dynamodb local:

```bash
cd sam-python-crud-sample
make dkn
make dkr
```

#### DynamoDB Local

See this [DYNAMO.md](https://github.com/aws-samples/sam-python-crud-sample/blob/main/DYNAMO.md)

## Running the unit tests

If you want only ro run the unit tests, first create you virtual env:

``` bash
make venv
```

Now let's activate your virtual env:

``` bash
make activate
```

You need to install the requirements and de dev requirements:

``` bash
make requirements
make requirementsdev
```

To run the unit tests, execute:

```bash
make test
```

## Deploy/Test the application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

- **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
- **AWS Region**: The AWS region you want to deploy your app to.
- **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
- **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modified IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
- **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
sam-python-crud-sample$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke CreateActivityFunction --docker-network lambda-local --event events/create_activity_event.json --parameter-overrides Table=Activities Region=us-east-1 AWSEnv=AWS_SAM_LOCAL
sam local invoke GetActivityFunction --docker-network lambda-local --event events/get_activity_event.json --parameter-overrides Table=Activities Region=us-east-1 AWSEnv=AWS_SAM_LOCAL
sam local invoke ListActivitiesFunction --docker-network lambda-local --event events/list_activities_event.json --parameter-overrides Table=Activities Region=us-east-1 AWSEnv=AWS_SAM_LOCAL
sam local invoke UpdateActivityFunction --docker-network lambda-local --event events/update_activity_event.json --parameter-overrides Table=Activities Region=us-east-1 AWSEnv=AWS_SAM_LOCAL
sam local invoke DeleteActivityFunction --docker-network lambda-local --event events/delete_activity_event.json --parameter-overrides Table=Activities Region=us-east-1 AWSEnv=AWS_SAM_LOCAL
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
make server
```

Obs: You can use the NoSQL Workbench for Amazon DynamoDB to manipulate the data.

### Postman

You can find some API calls for postman to help you during the tests into the folder `postman`.

## Add a resource to your application

The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` which lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
sam logs -n <Function> --stack-name sam-python-crud-sample --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name sam-python-crud-sample
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

## Authors

- **Claick Oliveira** - *Initial work* - [claick-oliveira](https://github.com/claick-oliveira)

See also the list of [contributors](https://github.com/aws-samples/sam-python-crud-sample/contributors) who participated in this project.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
