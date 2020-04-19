![AIAP Banner](https://gallery.mailchimp.com/f98d5ac0a3fbbdcdda35136ab/images/f937a4fd-77b6-416e-9f0f-6f8089ddb084.png "AIAP Banner")

# `Week/Assignment 7:` Deployment of Application

# `Assignment` (Overview & Instructions)

## Overview
Welcome to Week 7 of the coursework! In this week, we will look at deploying a model we have built in previous weeks. We will look at how to properly use this model, put it into a server and let users use it without the need of opening up a Jupyter Notebook.

It is important to note that the skills required will be slightly different from prior weeks due to the nature of this week's assignment. As always, feel free to engage your peers or any of us if you would like more information. For those who are new to serving code, do take the time to understand the underlying concepts instead of just copying code. For those with prior experience, please share your knowledge with those who are new to this topic.

>### Goals for the week:
>
>1. To create a reproducible project.
>2. To learn and understand the basic tools required for deployment.
>3. To deploy an AI/machine learning application.
>4. To have fun :)

# Creating & Deploying an Application (Deliverable)

## `1. Basics (REST API)`

In order to allow users to consume the model(s) we have built, we will need to expose some form of an interface so that the user can interact with it. There can be multiple ways of doing this but the simplest and most common approach is to build a REST API. If you have never built a REST API or don't even know what it is, here are some resources to get you started:
- [API][1]
- [REST API][2]

## `2. Python Flask App`

To build a REST API, you will leverage the popular Python framework: [`Flask`](3). Such application frameworks make it easy for anyone to quickly create web based applications as it provides the basic scaffolding and boilerplate code that are commonly required. 

### Task
Copy your code from ['Assignment 2'](../assignment2/) and figure out how you can build the following two API resources around it using Flask.<br>
Both these resrouces should accept POST requests with bodies, detailed in each collapsible section.

<blockquote>
<details>
    <summary><strong>/train</strong> - this will trigger the model training process</summary>

**Request:** empty JSON body {}    
**Response:** `200 OK` with JSON body:
```json
{"success": 1}
```
Return `1` only if training is successful and `0` otherwise.
</details>
</blockquote>
<blockquote>
<details>
    <summary><strong>/predict</strong> - this will trigger the model inference and return the prediction</summary>

**Request:** JSON object with all the raw features for a single record from the dataset:
```json
{"PassengerId": 1, "Age": 20, "Sex": "m", "Pclass": 1}
```
_(**Note:** Above example JSON only shows partial features.)_

**Response:** JSON body of the following format:
```json
{"PassengerId": 24, "Survived": 1}
```
**`'PassengerId'`** and **`'Survived'`** values should reflect outputs provided by the endpoint, having received the inputs.
<br>
</details>
</blockquote>

### Testing
Once you have the above two endpoints running, check that it works as expected. You can manually test it using tools such as:

- [curl][9]
- [postman][4]

There are also automated tests ready to test them when you commit and 
push your code.

## `3. Containerise the application (Docker)`

### Docker Basics

What is docker? Some useful resources:

- [What is a container?][5]
- [Docker for Beginners][6] (Stop at the section titled *Docker on AWS*.)


### Setup for usage of Docker images

Follow the steps below once you have read
up and understand how to write a Dockerfile:

1. [Install azure-cli][7] for your OS.
2. Login to Docker registry .
```
az login
az acr login -n 100edockerregistry -g 100edockerregistry-rg --subscription ac37cdd4-be55-4c18-b917-ee4a9da523eb
```
3. Create your **Dockerfile** in the base directory of this assignment. Do choose a [prebuilt base image][8] that AISG has already prepared to inherit from. 

4. Build the Docker image. **Replace {your-initial} in command below.**

```
docker build . -t 100edockerregistry.azurecr.io/aiap/{your_initial}:latest
```

## `4. Build, Train and Deploy`

Now that your app is nicely dockerised. Its time to push it through the build pipeline to have it be published.

So far, you have been building the model and packaging it locally. In order to ensure reproducibility of your work, this whole process should be automated and recreated easily. In order to do that, you will need to write a script that will tie this all together.

Fill in the steps required to do so in the [build script (build.sh)](build.sh). Ensure you can run the script locally and it is able to produce the Docker image for your application.

Finally, create a new branch with prefix **deploy-** followed by your name (e.g. 'deploy-jack'). Commit the code and push to this new branch. This will trigger the CI build process on GitLab which will run your `build.sh` script.

## `5. Documentation`

Documentation is extremely important to ensure that when we pass our code on to another analyst or engineer, they will know how to work with and modify the code for their own use. Especially given that AI Singapore needs highly reusable code and exchange of information between teams, we would like to set high standards for documentation.

For this assignment, we would expect a basic level of documentation written in a `README.md` in your repository. This document should discuss what your app would do, and give basic instructions - lines of bash commands - that can guide a user to run your code base on their computer. The right way to do this is to ask a partner to try running your code from a GitHub repository. If it runs with your instructions, you are good to go.

You can even use **this README** as a guide!

---

That's all the instructions for now. Have fun!

<!-- Ref links -->

[1]:https://www.mulesoft.com/resources/api/what-is-an-api/
[2]:https://www.mulesoft.com/resources/api/what-is-rest-api-design
[4]:https://www.getpostman.com/
[5]:https://www.docker.com/resources/what-container
[6]:https://docker-curriculum.com/
[7]:https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest
[8]:http://gitlab.int.aisingapore.org/aisg/base-docker-images
[9]:https://www.booleanworld.com/curl-command-tutorial-examples/
