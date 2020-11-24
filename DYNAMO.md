# Dynamo Local

To configure dynamo local we'll use the NoSQL Workbench for Amazon DynamoDB. To install this tool [click here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html) and to know more [see here](https://aws.amazon.com/pt/blogs/aws/nosql-workbench-for-amazon-dynamodb-available-in-preview/).

## Set up

Inside the folder `data_model` there is a basic example that we'll import using the NoSQL Workbench. To import the model:

![SS01](./images/ss01.png)

After import the model you'll be able to see the model:

![SS02](./images/ss02.png)

Now you need to create a new connection, click on the database icon:

![SS03](./images/ss03.png)

Click on '+ Add connection':

![SS04](./images/ss04.png)

Set the connection name and port (e.g. Local, 8000) and click 'Connect':

![SS05](./images/ss05.png)

Open the new connection:

![SS06](./images/ss06.png)

After test the connection you need to deploy the data model:

![SS07](./images/ss07.png)

In the data modeler screen click on 'Visualize data model':

![SS08](./images/ss08.png)

Now click on 'Commit to DynamoDB':

![SS09](./images/ss09.png)

Choose the connection that was created (e.g Local):

![SS10](./images/ss10.png)

Open the connection again:

![SS11](./images/ss11.png)

The table was created, nice!

![SS12](./images/ss12.png)
