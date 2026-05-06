## DEPLOYMENT TO THE CLOUD: AWS ELASTIC BEANSTALK
#### credential process at the end of this document

Amazon Elastic Beanstalk is one of the services in Amazon AWS. It’s an easy way to deploy your services, also including dockerized containers. It is a Platform as a Service (PaaS) offering that abstracts away the underlying infrastructure and streamlines the deployment, scaling, and management of web applications. With Elastic Beanstalk, developers can focus on writing code, while AWS takes care of provisioning resources, load balancing, auto-scaling, and monitoring.

#### WHO SHOUL USE AWS ELASTIC BEANSTALKS?

AWS Elastic Beanstalk is an excellent choice for startups, small businesses, and development teams looking to streamline the deployment and management of web applications. It’s also suitable for experienced AWS users who want to reduce the operational overhead of managing infrastructure.

#### INSTALLING THE EB CLI

To install the command line interface for AWS Elastic Beanstalk (awsebcli) as a development dependency, you can use the following commands:

`pipenv install awsebcli --dev`

After installing, you can activate the virtual environment with:

`pipenv shell`

Then, initialize an Elastic Beanstalk application with the specified options using:

`eb init -p docker -r <REGION: example - su-west-1> <NAME: churn-serving>`

This command will create an Elastic Beanstalk application named ‘churn-serving’ and generate a ‘.elasticbeanstalk’ folder containing a ‘config.yml’ file, which contains configuration settings for your Elastic Beanstalk environment.

#### DEPLOYING THE MODEL TO THE CLOUD

o create an Elastic Beanstalk environment for your application, you can use the following command:

`eb create churn-serving-env`

This command initiates the creation of an Elastic Beanstalk environment named ‘churn-serving-env.’ Please note that the environment creation is not instantaneous, so it may take a moment to complete. Once the process finishes, you’ll receive information indicating the specific address where your application is available.

An essential point to highlight here is that creating an Elastic Beanstalk environment this way makes it accessible from the internet by default. Therefore, it’s crucial to implement proper security measures and ensure that only authorized services and users have access.

Now, to test our running application, open another terminal window and execute the following command:

`python predict-test.py`

#### FINISHING YOUR PROCESS

To terminate the Elastic Beanstalk environment when you're done with it, you can use the following command:

`eb terminate churn-serving-env` # Deletes the environment (EC2 instances, load balancer, etc.)
`eb terminate --all` # Deletes the application itself in Elastic Beanstalk

This command will gracefully shut down and remove the Elastic Beanstalk environment, helping you manage your resources efficiently.

#### OBTAINING CREDENTIALS

Step 1 - Create the access keys

1. Log in to the AWS Console
2. Click your name (top right corner) > "Security credentials"
3. Scroll down to the "Access keys" section
4. Click "Create access key"
5. On the warning screen, select "Command Line Interface (CLI)" and confirm
6. Click "Create access key"
7. You will see two pieces of information - copy them now, as the Secret Key is only shown once:

`Access key ID:      AKIAIOSFODNN7EXAMPLE`
`Secret access key:  wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

Step 2 - Paste into the terminal
When `eb init` prompts you, paste each one at the right moment
