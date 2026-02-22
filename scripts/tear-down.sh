#!/bin/bash

# Variables
STACK_NAME="ws10-orch-stack"

# Delete the CloudFormation stack
aws cloudformation delete-stack --stack-name $STACK_NAME
echo "CloudFormation stack deletion initiated: $STACK_NAME"
